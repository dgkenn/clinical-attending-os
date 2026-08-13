"""Tests for HTTP transport layer: config fields, build_server(), build_http_app(), and main() HTTP mode."""
import importlib


def test_settings_expose_mcp_http_fields(monkeypatch):
    monkeypatch.setenv("MCP_TRANSPORT", "streamable-http")
    monkeypatch.setenv("MCP_HOST", "127.0.0.1")
    monkeypatch.setenv("MCP_PORT", "9001")
    monkeypatch.setenv("MCP_AUTH_TOKEN", "secret123")
    import src.config as cfg
    importlib.reload(cfg)
    s = cfg.Settings()
    assert s.mcp_transport == "streamable-http"
    assert s.mcp_host == "127.0.0.1"
    assert s.mcp_port == 9001
    assert s.mcp_auth_token == "secret123"


def test_build_server_registers_tools():
    from src.mcp_server import build_server
    mcp = build_server()
    names = set(mcp._tool_manager._tools.keys())
    assert {"get_next_topic", "submit_answer", "search_clinical_sources"} <= names


def test_http_app_auth_and_health():
    from starlette.testclient import TestClient
    from src.mcp_server import build_server, build_http_app
    app = build_http_app(build_server(), auth_token="secret123")
    # raise_server_exceptions=False so MCP's runtime "task group not initialized"
    # error doesn't abort the test — we only care about the auth layer (401 vs not-401).
    client = TestClient(app, raise_server_exceptions=False)
    assert client.get("/health").status_code == 200
    assert client.post("/mcp").status_code == 401
    assert client.post("/mcp", headers={"Authorization": "Bearer nope"}).status_code == 401
    r = client.post("/mcp", headers={"Authorization": "Bearer secret123"})
    assert r.status_code != 401


def test_main_http_mode_builds_app(monkeypatch):
    import src.mcp_server as srv
    captured = {}
    monkeypatch.setenv("MCP_TRANSPORT", "streamable-http")
    monkeypatch.setenv("MCP_HOST", "127.0.0.1")
    monkeypatch.setenv("MCP_PORT", "9123")
    monkeypatch.setenv("MCP_AUTH_TOKEN", "secret123")
    monkeypatch.setattr(srv, "_serve_http", lambda app, host, port: captured.update(host=host, port=port))
    srv.main()
    assert captured == {"host": "127.0.0.1", "port": 9123}
