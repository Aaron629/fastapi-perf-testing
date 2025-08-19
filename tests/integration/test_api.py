import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.integration
def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

@pytest.mark.integration
def test_add_api():
    r = client.get("/add", params={"a": 10, "b": 5})
    assert r.status_code == 200
    assert r.json()["result"] == 15
