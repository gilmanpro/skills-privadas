# Concurrencia en Go — Referencia Completa

## Filosofía de Go: "No se comuniques compartiendo memoria; comparte memoria comunicándote."

Go tiene concurrencia como ciudadano de primera clase. El modelo se basa en **goroutines** (hilos ligeros) y **channels** (tuberías de comunicación).

## Goroutines

Una goroutine es un hilo de ejecución ligero gestionado por el runtime de Go.

```go
go miFuncion()       // lanza miFuncion en una goroutine
go func() { ... }()  // lanza función anónima
```

### Características
- Stack inicial: ~2KB (crece/encoge según necesidad)
- Millones de goroutines son viables
- Multiplexadas sobre hilos del SO (M:N scheduling)
- Comunicación vía channels (preferido) o sync primitives

## Channels

Los channels son tuberías tipadas que conectan goroutines.

### Tipos de channels

| Tipo | Sintaxis | Comportamiento |
|---|---|---|
| Unbuffered | `make(chan T)` | Síncrono: el envío bloquea hasta que alguien recibe |
| Buffered | `make(chan T, N)` | Asíncrono hasta N elementos |
| Send-only | `chan<- T` | Solo se puede enviar |
| Receive-only | `<-chan T` | Solo se puede recibir |

### Operaciones básicas
```go
ch := make(chan int)

ch <- 42            // enviar (bloquea si unbuffered y sin receptor)
valor := <-ch       // recibir (bloquea si no hay datos)
valor, ok := <-ch   // ok=false si channel cerrado y vacío
close(ch)           // cerrar (solo el emisor cierra)
```

### Range sobre channel
```go
for msg := range ch {
    fmt.Println(msg)
}
// El loop termina cuando el channel se cierra
```

### Buffered channels
```go
ch := make(chan int, 3)
ch <- 1  // no bloquea (hay espacio)
ch <- 2  // no bloquea
ch <- 3  // no bloquea
ch <- 4  // BLOQUEA (buffer lleno) hasta que alguien reciba
```

## Select

`select` permite esperar en múltiples operaciones de channel simultáneamente.

```go
select {
case msg := <-ch1:
    fmt.Println("recibido de ch1:", msg)
case ch2 <- "hola":
    fmt.Println("enviado a ch2")
case <-time.After(1 * time.Second):
    fmt.Println("timeout")
default:
    fmt.Println("ningún canal listo")
}
```

### Select con timeout
```go
select {
case res := <-result:
    return res
case <-time.After(5 * time.Second):
    return "", errors.New("timeout")
}
```

### Select con nil channels (útil para desactivar casos)
```go
var ch chan int  // nil
select {
case <-ch:  // nunca se selecciona (channel nil bloquea para siempre)
case <-otherCh:
}
```

## Patrones de concurrencia

### 1. Worker Pool
```go
func worker(id int, jobs <-chan Job, results chan<- Result) {
    for job := range jobs {
        results <- process(job)
    }
}

func main() {
    const numWorkers = 5
    jobs := make(chan Job, 100)
    results := make(chan Result, 100)

    for w := 1; w <= numWorkers; w++ {
        go worker(w, jobs, results)
    }

    for j := 1; j <= 100; j++ {
        jobs <- Job{ID: j}
    }
    close(jobs)

    for r := 1; r <= 100; r++ {
        <-results
    }
}
```

### 2. Fan-Out / Fan-In
```go
// Fan-Out: distribuir trabajo
func generate(nums ...int) <-chan int {
    out := make(chan int)
    go func() {
        for _, n := range nums {
            out <- n
        }
        close(out)
    }()
    return out
}

// Stage de pipeline
func square(in <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        for n := range in {
            out <- n * n
        }
        close(out)
    }()
    return out
}

// Fan-In: mergear múltiples channels
func merge(cs ...<-chan int) <-chan int {
    out := make(chan int)
    var wg sync.WaitGroup
    wg.Add(len(cs))
    
    for _, c := range cs {
        go func(ch <-chan int) {
            for v := range ch {
                out <- v
            }
            wg.Done()
        }(c)
    }
    
    go func() {
        wg.Wait()
        close(out)
    }()
    return out
}
```

