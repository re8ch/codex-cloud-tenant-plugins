# RE8CH Cloud Tenant Plugin

Public Codex Marketplace for tenant-scoped RE8CH cloud services. The repository
is intentionally anonymous-readable so Codex can discover and update the plugin
before a tenant signs in.

Repository visibility does not grant cloud access. The plugin connects to an
OAuth-protected public MCP endpoint. Dex delegates login to GitHub, and the MCP
authorization layer maps the stable OIDC subject to exactly one tenant and its
quota.

## Marketplace

- Name: `re8ch-cloud-tenant`
- Git source: `https://github.com/re8ch/codex-cloud-tenant-plugins.git`
- Tenant package: `re8ch-tenant`
- MCP resource: `https://tools.re8ch.com/tenant/mcp`
- OIDC issuer: `https://dex.re8ch.com`

The marketplace intentionally exposes one generic tenant package. Registry,
database, observability, workload, and BYOC behavior are reusable skills inside
that package rather than separate plugins. Tenant-specific packages and names do
not belong in this shared catalog.

Authentication maps the OIDC identity to exactly one named tenant; a prompt
must never choose or override that mapping. TenantGrant authorization determines
which Consumables the caller can use. The proxy translates those grants into
application-native authorization and returns only opaque access references.

Tenant creation, identity binding, grant mutation, and BYOC approval are not
tenant self-service operations. They remain on the separately protected admin
interface.

The package contains no access token, client secret, Kubernetes credential, or
provider key. Installation and updates are public; runtime use requires OAuth.
