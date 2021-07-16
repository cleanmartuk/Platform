import pytest
from ..data_models.customer import create_customer, retrive_customer

valid_appl ={
                "title" : 'Speck&Span',
                "CompanyReg" : '07879504',
                "RegisteredAddress" : "2 Side Street, Mosttown, Mostcounty, Mostland, DT9 9BC",
                "password" : "secretPassword",
                "AreasCovered":["DT10", "DT11"],
                "WorkingDays":[2,4,6],
                "services": [1,3]
            }

def test_create_customer():
    '''
    Testing the creation of a customer
    '''
    expected = [
        {'7f644301-e3f1-4752-90d5-99fbfad91ab4': {'id': '7f644301-e3f1-4752-90d5-99fbfad91ab4', 'status': True, 'title': 'Any Clean', 'CompanyReg': 7999999, 'RegisteredAddress': '1 Main Street, Anytown, Anycounty, Anyland, XX9 9XX', 'password': 'Secret_Pa55w0rd', 'signup_ts': None, 'AreasCovered': ['DT1', 'DT2'], 'WorkingDays': [1, 2, 3, 4, 5, 6], 'services': [1, 3, 4]}}, 
        {'2277d8f3-f016-4a35-953f-0253f188f8cc': {'id': '2277d8f3-f016-4a35-953f-0253f188f8cc', 'status': True, 'title': 'Speck&Span', 'CompanyReg': '07879504', 'RegisteredAddress': '2 Side Street, Mosttown, Mostcounty, Mostland, DT9 9BC', 'password': 'secretPassword', 'signup_ts': 1626371299.48408, 'joined': 'Thu Jul 15 18:48:19 2021', 'AreasCovered': (['DT10', 'DT11'],), 'WorkingDays': ([2, 4, 6],), 'services': [1, 3]}}]
    
    actual = create_customer(valid_appl)
    new_customer_id = list(actual[1].keys())[0]
    print(f"New customer list : {actual}\n\n")
    print(f"New customer added: {actual[1]}\n\n")
    print(f"New customer id: {new_customer_id}\n\n")
    
    assert len(actual) == len(expected), f"ERROR 'Length NOT AS EXPECTED!'  expected : {expected} \n but was returned {actual}"
    assert actual[0] == expected[0], f"ERROR 'NOT AS EXPECTED!'  expected : {expected} \nbut was returned {actual}"
    assert actual[1][new_customer_id]['title'] == "Speck&Span", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'Spanarchian'} \n but was returned {actual[1][new_customer_id]['name']}"
    assert actual[1][new_customer_id]['CompanyReg'] == "07879504", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'07879504'} \n but was returned {actual[1][new_customer_id]['CompanyReg']}"
    assert actual[1][new_customer_id]['password'] == "secretPassword", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'secretPassword'} \n but was returned {actual[1][new_customer_id]['password']}"



def test_retrive_customer():
    '''
    Testing the retrival of a customer
    '''
    expected = [
        {'7f644301-e3f1-4752-90d5-99fbfad91ab4': {'id': '7f644301-e3f1-4752-90d5-99fbfad91ab4', 'status': True, 'title': 'Any Clean', 'CompanyReg': 7999999, 'RegisteredAddress': '1 Main Street, Anytown, Anycounty, Anyland, XX9 9XX', 'password': 'Secret_Pa55w0rd', 'signup_ts': None, 'AreasCovered': ['DT1', 'DT2'], 'WorkingDays': [1, 2, 3, 4, 5, 6], 'services': [1, 3, 4]}}, 
        {'2277d8f3-f016-4a35-953f-0253f188f8cc': {'id': '2277d8f3-f016-4a35-953f-0253f188f8cc', 'status': True, 'title': 'Speck&Span', 'CompanyReg': '07879504', 'RegisteredAddress': '2 Side Street, Mosttown, Mostcounty, Mostland, DT9 9BC', 'password': 'secretPassword', 'signup_ts': 1626371299.48408, 'joined': 'Thu Jul 15 18:48:19 2021', 'AreasCovered': (['DT10', 'DT11'],), 'WorkingDays': ([2, 4, 6],), 'services': [1, 3]}}]
    
    ref = '7f644301-e3f1-4752-90d5-99fbfad91ab4'
    actual = retrive_customer(ref)
    print(f"actual = {actual}")
    
    assert actual['title'] == "Any Clean", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'John Doe'} \n but was returned {actual[1][ref]['name']}"
    assert actual['password'] == "Secret_Pa55w0rd", f"ERROR 'Name NOT AS EXPECTED!'  expected : {'Secret_Pa55w0rd'} \n but was returned {actual[1][ref]['password']}"
