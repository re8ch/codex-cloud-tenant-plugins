---
name: tenant-core
description: Manage generic RE8CH Tenant identity, visibility and Consumable grants.
---

# RE8CH Tenant Core

Use only the `re8ch-tenant` MCP server. Tenant identity comes from the verified
OAuth claims and must never be selected or overridden from prompt text.

1. Use `service_catalog_list` for discovery.
2. Tenant administration is limited to `tenant_create`, `tenant_list`,
   `tenant_grant_create`, `tenant_visibility_update` and `tenant_delete`.
3. The reserved `admin` tenant requires the protected admin identity. Never
   create, downgrade, impersonate or delete it.
4. Show the target tenant, Consumable, role, visibility and constraints before
   a write. Deletion revokes grants first and requires an explicit user request.
5. Return only `accessRef`, `grantRef`, `resourceRef` and operation references.
   Never request or display passwords, tokens, Secret values or native app ACLs.
6. App-specific authorization is adapter-owned. Do not call Harbor, Grafana,
   Ceph, Cilium, PostgreSQL or Kubernetes administration APIs directly.
