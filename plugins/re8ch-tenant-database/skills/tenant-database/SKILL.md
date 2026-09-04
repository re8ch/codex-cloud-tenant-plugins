---
name: tenant-database
description: Provision and manage tenant-isolated RE8CH PostgreSQL Consumables.
---

# RE8CH Tenant Database

Use only `re8ch-tenant-database` and only
`database.postgresql.shared.v1`. OAuth identity fixes the tenant.

1. Discover and plan before provisioning. Show storageGiB, connectionClass,
   backupClass, retentionClass, region, quota impact and approval state.
2. Create, update, suspend, resume or delete only after explicit instruction,
   reusing the plan hash and a stable idempotency key.
3. Storage may expand but never shrink. Deletion is soft and retention-aware.
4. Bindings return an opaque `accessRef`; never reveal database passwords,
   Kubernetes Secrets, node addresses or Pigsty credentials.
5. Do not use PostgreSQL admin, Pigsty, Kubernetes or storage administration tools.
