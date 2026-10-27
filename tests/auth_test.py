from fastapi.testclient import TestClient
from app.main import app
from tests.conftest import empresa_criada

# ------------------------- TESTES -------------------------

def test_register_user_happy_way(client, empresa_criada):

    data_create_user = {
        "email": "almeidafellipe237@gmail.com",
        "senha": "senhaForteUser123!",
        "nome": "Fellipe",
        "perfil": "admin",
        "empresa_id": empresa_criada["id"]
    }
    
    response = client.post("api/users/register", json=data_create_user)

    assert response.status_code == 201

def test_login_happy_way(client):

    data_login = {
        'email': 'almeidafellipe237@gmail.com',
        'senha': 'senhaForteUser123!'
    }
    
    response = client.post("api/auth/login", json=data_login)

    assert response.status_code == 200


