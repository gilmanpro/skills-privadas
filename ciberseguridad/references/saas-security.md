# Seguridad SaaS — Referencia Completa

> API Security Pentesting (BOLA, mass assignment, GraphQL) vive en `references/pentesting-modes.md` §3. Este archivo se enfoca en amenazas SaaS, SSPM y gobernanza.

## Principales amenazas SaaS

### 1. Account Takeover (ATO)
**Vectores:**
- Credential stuffing (reuso de passwords filtrados)
- Session hijacking via cookies robadas
- OAuth token theft (Evilginx2, AitM phishing)
- MFA fatigue / push bombing
- Device code phishing

**Mitigación:**
- MFA obligatorio (FIDO2/WebAuthn preferido)
- Conditional Access con geofencing
- Token Protection (vincular token a dispositivo)
- Continuous Access Evaluation (CAE)
- Detección de impossible travel (queries KQL en `forensics-ir.md`)

### 2. Data Loss / Exfiltration
**Vectores:**
- Shadow IT (apps no autorizadas)
- Compartición excesiva de archivos
- API keys expuestas
- Exportación masiva de datos
- Email forwarding rules maliciosas

**Mitigación:**
- CASB (Cloud Access Security Broker)
- DLP (Data Loss Prevention) policies
- SSPM (SaaS Security Posture Management)
- Clasificación y etiquetado de datos
- Alerts en sharing excesivo

### 3. Supply Chain Attacks en SaaS
**Vectores:**
- Third-party app integrations con permisos excesivos
- OAuth grants peligrosos
- Webhook endpoints no validados
- Marketplace apps maliciosas

**Mitigación:**
- Revisar permisos de integraciones periódicamente
- OAuth consent policies restrictivas
- App governance en Defender for Cloud Apps
- SBOM de dependencias

## SSPM Checklist
- [ ] MFA habilitado para todos los usuarios admin
- [ ] SSO configurado
- [ ] Session timeout < 24h
- [ ] Password policy: 12+ caracteres, complexity
- [ ] Revisión trimestral de permisos de apps
- [ ] DLP policies activas
- [ ] Audit logging habilitado
- [ ] Alertas de sharing externo configuradas
- [ ] Backup de datos críticos
- [ ] Incident response plan documentado
