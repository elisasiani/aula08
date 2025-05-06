from http import HTTPStatus
from fastapi.testclient import TestClient  # type: ignore
from app import app
import pytest

@pytest.fixture()
def client():
    return TestClient(app)

def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user():
    client = TestClient(app)
    response = client.post(
        '/users/',
        json={
            'username': 'ana',
            'email': 'ana@exemplo.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'ana',
        'email': 'ana@exemplo.com',
        'id': 1,
    }
