---
name: tenant-observability
description: Manage tenant Grafana and datasource access through RE8CH Consumables.
---

# RE8CH Tenant Observability

Use only `re8ch-tenant-observability` and the
`observability.grafana.v1` Consumable. OAuth identity fixes the tenant.

1. Discover and plan before creating access.
2. Require `datasourceRefs` and either `organizationRef` or `folderRefs`.
   Use only viewer or editor plans and explain the visibility boundary.
3. Create or revoke an opaque binding after explicit instruction. Never request
   Grafana API keys, datasource passwords or Victoria backend credentials.
4. Grafana is the shared UI; organizations, folders and datasources are the
   tenant authorization units. Metrics, logs, retention and queries are usage facts.
5. Do not call Grafana admin, Victoria, Kubernetes or qianwen-ops proxy APIs directly.
