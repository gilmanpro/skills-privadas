# Cloud Security — AWS / Azure / GCP / Containers

> Incluye pentesting cloud (antes en `pentesting-modes.md` §6) consolidado aquí.

## AWS Security

### Reconocimiento
```bash
aws iam list-users
aws iam list-roles
aws iam list-policies --scope Local
aws sts get-caller-identity
```

### Vectores de ataque
- **S3 bucket público:** `aws s3 ls s3://target-bucket --no-sign-request`
- **Metadata service (IMDSv1):** `curl http://169.254.169.254/latest/meta-data/iam/security-credentials/`
- **Lambda env vars:** pueden contener secrets
- **Privilege escalation:** políticas `*:*`, role chaining, confused deputy
- **CloudTrail tampering:** deshabilitar logging
- **Cross-account access:** resource policies mal configuradas

### Hardening
- IMDSv2 obligatorio
- SCPs restrictivos
- AWS Config Rules + Security Hub
- GuardDuty en todas las regiones
- KMS con rotación automática
- VPC Flow Logs activos

## Azure Security

### Reconocimiento
```powershell
Get-AzResource
Get-AzRoleAssignment
Get-AzADUser
Get-AzADServicePrincipal
```

### Vectores de ataque
- **Blob Storage público:** acceso anónimo
- **Managed Identity abuse:** VMs con identidades privilegiadas
- **Runbook automation:** ejecución de código
- **Azure AD Connect:** robo de hashes on-premises
- **Guest user invitations:** acceso externo

### Hardening
- Conditional Access Policies
- PIM (Privileged Identity Management)
- Azure Defender for Cloud
- NSGs restrictivos
- Azure Key Vault

## GCP Security

### Reconocimiento
```bash
gcloud projects list
gcloud iam service-accounts list
gcloud compute instances list
gsutil ls
```

### Vectores de ataque
- **GCS bucket público:** sin autenticación
- **Service account key extraction:** JSON keys en repos
- **Project hopping:** cross-project via IAM
- **Cloud Functions:** permisos excesivos

### Hardening
- Organization Policy Constraints
- VPC Service Controls
- Binary Authorization
- Cloud Armor (WAF)
- Security Command Center

## Container Security (K8s / Docker)

### Escaneo
```bash
trivy image myapp:latest
grype myapp:latest
docker scout cves myapp:latest
```

### Vectores de ataque
- Container escape via privileged mode
- K8s API server sin auth
- Secrets en env vars (no en Secrets Manager)
- RBAC demasiado permisivo
- kubelet API accesible

### Hardening
- Pod Security Standards (restricted)
- Network Policies
- OPA/Gatekeeper
- Falco para runtime detection
- Image signing con Cosign/Notary
- Read-only root filesystem
- Non-root containers