### 3. Pipeline
```go
// Stage 1: generador
func gen(nums ...int) <-chan int {
    out := make(chan int)
    go func() {
        for _, n := range nums {
            out <- n
        }
        close(out)
    }()
    return out
}

// Stage 2: procesador
func sq(in <-chan int) <-chan int {
    out := make(chan int)
    go func() {
        for n := range in {
            out <- n * n
        }
        close(out)
    }()
    return out
}

// Uso del pipeline
nums := gen(2, 3, 4, 5)
squares := sq(nums)
for n := range squares {
    fmt.Println(n) // 4, 9, 16, 25
}
```

### 4. Or (merge de channels dinámicos)
```go
func or(channels ...<-chan int) <-chan int {
    switch len(channels) {
    case 0:
        return nil
    case 1:
        return channels[0]
    }

    orDone := make(chan int)
    go func() {
        defer close(orDone)
        
        switch len(channels) {
        case 2:
            select {
            case <-channels[0]:
            case <-channels[1]:
            }
        default:
            select {
            case <-channels[0]:
            case <-channels[1]:
            case <-channels[2]:
            case <-or(append(channels[3:], orDone)...):
            }
        }
    }()
    return orDone
}
```

### 5. Tee (dividir un channel en dos)
```go
func tee(input <-chan int) (_, _ <-chan int) {
    out1 := make(chan int)
    out2 := make(chan int)
    
    go func() {
        defer close(out1)
        defer close(out2)
        
        for val := range input {
            out1 <- val
            out2 <- val
        }
    }()
    return out1, out2
}
```

### 6. Bridge (iterar sobre channels de channels)
```go
func bridge(done <-chan struct{}, chanStream <-chan <-chan int) <-chan int {
    valueStream := make(chan int)
    go func() {
        defer close(valueStream)
        for {
            var stream <-chan int
            select {
            case maybeStream, ok := <-chanStream:
                if !ok {
                    return
                }
                stream = maybeStream
            case <-done:
                return
            }
            for val := range orDone(done, stream) {
                select {
                case valueStream <- val:
                case <-done:
                }
            }
        }
    }()
    return valueStream
}
```

## Context — Cancelación y Deadlines

```go
// Crear context root
ctx := context.Background()   // para entry points (main, init)
ctx := context.TODO()         // cuando no sabes qué context usar

// Con timeout
ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
defer cancel()

// Con deadline
ctx, cancel := context.WithDeadline(context.Background(), time.Now().Add(2*time.Second))
defer cancel()

// Con cancelación manual
ctx, cancel := context.WithCancel(context.Background())
defer cancel()

// Con valores (evitar; usar solo para request-scoped data como request IDs)
ctx = context.WithValue(ctx, "key", "value")

// Verificar cancelación
select {
case <-ctx.Done():
    return ctx.Err()  // DeadlineExceeded o Canceled
default:
}
```

### Patrón: Server con Graceful Shutdown
```go
func main() {
    srv := &http.Server{Addr: ":8080"}
    
    // Canal para señales del sistema
    quit := make(chan os.Signal, 1)
    signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
    
    go func() {
        <-quit
        log.Println("Shutting down...")
        
        ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
        defer cancel()
        
        if err := srv.Shutdown(ctx); err != nil {
            log.Fatal("Server forced to shutdown:", err)
        }
    }()
    
    if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
        log.Fatal(err)
    }
}
```

## sync — Primitivas de sincronización

### WaitGroup
```go
var wg sync.WaitGroup

for i := 0; i < 10; i++ {
    wg.Add(1)
    go func(id int) {
        defer wg.Done()
        fmt.Println(id)
    }(i)
}
wg.Wait()
```

### Mutex / RWMutex
```go
type SafeMap struct {
    mu sync.RWMutex
    m  map[string]string
}

func (s *SafeMap) Get(key string) string {
    s.mu.RLock()
    defer s.mu.RUnlock()
    return s.m[key]
}

func (s *SafeMap) Set(key, value string) {
    s.mu.Lock()
    defer s.mu.Unlock()
    s.m[key] = value
}
```

