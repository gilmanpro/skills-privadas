# Auditoría y Detección de Intrusiones en Linux

Módulo defensivo basado en guías de TuxCare (detección de intrusiones) y SentinelOne
(auditoría de seguridad de Linux). Aplica a **hosts Linux propios o autorizados**:
evalúa postura de seguridad, endurece configuraciones y detecta compromisos.

- Fuente IDS: https://tuxcare.com/es/blog/linux-intrusion-detection/
- Fuente auditoría: https://www.sentinelone.com/es/cybersecurity-101/cybersecurity/linux-security-audit/

## 1. Cuándo usar este módulo

- Petición de auditoría/hardening de un servidor Linux (local o remoto con acceso autenticado).
- Sospecha de compromiso o verificación post-incidente (triaje).
- Cumplimiento (RGPD, PCI-DSS, HIPAA, benchmarks CIS).
- Implementar monitoreo (IDS/SIEM) en infraestructura Linux.

Al finalizar, genera `security/report.md` con hallazgos y severidades, igual que el resto de la skill.

## 2. Auditoría de seguridad de Linux (proceso en 8 pasos)

Ejecuta el script automatizado o los comandos por paso:

```bash
sudo ./scripts/linux-audit.sh            # recolecta toda la evidencia en security/linux-audit-*
```

### Paso 1 — Definir alcance
Define hosts, aplicaciones y requisitos de cumplimiento antes de empezar.
Solo audita máquinas con autorización por escrito.

### Paso 2 — Información del sistema
```bash
uname -a && cat /etc/os-release && uptime
hostnamectl
df -h && free -h          # recurso (para detectar minado: CPU/memoria altos)
```

### Paso 3 — Cuentas de usuario
```bash
awk -F: '$3==0 {print $1": UID 0 (root)"}' /etc/passwd   # cuentas con privilegios de root
grep -E '(/bin/bash|/bin/sh|/bin/zsh)$' /etc/passwd       # cuentas con shell
last -25 && w                                              # accesos recientes y activos
grep -rhvE '^\s*(#|$)' /etc/sudoers /etc/sudoers.d/       # reglas sudo
```
Señales: UID 0 que no sean `root` → High. Cuentas inactivas con shell → Medium.
Usuarios con sudo NOPASSWD → revisar (Medium/High según perfil).

### Paso 4 — Permisos de archivos
```bash
find / -xdev -perm -4000 -type f 2>/dev/null   # SUID (escalada local)
find / -xdev -perm -2000 -type f 2>/dev/null   # SGID
find / -xdev -type f -perm -0002 2>/dev/null   # world-writable
ls -la /etc/passwd /etc/shadow /etc/gshadow /etc/ssh/ 2>/dev/null
```
Señales: `/etc/shadow` con permisos distintos de `-rw-r-----` → Critical.
SUID en binarios no estándar (`/tmp`, `/home`, `nc`, `busybox`) → High.

### Paso 5 — Software y actualizaciones
```bash
# Debian/Ubuntu
dpkg -l | wc -l
apt list --upgradable 2>/dev/null | grep -i security
# RHEL/CentOS/Fedora
rpm -qa | wc -l
yum check-update --security
# Debilidades conocidas en paquetes instalados
sudo apt install -y debsecan lynis 2>/dev/null; debsecan 2>/dev/null | head -40
```
Señales: paquetes con CVE público sin parche → High/Critical (usa `cve-lookup.sh` o
`debsecan`/`trivy fs .` para el mapeo). Software innecesario en ejecución → Low/Medium.

### Paso 6 — Logs de auditoría
```bash
grep -E 'Failed password|Invalid user' /var/log/auth.log | tail -30   # RHEL: /var/log/secure
journalctl -u ssh --no-pager -n 30
last -n 20 && lastb -n 20 2>/dev/null        # últimos y fallidos
```
Verifica que `auditd` esté activo: `systemctl status auditd` (objetivo A07/Defense).

