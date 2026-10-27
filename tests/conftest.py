import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture
def empresa_criada(client):
    response = client.post(
        "/api/empresa",
        json={
            "nome_empresa": "Zezinho confecções S.A",
            "cnpj": "AAAAAAAAAAAA12",
        },
    )

    assert response.status_code == 201
    return response.json()
