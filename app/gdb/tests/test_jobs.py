import pytest

from ..data_models.job import create_job, retrive_job

valid_appl ={ "client_id":"Spanarchian", "houseNumber": "1", "location": "DT1 1SS", "service_req":[1], "required_date":"", "time":"", "budget":"15.00"}


def test_create_job():
    '''
    Testing the creation of a job
    '''
    expected = [{'4b886871-b3c5-4003-b8b2-528a76490c68': {'job_id': '4b886871-b3c5-4003-b8b2-528a76490c68', 'status': 'O', 'client_id': 'Spanarchian', 'houseNumber': '1', 'location': 'DT1 1SS', 'service_req': [1], 'created_ts': 1626729546.245023, 'created': 'Mon Jul 19 22:19:06 2021', 'required_date': '', 'time': '', 'budget': '15.00'}},
                {'4b886871-b3c5-4003-b8b2-528a76490c46': {'job_id': '4b886871-b3c5-4003-b8b2-528a76490c46', 'status': 'O', 'client_id': 'Spanarchian', 'houseNumber': '1', 'location': 'DT1 1SS', 'service_req': [1], 'created_ts': 1626729546.245023, 'created': 'Mon Jul 19 22:19:06 2021', 'required_date': '', 'time': '', 'budget': '15.00'}}]

    actual = create_job(valid_appl)
    new_job_id = list(actual[1].keys())[0]
    print(f"New job list : {actual}\n\n")
    print(f"New job added: {actual[1]}\n\n")
    print(f"New job id: {new_job_id}\n\n")
    
    assert len(actual) == len(expected), f"ERROR 'Length NOT AS EXPECTED!'  expected : {expected} \n but was returned {actual}"
    assert actual[0] == expected[0], f"ERROR 'NOT AS EXPECTED!'  expected : {expected} \n but was returned {actual}"
    assert actual[1][new_job_id]['client_id'] == "Spanarchian", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'Spanarchian'} \n but was returned {actual[1][new_job_id]['client_id']}"
    assert actual[1][new_job_id]['status'] == "O", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'O'} \n but was returned {actual[1][new_job_id]['status']}"



def test_retrive_job():
    '''
    Testing the retrival of a job
    '''
    expected = [{'4b886871-b3c5-4003-b8b2-528a76490c68': {'job_id': '4b886871-b3c5-4003-b8b2-528a76490c68', 'status': 'O', 'client_id': 'Spanarchian', 'houseNumber': '1', 'location': 'DT1 1SS', 'service_req': [1], 'created_ts': 1626729546.245023, 'created': 'Mon Jul 19 22:19:06 2021', 'required_date': '', 'time': '', 'budget': '15.00'}}]
    ref = '4b886871-b3c5-4003-b8b2-528a76490c68'
    actual = retrive_job(ref)
    print(f"actual = {actual}")
    
    # assert actual['name'] == "John Doe", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'John Doe'} \n but was returned {actual[1][ref]['name']}"
    # assert actual['password'] == "Secret_Pa55w0rd", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'Secret_Pa55w0rd'} \n but was returned {actual[1][ref]['password']}"
    assert actual['client_id'] == "Spanarchian", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'Spanarchian'} \n but was returned {actual['client_id']}"
    assert actual['status'] == "O", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'O'} \n but was returned {actual['status']}"