### Paso 7 — Análisis de vulnerabilidades
```bash
sudo lynis audit system --quick        # benchmark CIS-ish con puntaje
apt install -y chkrootkit rkhunter; chkrootkit; rkhunter --check --skip-keypress
```
Lynis da un índice de hardening (0-100) y lista sugerencias; prioriza las de severidad alta.

### Paso 8 — Documentar y remediar
Resume hallazgos en `security/report.md` con: severidad, evidencia (archivo+línea),
reproducción, remediación y mapeo CIS/OWASP/MITRE. Ejemplo:

```markdown
## [High] Aceptar logins root remotos por SSH
- **Evidencia:** `grep -E 'PermitRootLogin|PasswordAuthentication' /etc/ssh/sshd_config`
- **Remediación:** `PermitRootLogin no` + `PasswordAuthentication no` + claves SSH.
- **CIS:** 5.2.x · **MITRE:** T1078 (Valid Accounts)
```

## 3. Checklist rápida (SentinelOne)

1. Examina cuentas de usuario (inactivas, UID 0, shells).
2. Verifica privilegios de administrador (sudo, root directo).
3. Aplica políticas de contraseñas y autenticación (PAM + MFA).
4. Revisa la configuración SSH (`/etc/ssh/sshd_config`).
5. Comprueba actualizaciones de seguridad pendientes.
6. Audita red: puertos abiertos, servicios expuestos, firewall.
7. Evalúa acceso no autorizado (logins fallidos, accesos raros).
8. Busca malware/rootkits (chkrootkit, rkhunter, clamav).
9. Aplica mínimo privilegio (RBAC, umask 027, sudoers mínimo).

## 4. Hardening esencial (remediaciones típicas)

### SSH
```
# /etc/ssh/sshd_config
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
MaxAuthTries 3
AllowUsers alice bob        # solo cuentas necesarias
```
`systemctl restart ssh && ssh -t <host> 'sshd -T | grep -Ei "permitrootlogin|passwordauthentication"'`

### Firewall (solo abre lo necesario)
```bash
sudo ufw default deny incoming && sudo ufw allow 22/tcp && sudo ufw enable
# o con nftables/iptables; auditar con: ss -tulnp
```

### Password policy (PAM) + MFA
```
# /etc/security/pwquality.conf
minlen = 14
minclass = 4
# sudo pam_faillock para lockout de 5 intentos; MFA: google-authenticator/libpam-google-authenticator
```

### Actualizaciones automáticas de seguridad
```bash
# Debian/Ubuntu
sudo apt install -y unattended-upgrades && sudo dpkg-reconfigure --priority=low unattended-upgrades
# RHEL
sudo dnf install -y dnf-automatic && sudo systemctl enable --now dnf-automatic.timer
```

### Monitoreo de integridad
```bash
sudo apt install -y aide && sudo aideinit && sudo mv /var/lib/aide/aide.db.new /var/lib/aide/aide.db
sudo aide.wrapper --check   # en cron diario
```

## 5. Detección de intrusiones (IDS)

### NIDS (red) — Snort / Suricata
```bash
sudo apt install -y snort    # o suricata
# config: /etc/snort/snort.conf (redes internas, reglas)
sudo snort -c /etc/snort/snort.conf -i eth0 -l /var/log/snort -A alert_fast
# actualizar reglas periódicamente (pulledpork/OpenAppID o reglas de Emerging Threats)
```
Regla básica de prueba:
```
alert tcp any any -> 192.168.0.0/16 80 (msg:"HTTP a la LAN"; sid:1000001;)
```

### HIDS (host) — OSSEC / Wazuh
```bash
# OSSEC (HIDS clásico)
wget https://github.com/ossec/ossec-hids/archive/3.6.0.tar.gz
tar xzf 3.6.0.tar.gz && cd ossec-hids-3.6.0 && sudo ./install.sh
sudo /var/ossec/bin/ossec-control start && sudo /var/ossec/bin/ossec-control status
# config: /var/ossec/etc/ossec.conf → <localfile> para /var/log/auth.log, reglas, rootcheck
```
Monitorea logs, detecta rootkits (rootcheck), integridad (syscheck) y respuesta activa.
Wazuh es la evolución moderna: agente + servidor + Kibana (SIEM).

