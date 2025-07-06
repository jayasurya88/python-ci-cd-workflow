import pytest
from app import app

@pytest.fixture
def client():
    with app.TestClient() as client:
        yield client



def test _app_is_working(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello,World!" in response.data

