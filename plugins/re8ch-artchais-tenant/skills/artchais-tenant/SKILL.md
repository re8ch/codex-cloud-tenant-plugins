---
name: artchais-tenant
description: Operate the Artchais artc cluster through role-scoped RE8CH AmongClusters access.
---

# Artchais Tenant

Use only `re8ch-artchais-tenant`. GitHub login and the server-resolved Artchais team role are authoritative; never accept a prompted tenant, role, kubeconfig, token, server address or client certificate.

Use `artc_kubernetes_read` for inspection. It deliberately excludes Secret and ConfigMap data. Use `artc_kubernetes_apply` for an Artchais workload only after showing the preview; it forces the `artchais` namespace and requires an operator or admin role. Use `artc_kubernetes_admin` only for a cluster-wide task the user explicitly requested, inspect its default preview, then repeat with `apply=true`. The admin tool still forbids Secret access, credential export, pod exec/debug/attach, file copy, impersonation, port forwarding and proxy commands.

If the tool reports that an access grant is unavailable, do not ask for credential material and do not fall back to local SSH or kubeconfig. Report the missing AmongClusters grant or agent approval by name.
