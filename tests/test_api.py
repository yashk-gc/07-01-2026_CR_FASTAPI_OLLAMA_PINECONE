from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_store_endpoint_structure():
    response = client.post(
        "/store",
        json={"query": "Test cascade policy"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "status" in data
    assert "id" in data
    assert "dimension" in data
    assert data["status"] == "stored"
    assert isinstance(data["dimension"], int)


def test_search_endpoint_structure():
    response = client.post(
        "/search",
        json={"query": "cascade policy"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "query" in data
    assert "results" in data
    assert isinstance(data["results"], list)