### Once (ejecutar una sola vez)
```go
var once sync.Once
var instance *Singleton

func GetInstance() *Singleton {
    once.Do(func() {
        instance = &Singleton{}
    })
    return instance
}
```

### Pool (reutilización de objetos)
```go
var bufPool = sync.Pool{
    New: func() any {
        return new(bytes.Buffer)
    },
}

func write(w io.Writer, data string) {
    buf := bufPool.Get().(*bytes.Buffer)
    defer bufPool.Put(buf)
    buf.Reset()
    buf.WriteString(data)
    w.Write(buf.Bytes())
}
```

### Map (concurrente, especializado)
```go
var m sync.Map

m.Store("key", "value")
value, ok := m.Load("key")
m.LoadOrStore("key", "default")
m.Delete("key")
m.Range(func(key, value any) bool {
    fmt.Println(key, value)
    return true // continuar iteración
})
```

## Atomic operations

```go
var counter atomic.Int64  // Go 1.19+

counter.Add(1)
value := counter.Load()
counter.Store(42)

// Versión pre-1.19
var counter int64
atomic.AddInt64(&counter, 1)
atomic.LoadInt64(&counter)
atomic.StoreInt64(&counter, 42)
```

## Data Race Detector

Siempre corre tests con `-race`:
```bash
go test -race ./...
go build -race .
```

El detector imprime un stack trace detallado cuando detecta un race condition.

## Best practices de concurrencia

### 1. No lances goroutines sin saber cómo terminan
```go
go work()  // ¿quién espera a esta goroutine?
```
Solución: usa WaitGroup, channels, o context.

### 2. El que envía datos cierra el channel
```go
// Emisor cierra
go func() {
    for _, item := range items {
        ch <- item
    }
    close(ch)  // el emisor cierra
}()

// Receptor itera
for item := range ch {
    // ...
}
```

### 3. Mantén las goroutines bajo tu control
- Usa `go` solo en el nivel más alto (main, handlers, test functions)
- No lances goroutines en bibliotecas (a menos que documentes cómo detenerlas)

### 4. Prefiere channels sobre mutexes (pero usa mutex cuando sea apropiado)
- Channels: flujo de datos, comunicación
- Mutex: protección de estado compartido

### 5. Siempre usa context para operaciones que puedan cancelarse
- Todas las operaciones de red/DB deben aceptar context
- Los timers/deadlines son obligatorios en servidores

### 6. Cuidado con goroutine leaks
```go
// LEAK: worker nunca termina
func leak() {
    ch := make(chan int)
    go func() { // se queda esperando siempre
        val := <-ch
        fmt.Println(val)
    }()
}
```

### 7. Usa errgroup para manejar errores en goroutines
Paquete: `golang.org/x/sync/errgroup`

```go
g, ctx := errgroup.WithContext(context.Background())

urls := []string{"http://...", "http://..."}
for _, url := range urls {
    url := url
    g.Go(func() error {
        resp, err := http.Get(url)
        if err != nil { return err }
        defer resp.Body.Close()
        // ...
        return nil
    })
}

if err := g.Wait(); err != nil {
    log.Fatal(err)
}
```

## Anti-patrones

### ❌ Channel como promise/future
```go
ch := make(chan Result)
go func() {
    ch <- doWork()
}()
result := <-ch
```
✅ Mejor: devolver el channel desde una función factory.

### ❌ Buffer grande en channel como sustituto de estructura de datos
```go
ch := make(chan int, 1000000)  // probablemente deberías usar un slice
```

### ❌ Compartir variable sin protección
```go
var counter int  // nunca accedas a esto concurrentemente sin mutex/atomic
```

---

# Optimización Computacional con Múltiples Hilos

## Concurrencia ≠ Paralelismo (importante distinguir)

