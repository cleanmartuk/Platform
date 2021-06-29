from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def test_routes_read_item():
    response = client.get("/items/?token=jessica", headers={"X-Token": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {
  "plumbus": {
    "name": "Plumbus"
  },
  "gun": {
    "name": "Portal Gun"
  }
}

def test_routes_read_user():
    response = client.get("users/?token=jessica")
    assert response.status_code == 200
    assert response.json() == [
  {
    "username": "Rick"
  },
  {
    "username": "Morty"
  }
]