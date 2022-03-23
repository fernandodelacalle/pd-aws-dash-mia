from fastapi.testclient import TestClient
from app import app


test_client = TestClient(app)


def test_suma():
    params = {'a': 1, 'b': 2}
    response = test_client.get('/suma', params=params)
    assert response.status_code == 200
    assert response.json() == 3


def test_resta():
    params = {'a': 2, 'b': 2}
    response = test_client.get('/resta', params=params)
    assert response.status_code == 200
    assert response.json() == 0