| Concepto | Definición | En Go |
|---|---|---|
| **Concurrencia** | Estructurar el programa como múltiples tareas independientes | Gorutinas + channels (composición) |
| **Paralelismo** | Ejecutar múltiples tareas SIMULTÁNEAMENTE en múltiples núcleos | GOMAXPROCS + worker pools |

Go te da CONCURRENCIA por defecto (gorutinas). El PARALELISMO requiere:
1. Múltiples núcleos (hardware)
2. `GOMAXPROCS` configurado correctamente
3. Trabajo CPU-bound que pueda dividirse

## GOMAXPROCS — El control maestro del paralelismo

```go
import "runtime"

// Cuántos núcleos tenemos?
nucleos := runtime.NumCPU()         // ej: 8
fmt.Println(runtime.GOMAXPROCS(0))  // valor actual

// Configurar (default = NumCPU, casi siempre óptimo)
runtime.GOMAXPROCS(nucleos)

// Para CPU-bound puro: GOMAXPROCS = NumCPU()
// Para I/O-bound mixto: GOMAXPROCS puede ser NumCPU() * 1.5 o 2
// Para contenedores con límites de CPU: usar cgroup
```

### Cómo GOMAXPROCS afecta el rendimiento

| GOMAXPROCS | CPU-bound (8 núcleos) | I/O-bound | Explicación |
|---|---|---|---|
| 1 | 1x (lento) | Bien | Una sola gorutina a la vez |
| 4 | ~4x | Bien | 4 gorutinas simultáneas |
| 8 (óptimo) | ~8x | Bien | Todas las gorutinas posibles |
| 16 | ~8x (no mejora) | Puede ayudar | Oversubscription si hay I/O esperando |

## Patrón: Worker Pool CPU-bound (el más IMPORTANTE para optimización)

Este es el patrón que MAXIMIZA el uso de todos los núcleos:

```go
// parallelMap aplica fn a cada elemento usando TODOS los núcleos
func parallelMap[T, U any](items []T, fn func(T) U) []U {
    numWorkers := runtime.NumCPU()
    chunkSize := (len(items) + numWorkers - 1) / numWorkers

    type result struct {
        index int
        value U
    }

    results := make([]U, len(items))
    resultCh := make(chan result, len(items))

    var wg sync.WaitGroup
    for w := 0; w < numWorkers; w++ {
        wg.Add(1)
        start := w * chunkSize
        end := start + chunkSize
        if end > len(items) {
            end = len(items)
        }
        if start >= len(items) {
            wg.Done()
            break
        }

        go func(s, e int) {
            defer wg.Done()
            for i := s; i < e; i++ {
                resultCh <- result{i, fn(items[i])}
            }
        }(start, end)
    }

    go func() {
        wg.Wait()
        close(resultCh)
    }()

    for r := range resultCh {
        results[r.index] = r.value
    }
    return results
}

// Uso: paralelismo REAL en N núcleos
resultados := parallelMap(millonesDeItems, procesamientoPesado)
```

## Patrón: Procesamiento por lotes (Batch Processing)

```go
func processInBatches[T any](items []T, batchSize int, fn func([]T)) {
    numWorkers := runtime.NumCPU()
    work := make(chan []T, len(items)/batchSize+1)
    done := make(chan struct{})

    // Workers consumen lotes
    for w := 0; w < numWorkers; w++ {
        go func() {
            for batch := range work {
                fn(batch)  // cada worker procesa un lote EN PARALELO
            }
            done <- struct{}{}
        }()
    }

    // Productor envía lotes
    for i := 0; i < len(items); i += batchSize {
        end := i + batchSize
        if end > len(items) {
            end = len(items)
        }
        work <- items[i:end]
    }
    close(work)

    // Esperar todos los workers
    for w := 0; w < numWorkers; w++ {
        <-done
    }
}

// Procesar 10 millones de registros en lotes de 1000, usando 8 núcleos
// Tiempo secuencial: ~40s → Tiempo paralelo: ~5s (8x mejora)
```

## Patrón: Divide y Vencerás Paralelo (Parallel Divide & Conquer)

