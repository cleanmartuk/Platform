from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


# ************************************
# ******** Clients  Tests ************
# ************************************

def test_routes_read_clients():
    response = client.get("/clients/?token=jessica", headers={"X-Token": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {"7f644301-e3f1-4752-90d5-99fbfad91ab3": {
    "id": "7f644301-e3f1-4752-90d5-99fbfad91ab3",
    "status" : True,
    "name" : 'John Doe',
    "houseNumber" : 23,
    "location" : "DT1 1SS",
    "password" : "Secret_Pa55w0rd",
    "signup_ts": None,
    "JobSheet": ["79dc3d3a-c40b-47e8-8cf4-207c2de7e36","c85a5633-2803-4826-ae5a-82474c238d5","0348ae36-202a-4bfc-a92d-849607fd541" ]
}, "7f644301-e3f1-4752-90d5-99fbfad91ab4": {
    "id": "7f644301-e3f1-4752-90d5-99fbfad91ab4",
    "status" : True,
    "name" : 'Jane Doe',
    "houseNumber" : 33,
    "location" : "DT2 2SS",
    "password" : "Secret_Pa55w0rd",
    "signup_ts": None,
    "JobSheet": ["79dc3d3a-c40b-47e8-8cf4-207c2de7e24","c85a5633-2803-4826-ae5a-82474c238c4","0348ae36-202a-4bfc-a92d-849607fd520" ]
}}


def test_routes_read_clients_err_token():
    response = client.get("/clients/?token=jess", headers={"X-Token": "fake-super-secret-token"})
    assert response.status_code == 400
    assert response.json() == {'detail': 'No Jessica token provided'}

def test_routes_read_clients_err_header():
    response = client.get("/clients/?token=jessica", headers={"X-Token": "fake-secret-token"})
    assert response.status_code == 400
    assert response.json() == {'detail': 'X-Token header invalid'}
