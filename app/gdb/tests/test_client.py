import pytest

from ..data_models.client import create_client, retrive_client

valid_appl ={"name":"Spanarchian", "houseNumber": "1", "location": "DT1 1SS", "password": "secretPassword"}


def test_create_client():
    '''
    Testing the creation of a client
    '''
    expected = [{'7f644301-e3f1-4752-90d5-99fbfad91ab4': {'id': '7f644301-e3f1-4752-90d5-99fbfad91ab4', 'status': True, 'name': 'John Doe', 'houseNumber': 23, 'location': 'DT1 1SS', 'password': 'Secret_Pa55w0rd', 'signup_ts': None, 'JobSheet': ['79dc3d3a-c40b-47e8-8cf4-207c2de7e36', 'c85a5633-2803-4826-ae5a-82474c238d5', '0348ae36-202a-4bfc-a92d-849607fd541']}}, {'92bf9e91-a652-45f2-b4d3-83b9a213b169': {'id': '92bf9e91-a652-45f2-b4d3-83b9a213b169', 'status': True, 'name': 'Spanarchian', 'houseNumber': '1', 'location': 'DT1 1SS', 'password': 'secretPassword', 'signup_ts': 1626364892.644924, 'joined': 'Thu Jul 15 17:01:32 2021', 'JobSheet': []}}]
    
    actual = create_client(valid_appl)
    new_client_id = list(actual[1].keys())[0]
    print(f"New client list : {actual}\n\n")
    print(f"New client added: {actual[1]}\n\n")
    print(f"New client id: {new_client_id}\n\n")
    
    assert len(actual) == len(expected), f"ERROR 'Length NOT AS EXPECTED!'  expected : {expected} \n but was returned {actual}"
    assert actual[0] == expected[0], f"ERROR 'NOT AS EXPECTED!'  expected : {expected} \n but was returned {actual}"
    assert actual[1][new_client_id]['name'] == "Spanarchian", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'Spanarchian'} \n but was returned {actual[1][new_client_id]['name']}"
    assert actual[1][new_client_id]['password'] == "secretPassword", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'secretPassword'} \n but was returned {actual[1][new_client_id]['password']}"



def test_retrive_client():
    '''
    Testing the retrival of a client
    '''
    expected = [{'7f644301-e3f1-4752-90d5-99fbfad91ab4': {'id': '7f644301-e3f1-4752-90d5-99fbfad91ab4', 'status': True, 'name': 'John Doe', 'houseNumber': 23, 'location': 'DT1 1SS', 'password': 'Secret_Pa55w0rd', 'signup_ts': None, 'JobSheet': ['79dc3d3a-c40b-47e8-8cf4-207c2de7e36', 'c85a5633-2803-4826-ae5a-82474c238d5', '0348ae36-202a-4bfc-a92d-849607fd541']}}, {'92bf9e91-a652-45f2-b4d3-83b9a213b169': {'id': '92bf9e91-a652-45f2-b4d3-83b9a213b169', 'status': True, 'name': 'Spanarchian', 'houseNumber': '1', 'location': 'DT1 1SS', 'password': 'secretPassword', 'signup_ts': 1626364892.644924, 'joined': 'Thu Jul 15 17:01:32 2021', 'JobSheet': []}}]
    ref = '7f644301-e3f1-4752-90d5-99fbfad91ab4'
    actual = retrive_client(ref)
    print(f"actual = {actual}")
    
    assert actual['name'] == "John Doe", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'John Doe'} \n but was returned {actual[1][ref]['name']}"
    assert actual['password'] == "Secret_Pa55w0rd", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'Secret_Pa55w0rd'} \n but was returned {actual[1][ref]['password']}"