```go
// MergeSort paralelo — O(n log n) con todos los núcleos
func parallelMergeSort(items []int) []int {
    if len(items) <= 1 {
        return items
    }

    mid := len(items) / 2

    // Para datasets pequeños, usa ordenamiento secuencial
    if len(items) < 10000 {
        return merge(
            parallelMergeSort(items[:mid]),
            parallelMergeSort(items[mid:]),
        )
    }

    // Para datasets grandes: divide en PARALELO
    var left, right []int
    var wg sync.WaitGroup
    wg.Add(1)

    go func() {
        defer wg.Done()
        left = parallelMergeSort(items[:mid])
    }()
    right = parallelMergeSort(items[mid:])

    wg.Wait()
    return merge(left, right)
}

func merge(left, right []int) []int {
    result := make([]int, 0, len(left)+len(right))
    i, j := 0, 0
    for i < len(left) && j < len(right) {
        if left[i] <= right[j] {
            result = append(result, left[i])
            i++
        } else {
            result = append(result, right[j])
            j++
        }
    }
    result = append(result, left[i:]...)
    result = append(result, right[j:]...)
    return result
}
```

## Patrón: Semáforo para controlar paralelismo máximo

```go
// Limitar a N gorutinas concurrentes (evita saturación)
func concurrentProcess(items []Item, maxConcurrent int, fn func(Item)) {
    sem := make(chan struct{}, maxConcurrent)
    var wg sync.WaitGroup

    for _, item := range items {
        wg.Add(1)
        sem <- struct{}{}  // bloquea si ya hay maxConcurrent gorutinas
        go func(i Item) {
            defer wg.Done()
            defer func() { <-sem }()  // libera slot
            fn(i)
        }(item)
    }
    wg.Wait()
}

// Ejemplo: procesar 10000 URLs con máximo 20 conexiones concurrentes
concurrentProcess(urls, 20, fetchURL)
```

## Benchmarking de paralelismo

### Comparación secuencial vs paralelo
```go
func BenchmarkSequencial(b *testing.B) {
    data := generateData(100000)
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        processSequential(data)
    }
}

func BenchmarkParalelo_1Worker(b *testing.B) {
    data := generateData(100000)
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        processParallel(data, 1)
    }
}

func BenchmarkParalelo_4Workers(b *testing.B) {
    data := generateData(100000)
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        processParallel(data, 4)
    }
}

func BenchmarkParalelo_8Workers(b *testing.B) {
    data := generateData(100000)
    b.ResetTimer()
    for i := 0; i < b.N; i++ {
        processParallel(data, 8)
    }
}
```

```bash
# Ejecutar con GOMAXPROCS explícito para medir escalabilidad
GOMAXPROCS=1 go test -bench=BenchmarkParalelo -benchmem
GOMAXPROCS=2 go test -bench=BenchmarkParalelo -benchmem
GOMAXPROCS=4 go test -bench=BenchmarkParalelo -benchmem
GOMAXPROCS=8 go test -bench=BenchmarkParalelo -benchmem
```

### Interpretación de resultados

| Workers | Tiempo | Speedup | Eficiencia |
|---|---|---|---|
| 1 (secuencial) | 100s | 1x | 100% |
| 2 | 50s | 2x | 100% |
| 4 | 25s | 4x | 100% |
| 8 | 13s | 7.7x | 96% (overhead scheduling) |
| 16 | 14s | 7.1x | 44% (oversubscription) |

> **Ley de Amdahl:** Si el 95% del trabajo es paralelizable, el speedup máximo en 8 núcleos es ~6x. No todo se puede paralelizar.

## Casos de uso REALES de paralelismo en Go

