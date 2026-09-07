import json
from pathlib import Path


ROOT = Path(__file__).parents[1]
MARKETPLACE = ROOT / ".agents/plugins/marketplace.json"
PLUGIN = ROOT / "plugins/re8ch-tenant"


def read_json(path: Path):
    return json.loads(path.read_text())


def test_marketplace_exposes_exactly_one_generic_tenant_plugin():
    marketplace = read_json(MARKETPLACE)
    assert marketplace["name"] == "re8ch-cloud-tenant"
    assert marketplace["plugins"] == [
        {
            "name": "re8ch-tenant",
            "source": {"source": "local", "path": "./plugins/re8ch-tenant"},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": "Developer Tools",
        }
    ]


def test_tenant_plugin_uses_the_single_identity_scoped_endpoint():
    manifest = read_json(PLUGIN / ".codex-plugin/plugin.json")
    mcp = read_json(PLUGIN / ".mcp.json")
    assert manifest["name"] == "re8ch-tenant"
    assert manifest["version"] == "0.2.1"
    assert manifest["interface"]["displayName"] == "Re8ch Tenant"
    assert mcp == {
        "mcpServers": {
            "re8ch-tenant": {
                "type": "http",
                "url": "https://tools.re8ch.com/tenant/mcp",
                "oauth": {"clientId": "re8ch-tenant"},
                "scopes": ["openid", "profile", "email", "groups", "offline_access"],
            }
        }
    }


def test_domain_capabilities_are_skills_not_marketplace_plugins():
    skills = {path.parent.name for path in (PLUGIN / "skills").glob("*/SKILL.md")}
    assert skills == {
        "tenant-self-service",
        "tenant-registry",
        "tenant-database",
        "tenant-observability",
        "tenant-byoc",
    }
    plugin_dirs = {
        path.parent.parent.name for path in ROOT.glob("plugins/*/.codex-plugin/plugin.json")
    }
    assert plugin_dirs == {"re8ch-tenant"}


def test_shared_marketplace_contains_no_tenant_specific_identity():
    content = "\n".join(
        path.read_text()
        for root in (ROOT / "plugins", ROOT / ".agents", ROOT / "README.md")
        for path in ([root] if root.is_file() else root.rglob("*"))
        if path.is_file()
    ).lower()
    assert "qwen" not in content
    assert "artchais" not in content


def test_plugin_never_embeds_credential_material():
    forbidden = ('"password"', '"token"', '"secret"', '"apikey"', '"clientsecret"')
    for path in PLUGIN.rglob("*"):
        if path.is_file():
            text = path.read_text().lower()
            assert not any(value in text for value in forbidden), path
