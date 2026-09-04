# RE8CH Cloud Tenant Plugins

Public Codex Marketplace for tenant-scoped RE8CH cloud services.
The repository is intentionally anonymous-readable so Codex can discover and
update plugin packages before a tenant signs in.

Repository visibility does not grant cloud access. Each plugin connects to an
OAuth-protected public MCP endpoint. Dex delegates login to GitHub, and the MCP
authorization layer maps the stable OIDC subject to one tenant and its quota.

## Marketplace

- Name: `re8ch-cloud-tenant`
- Git source: `https://github.com/re8ch/codex-cloud-tenant-plugins.git`
- Generic lifecycle: `re8ch-tenant-core`
- Registry: `re8ch-tenant-registry`
- Database: `re8ch-tenant-database`
- Observability: `re8ch-tenant-observability`
- Compatibility package: `re8ch-qwen-tenant-expert`
- MCP resource: `https://tools.re8ch.com/tenant/mcp`
- OIDC issuer: `https://dex.re8ch.com`

The package contains no access token, client secret, Kubernetes credential, or
provider key. Installation and updates are public; runtime use requires OAuth.

The generic packages are purpose-specific views over the same tenant proxy.
Authentication maps the OIDC identity to `admin` or an arbitrary named tenant;
a prompt must never choose or override that mapping. The proxy translates
Consumable grants into application-native authorization and returns only opaque
access references.
