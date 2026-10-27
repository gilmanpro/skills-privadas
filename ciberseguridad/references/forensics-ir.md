# Digital Forensics & Incident Response

> Análisis estático/dinámico de malware vive en `references/malware-analysis.md`. Este archivo se enfoca en DFIR: evidencia, volatilidad, timeline, ransomware y detección.

## DFIR Process

### 1. Contención
- **Inmediata:** Desconectar red (no apagar), aislar sistemas comprometidos
- **Preservar evidencia:** Captura de memoria, imagen de disco, logs
- **Documentar:** Todo con timestamps UTC

### 2. Recolección de evidencia
**Volatilidad (de mayor a menor):**
1. Registros de CPU / caché
2. Memoria RAM
3. Estado de red (conexiones, ARP, routing)
4. Procesos en ejecución
5. Archivos temporales
6. Logs del sistema
7. Archivos en disco
8. Backups

**Herramientas:**
```bash
# Captura de memoria
winpmem_mini_x64.exe memdump.raw
avml /tmp/memory.lime  # Linux

# Imagen de disco
dc3dd if=/dev/sda of=disk.img hash=sha256 log=disk.log
FTK Imager (Windows)

# Volatility 3
vol -f memdump.raw windows.pslist
vol -f memdump.raw windows.netscan
vol -f memdump.raw windows.cmdline
vol -f memdump.raw windows.malfind
```

### 3. Timeline reconstruction
```bash
# Plaso / log2timeline
log2timeline.py timeline.plaso disk.img
psort.py -o l2tcsv timeline.plaso -w timeline.csv
```

## Ransomware Response
1. **Aislar** sistemas infectados (no pagar)
2. **Identificar** variante (ransomware-id.com, nomoreransom.org)
3. **Preservar** evidencia (imagen de disco)
4. **Notificar** a CSIRT/CERT nacional
5. **Restaurar** desde backups verificados
6. **Hardening** post-incidente
7. **Reportar** a autoridades si hay robo de datos

## KQL Queries para detección

### Malicious PowerShell
```kql
DeviceProcessEvents
| where FileName == "powershell.exe" or FileName == "pwsh.exe"
| where ProcessCommandLine has_any ("-enc", "bypass", "hidden", "downloadstring", "invoke-expression", "IEX")
| project Timestamp, DeviceName, ProcessCommandLine, InitiatingProcessFileName
```

### Suspicious Scheduled Tasks
```kql
DeviceProcessEvents
| where FileName == "schtasks.exe"
| where ProcessCommandLine has "/create"
| where ProcessCommandLine has_any ("powershell", "cmd", "http", "temp", "appdata")
| project Timestamp, DeviceName, ProcessCommandLine
```

### Lateral Movement Detection
```kql
DeviceLogonEvents
| where LogonType == "Network"
| summarize LoginCount=dcount(DeviceName), Devices=make_set(DeviceName) by AccountName
| where LoginCount > 5
| sort by LoginCount desc
```

### Impossible Travel (Azure/Entra ID)
```kql
SigninLogs
| where TimeGenerated > ago(7d)
| where ResultType == 0
| summarize make_set(Location), make_set(IPAddress) by UserPrincipalName
| where array_length(set_Location) > 1
```
