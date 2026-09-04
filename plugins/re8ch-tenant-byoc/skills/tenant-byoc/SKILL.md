---
name: tenant-byoc
description: Register and consume an outbound-only RE8CH BYOC cluster connection.
---

# RE8CH Tenant BYOC

Use only `re8ch-tenant-byoc`. The authenticated tenant is authoritative; never accept a prompted tenant override. Register only cluster UID, HTTPS issuer, public-key identity, region and declared capabilities. Never request or upload a kubeconfig or private key. Return the enrollment reference as opaque and wait for admin approval. A ConsumptionBinding may use only a Ready, non-revoked connection owned by the same tenant. List before revoke; report `RevocationPending` when an offline cluster cannot complete cleanup. Do not call the tenant-admin server.
