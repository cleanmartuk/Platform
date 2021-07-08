from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


# ************************************
# ********* Works Tests **************
# ************************************



def test_routes_read_item():
    response = client.get("/works/?token=jessica", headers={"X-Token": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {
  "plumbus": {
    "name": "Plumbus"
  },
  "gun": {
    "name": "Portal Gun"
  }
}
    
def test_routes_read_item_err_token():
    response = client.get("/works/?token=jesa", headers={"X-Token": "fake-super-secret-token"})
    assert response.status_code == 400
    assert response.json() == {'detail': 'No Jessica token provided'}
    
    
def test_routes_read_item_err_header():
    response = client.get("/works/?token=jessica", headers={"X-Token": "fake-secret-token"})
    assert response.status_code == 400
    assert response.json() == {'detail': 'X-Token header invalid'}

# ************************************
# ********** Jobs Tests **************
# ************************************


def test_routes_read_jobs():
    response = client.get("/jobs/?token=jessica", headers={"X-Token": "fake-super-secret-token"})
    assert response.status_code == 200
    assert response.json() == {"7f644301-e3f1-4752-90d5-99fbfad95uh8": {
                "id": "7f644301-e3f1-4752-90d5-99fbfad95uh8",
                "active" : True,
                "assigned" : False,
                "client_id" : 'client_guid',
                "date_required" : "01/01/22",
                "date_required" : "13:45",
                "assigned_to" : "",
                "assigned_on" : "",
                "worksheet" : "",
                },
               "":{
                "id": "7f644301-e3f1-4752-90d5-99fbfad99xx9",
                "active" : True,
                "assigned" : True,
                "client_id" : 'client_guid',
                "date_required" : "01/01/22",
                "date_required" : "13:45",
                "assigned_to" : "customer_guid",
                "assigned_on" : "10/10/21",
                "worksheet" : "7f644301-e3f1-4752-90d5-99fbabc12xx3",
               }}

def test_routes_read_jobs_err_token():
    response = client.get("jobs/?token=jess")
    assert response.status_code == 400
    assert response.json() == {'detail': 'No Jessica token provided'}
  

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
   
 
    