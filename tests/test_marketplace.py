import json
from pathlib import Path


ROOT = Path(__file__).parents[1]
MARKETPLACE = ROOT / ".agents/plugins/marketplace.json"
GENERIC = {
    "re8ch-tenant-registry": "tenant-registry",
    "re8ch-tenant-observability": "tenant-observability",
    "re8ch-tenant-byoc": "tenant-byoc",
}
ENDPOINTS = {
    "re8ch-tenant-registry": ("registry", "re8ch-tenant-registry"),
    "re8ch-tenant-observability": ("observability", "re8ch-tenant-observability"),
    "re8ch-tenant-byoc": ("byoc", "re8ch-tenant-byoc"),
}


def read_json(path: Path):
    return json.loads(path.read_text())


def test_marketplace_contains_separate_tenant_purposes():
    marketplace = read_json(MARKETPLACE)
    assert marketplace["name"] == "re8ch-cloud-tenant"
    names = [entry["name"] for entry in marketplace["plugins"]]
    assert len(names) == len(set(names))
    assert set(GENERIC) <= set(names)
    policies = {entry["name"]: entry["policy"] for entry in marketplace["plugins"]}
    assert policies["re8ch-tenant-core"]["installation"] == "NOT_AVAILABLE"
    assert policies["re8ch-tenant-database"]["installation"] == "NOT_AVAILABLE"
    assert all(policies[name] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"} for name in GENERIC)


def test_generic_plugins_share_proxy_but_have_distinct_skill_contracts():
    skill_texts = {}
    for plugin_name, skill_name in GENERIC.items():
        plugin = ROOT / "plugins" / plugin_name
        manifest = read_json(plugin / ".codex-plugin/plugin.json")
        mcp = read_json(plugin / ".mcp.json")
        server = next(iter(mcp["mcpServers"].values()))
        assert manifest["name"] == plugin_name
        endpoint, client = ENDPOINTS[plugin_name]
        assert server["url"] == f"https://tools.re8ch.com/tenant/{endpoint}/mcp"
        assert server["oauth"]["clientId"] == client
        assert "groups" in server["scopes"]
        skill_texts[plugin_name] = (plugin / "skills" / skill_name / "SKILL.md").read_text()
    assert "registry.harbor.v1" in skill_texts["re8ch-tenant-registry"]
    assert "observability.grafana.v1" in skill_texts["re8ch-tenant-observability"]
    assert "kubeconfig" in skill_texts["re8ch-tenant-byoc"]


def test_plugins_never_embed_credential_material():
    forbidden = ('"password"', '"token"', '"secret"', '"apiKey"', '"clientSecret"')
    for path in (ROOT / "plugins").rglob("*"):
        if path.is_file():
            text = path.read_text()
            assert not any(value in text for value in forbidden), path
