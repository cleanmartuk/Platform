#!/usr/bin/env python3
"""Customer Data Management."""

import time, uuid
from typing import List, Optional
from pydantic import BaseModel
import json
from py2neo import Graph


graph = Graph("bolt://localhost:7687")


class Customer(BaseModel):
    id: str
    status : bool
    title : str
    CompanyReg : int
    RegisteredAddress : str
    password : str
    signup_ts: float
    AreasCovered: List[ str ] = []
    WorkingDays: List[ str ] = []
    services: List[ str ] = []
    class Config:
        '''Docstring here.'''
        schema_extra = {
            "example": {
                "id": "9g644301-e3f1-4752-90d5-99fbfad99xy4",
                "status" : True,
                "title" : 'Any Clean',
                "CompanyReg" : 7999999,
                "RegisteredAddress" : "1 Main Street, Anytown, Anycounty, Anyland, XX9 9XX",
                "password" : "Secret_Pa55w0rd",
                "signup_ts": None,
                "AreasCovered":["DT1", "DT2"],
                "WorkingDays":[1,2,3,4,5,6],
                "services": [1,3,4],
            }}


external_data = {
                "id": "7f644301-e3f1-4752-90d5-99fbfad91ab4",
                "status" : True,
                "title" : 'Any Clean',
                "CompanyReg" : 7999999,
                "RegisteredAddress" : "1 Main Street, Anytown, Anycounty, Anyland, XX9 9XX",
                "password" : "Secret_Pa55w0rd",
                "signup_ts": None,
                "AreasCovered":["DT1", "DT2"],
                "WorkingDays":[1,2,3,4,5,6],
                "services": [1,3,4]
                }

faked_data = [
              {"7f644301-e3f1-4752-90d5-99fbfad91ab4":{
                "id": "7f644301-e3f1-4752-90d5-99fbfad91ab4",
                "status" : True,
                "title" : 'Any Clean',
                "CompanyReg" : 7999999,
                "RegisteredAddress" : "1 Main Street, Anytown, Anycounty, Anyland, XX9 9XX",
                "password" : "Secret_Pa55w0rd",
                "signup_ts": None,
                "AreasCovered":["DT1", "DT2"],
                "WorkingDays":[1,2,3,4,5,6],
                "services": [1,3,4]
                }
               }
              ]


def register_customer(customer):
    print(f"Start registration for customer : {customer}")
    query = """
    WITH $json as data
    UNWIND data as q

    MERGE (customer:customer {id:q.id}) ON CREATE
    SET customer.name = q.name, customer.status = q.status, customer.houseNumber = q.houseNumber, 
    customer.location = q.location, customer.JobSheet = q.JobSheet, customer.password = q.password
    """

    print(f"Start graph execution for customer {customer}")
    graph.run(query,json=customer)
    print(f"Complete graph execution for customer {customer}")

register_customer(external_data)


def get_customer(ref):
    '''To retrieve the profile of a customer by id.'''
    print(f"Start retrieval of customer: {ref}")
    query = """
    match (customer:customer) where customer.id = $ref return customer as clt
    """

    print(f"Start graph execution for retrieving customer {ref}")
    result = graph.run(query,ref=ref)
    print(f"Complete graph execution for customer {ref}")
    # elem = result.single()
    # print(f"result: Name = {elem['clt']['name']},\n ID = {elem['clt']['id']}")

customer = get_customer("7f644301-e3f1-4752-90d5-99fbfad91ab4")



def create_customer(applicant):
    now = time.time() # Get timestamp of creation
    id = str(uuid.uuid4()) # Create unique Customer  ref
    customer = {}
    customer["id"] = id
    customer["status"]= True
    customer["title"]= applicant["title"]
    customer["CompanyReg"]= applicant["CompanyReg"]
    customer["RegisteredAddress"]= applicant["RegisteredAddress"]
    customer["password"]= applicant["password"]
    customer["signup_ts"]= now
    customer["joined"]= time.ctime(now)
    customer["AreasCovered"]=applicant["AreasCovered"],
    customer["WorkingDays"]=applicant["WorkingDays"],
    customer["services"]= applicant["services"]
    
    faked_data.append({id: customer})
    return faked_data