### 1. Procesamiento de imágenes por lote
```go
func processImagesConcurrently(files []string) error {
    sem := make(chan struct{}, runtime.NumCPU())
    var wg sync.WaitGroup
    errCh := make(chan error, len(files))

    for _, f := range files {
        wg.Add(1)
        sem <- struct{}{}
        go func(filename string) {
            defer wg.Done()
            defer func() { <-sem }()
            if err := processImage(filename); err != nil {
                errCh <- fmt.Errorf("procesando %s: %w", filename, err)
            }
        }(f)
    }

    wg.Wait()
    close(errCh)

    for err := range errCh {
        if err != nil {
            return err
        }
    }
    return nil
}
// Resultado: 1000 imágenes en 8 núcleos → ~8x más rápido que secuencial
```

### 2. Web scraping paralelo
```go
func scrapeURLs(urls []string) []ScrapedData {
    results := make([]ScrapedData, 0, len(urls))
    mu := sync.Mutex{}
    var wg sync.WaitGroup
    sem := make(chan struct{}, 20)  // max 20 conexiones concurrentes

    for _, url := range urls {
        wg.Add(1)
        sem <- struct{}{}
        go func(u string) {
            defer wg.Done()
            defer func() { <-sem }()
            data := scrape(u)
            mu.Lock()
            results = append(results, data)
            mu.Unlock()
        }(url)
    }

    wg.Wait()
    return results
}
```

### 3. Cálculos matemáticos masivos (Monte Carlo, matrices, etc.)
```go
// Estimación de Pi con Monte Carlo paralelo
func estimatePi(samples int) float64 {
    workers := runtime.NumCPU()
    samplesPerWorker := samples / workers
    ch := make(chan int, workers)

    for w := 0; w < workers; w++ {
        go func() {
            count := 0
            rng := rand.New(rand.NewSource(time.Now().UnixNano()))
            for i := 0; i < samplesPerWorker; i++ {
                x, y := rng.Float64(), rng.Float64()
                if x*x+y*y <= 1 {
                    count++
                }
            }
            ch <- count
        }()
    }

    total := 0
    for w := 0; w < workers; w++ {
        total += <-ch
    }
    return 4.0 * float64(total) / float64(samples)
}
// Precisión: a más samples, mejor. Velocidad: 8x en 8 núcleos.
```

### 4. Procesamiento de logs / archivos de texto
```go
func countWordsInFiles(files []string) map[string]int {
    results := make(chan map[string]int, len(files))
    var wg sync.WaitGroup

    for _, f := range files {
        wg.Add(1)
        go func(filename string) {
            defer wg.Done()
            results <- countWords(filename)
        }(f)
    }

    go func() {
        wg.Wait()
        close(results)
    }()

    total := make(map[string]int)
    for partial := range results {
        for word, count := range partial {
            total[word] += count
        }
    }
    return total
}
```

## Medición y profiling de paralelismo

```go
import "runtime"

func trackParallelEfficiency(workers int, fn func()) {
    before := time.Now()
    fn()
    elapsed := time.Since(before)

    // Eficiencia = speedup / workers * 100
    // speedup = tiempo_1_worker / tiempo_N_workers
    fmt.Printf("Workers: %d, Tiempo: %v\n", workers, elapsed)
}
```

### Profile con pprof para detectar cuellos de botella
```bash
# Profile de CPU con paralelismo
go test -bench=. -cpuprofile=cpu.prof

# Analizar: ¿las gorutinas están realmente en paralelo?
go tool pprof -http=:8080 cpu.prof
# Buscar: mutex contention, scheduling latency, goroutine blocking
```

## Checklist para optimización multi-hilo

- [ ] `GOMAXPROCS` está configurado (default es bueno para CPU-bound)
- [ ] El trabajo es CPU-bound (no I/O-bound disfrazado)
- [ ] El overhead de dividir trabajo no domina el tiempo de cómputo
- [ ] No hay data races (verificado con `go test -race`)
- [ ] Los workers tienen chunks de trabajo suficientemente grandes (>1ms por chunk)
- [ ] Los canales tienen buffer adecuado (o son unbuffered cuando toca)
- [ ] Se midió speedup real vs secuencial (benchmarks)
- [ ] Se verificó que no hay goroutine leaks
- [ ] La eficiencia de paralelismo es >70% (speedup / workers)
- [ ] Si hay I/O, se usó semáforo para limitar concurrencia