### Integridad de archivos — AIDE / Tripwire
Compara hashes de archivos críticos (`/etc`, `/usr/bin`, `/root`) ante cambios no
autorizados. IDS de integridad: `sudo aide.wrapper --check` (ver §4).

### Análisis de logs centralizado
ELK (Elasticsearch+Logstash+Kibana), Graylog o Splunk: agrega logs de todos los hosts,
alerta en tiempo real y da correlación. Configura rotación (`/etc/logrotate.d/`) y cifrado.

## 6. Registros que auditar y patrones de búsqueda

| Log | Ruta | Qué buscar |
|---|---|---|
| Auth | `/var/log/auth.log` (Debian) / `/var/log/secure` (RHEL) | logins fallidos, `Invalid user`, `Accepted` a horas raras, sudo |
| Sistema | `/var/log/syslog` / `journalctl` | errores, reinicios, servicios |
| Kernel | `dmesg` | drivers/loads de kernel anómalos |
| Firewall | logs de iptables/nftables | scans, conexiones bloqueadas repetidas |
| Fallidos | `/var/log/btmp` (`lastb`) | fuerza bruta |
| Auditd | `/var/log/audit/audit.log` | cambios en archivos, execs, sudo |

Patrones de caza:
```bash
# Fuerza bruta SSH
grep -E 'Failed password' /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -rn | head
# Cuentas usadas en intentos
grep -E 'Invalid user' /var/log/auth.log | awk '{print $(NF-2)}' | sort | uniq -c | sort -rn | head
# Logins aceptados raros
grep 'Accepted' /var/log/auth.log | tail -30
# Cambios en archivos críticos (auditd)
ausearch -k file_monitor 2>/dev/null | tail -40
```
High: >5 logins fallidos desde una IP → considerar fail2ban.

## 7. Triaje de compromiso (respuesta)

Ante sospecha, **no modifiques nada** (no apagues, no edites): preserva evidencia
(imagen de memoria, copia de `/var/log` y `.bash_history`), aísla el host de la red
y ejecuta:

```bash
sudo ./scripts/linux-intrusion-triage.sh    # triaje de lectura en 12 pasos
```

Señales típicas (IOC) a buscar: procesos de minado (`xmrig`, `kinsing`, `kdevtmpfsi`),
conexiones a IPs desconocidas, binarios SUID nuevos, cron/at maliciosos, usuarios nuevos
con UID 0, bash_history con `wget|curl` de fuentes raras, rootkits (chkrootkit/rkhunter),
logs de auth borrados o con huecos.

## 8. Scripts incluidos

| Script | Uso |
|---|---|
| `scripts/linux-audit.sh` | Auditoría automatizada: sistemas, cuentas, permisos, software, red, servicios, logs, rootkits → `security/linux-audit-*` |
| `scripts/linux-intrusion-triage.sh` | Triaje rápido de compromiso (solo lectura) en 12 pasos |

Ambos requieren Linux y normalmente `sudo` (para leer `/var/log` y correr scanners).
No son aplicables en Windows (ahí usa `security-scan.bat` como base).

## 9. Reglas del módulo

1. Solo auditar hosts propios o con autorización por escrito (es postura defensiva, no requiere
   exploit, pero igual aplica el alcance de la skill).
2. Los scripts y comandos son **de solo lectura** salvo las remediaciones explícitas
   (editar `sshd_config`, instalar herramientas): no modifques configuración sin pedirlo.
3. No expongas hashes, claves, o datos de usuarios en el reporte; redacta como los secretos.
4. Prioriza por severidad: acceso root/SSH discrecional > paquetes sin parche > permisos > log.
5. Guarda toda evidencia en `security/evidence/` y resume en `security/report.md`.