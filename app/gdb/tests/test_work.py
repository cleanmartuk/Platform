import pytest

from ..data_models.work import create_work, retrive_work

# Expected json from the work exchange service
valid_appl ={"work_id":"work1", 'status': "O", "client_id":"Spanarchian", "houseNumber": "1", "location": "DT1 1SS", "service_req":[1], "required_date":"", "time":"", "budget":"15.00"}

@pytest.mark.skip("PENDING TEST")
def test_create_work():
    '''
    Testing the creation of a work
    '''
    expected = [{'7f644301-e3f1-4752-90d5-99fbfad91ab4': {'work_id': '7f644301-e3f1-4752-90d5-99fbfad91ab4', 'status': "O", 'client_id': '', 'houseNumber': 23, 'location': 'DT2 1SS', 'service_req': [1,3], 'signup_ts': None, "required_date":"", "time":"", "budget":"15.00"}}]
    
    actual = create_work(valid_appl)
    new_work_id = list(actual[1].keys())[0]
    print(f"New work list : {actual}\n\n")
    print(f"New work added: {actual[1]}\n\n")
    print(f"New work id: {new_work_id}\n\n")
    
    assert len(actual) == len(expected), f"ERROR 'Length NOT AS EXPECTED!'  expected : {expected} \n but was returned {actual}"
    assert actual[0] == expected[0], f"ERROR 'NOT AS EXPECTED!'  expected : {expected} \n but was returned {actual}"
    assert actual[1][new_work_id]['name'] == "Spanarchian", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'Spanarchian'} \n but was returned {actual[1][new_work_id]['name']}"
    assert actual[1][new_work_id]['password'] == "secretPassword", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'secretPassword'} \n but was returned {actual[1][new_work_id]['password']}"


@pytest.mark.skip("PENDING TEST")
def test_retrive_work():
    '''
    Testing the retrival of a work
    '''
    expected = [{'7f644301-e3f1-4752-90d5-99fbfad91ab4': {'id': '7f644301-e3f1-4752-90d5-99fbfad91ab4', 'status': True, 'name': 'John Doe', 'houseNumber': 23, 'location': 'DT1 1SS', 'password': 'Secret_Pa55w0rd', 'signup_ts': None, 'workSheet': ['79dc3d3a-c40b-47e8-8cf4-207c2de7e36', 'c85a5633-2803-4826-ae5a-82474c238d5', '0348ae36-202a-4bfc-a92d-849607fd541']}}, {'92bf9e91-a652-45f2-b4d3-83b9a213b169': {'id': '92bf9e91-a652-45f2-b4d3-83b9a213b169', 'status': True, 'name': 'Spanarchian', 'houseNumber': '1', 'location': 'DT1 1SS', 'password': 'secretPassword', 'signup_ts': 1626364892.644924, 'joined': 'Thu Jul 15 17:01:32 2021', 'workSheet': []}}]
    ref = '7f644301-e3f1-4752-90d5-99fbfad91ab4'
    actual = retrive_work(ref)
    print(f"actual = {actual}")
    
    assert actual['name'] == "John Doe", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'John Doe'} \n but was returned {actual[1][ref]['name']}"
    assert actual['password'] == "Secret_Pa55w0rd", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'Secret_Pa55w0rd'} \n but was returned {actual[1][ref]['password']}"
