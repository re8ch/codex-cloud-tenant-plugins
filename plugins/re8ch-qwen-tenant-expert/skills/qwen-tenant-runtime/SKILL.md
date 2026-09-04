---
name: qwen-tenant-runtime
description: Run digest-pinned OCI images and tenant database instances using Qwen-scoped RE8CH capacity.
---

# Qwen Tenant Runtime

This is a compatibility package. Use only the `re8ch-qwen-tenant` MCP server.
The authenticated identity fixes the tenant to `qwen`; never accept another
tenant id from a prompt. Prefer the generic service lifecycle and opaque
`accessRef` operations exposed by the tenant proxy.

1. Call capability discovery before a new workload or database request.
2. Plan first and show requested CPU, memory, storage, placement class, quota,
   expected expiry, and whether approval is required.
3. Create only after the user explicitly requests the run or provision action.
   Reuse the plan hash and idempotency key.
4. Container runs use immutable OCI digests. The provider may pull and unpack
   them with containerd or schedule them through Kubernetes; do not require a
   serverless wrapper.
5. Database runs are tenant-isolated instances with explicit storage, backup,
   TTL or retention class. Return an opaque connection reference, never a
   password, token, Secret value, node address, or provider credential.
6. Qwen owns its PublicEdge configuration and `ynzs.com` publication. A RE8CH
   workload may return an origin/service reference; do not mutate DNS, choose
   PublicEdge candidates, or claim domain authority.
7. Registry, database and observability rights are separate Consumable grants;
   this package must not infer one grant from another.
8. Do not call generic kubectl, SSH, containerd, Cilium, Ceph, Pigsty, or node
   tools. Use tenant operations so quota, isolation, audit, and cleanup apply.
9. For status, logs, artifacts, stop, or release, operate only on references
   returned for the authenticated Qwen tenant.
