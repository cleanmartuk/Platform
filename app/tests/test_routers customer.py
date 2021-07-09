from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


# ************************************
# ******** Customer Tests ************
# ************************************

def test_routes_read_customers():
    response = client.get("/customers/?token=jessica", headers={"X-Token": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == { "9g644301-e3f1-4752-90d5-99fbfad99xy4": {
                "id": "9g644301-e3f1-4752-90d5-99fbfad99xy4",
                "status" : True,
                "title" : 'ServiceMaster',
                "CompanyReg" : 7999999,
                "RegisteredAddress" : "The Cleaning Centre, Groove Trading Estate, Dorchester DT1 1ST",
                "password" : "Secret_Pa55w0rd",
                "signup_ts": None,
                "AreasCovered":["DT1", "DT2", "DT3", "DT4", "DT5", "DT9", "DT10", "DT11"],
                "WorkingDays":[1,2,3,4,5,6],
                "services": [1,3,4],
            },
     "9g644301-e3f1-4752-90d5-99fbfad99dc9":{
                "id": "9g644301-e3f1-4752-90d5-99fbfad99dc9",
                "status" : True,
                "title" : 'Cloverclean',
                "CompanyReg" : 7888888,
                "RegisteredAddress" : "27 Oakwood, Broadmayne, Dorchester DT2 8UL",
                "password" : "Secret_Pa55w0rd",
                "signup_ts": None,
                "AreasCovered":["DT1", "DT2", "DT3", "DT4", "DT5", "DT6", "DT7", "DT8"],
                "WorkingDays":[1,2,3,4,5],
                "services": [1,2,5],
            }
     }

def test_routes_read_customers_err_token():
    response = client.get("/customers/?token=jess", headers={"X-Token": "fake-super-secret-token"})
    assert response.status_code == 400
    assert response.json() == {'detail': 'No Jessica token provided'}

def test_routes_read_customers_err_header():
    response = client.get("/customers/?token=jessica", headers={"X-Token": "fake-secret-token"})
    assert response.status_code == 400
    assert response.json() == {'detail': 'X-Token header invalid'}
   
 
    