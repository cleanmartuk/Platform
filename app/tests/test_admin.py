from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)

def test_read_admin():
    response = client.post("/admin/?token=jessica", headers={"X-Token": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {
        "message": "Admin getting schwifty"
    }
