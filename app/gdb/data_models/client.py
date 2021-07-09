from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
import json
from py2neo import Graph


graph = Graph("bolt://localhost:7687")


class User(BaseModel):
    id: str
    name = 'John Doe'
    houseNumbber = int
    location = str
    password = str
    signup_ts: Optional[datetime] = None
    JobSheet: List[ str ] = []

external_data = {
    "id": "7f644301-e3f1-4752-90d5-99fbfad91ab4",
    "status": True,
    "name" : 'John Doe',
    "houseNumbber" : 23,
    "location" : "DT1 1SS",
    "password" : "Secret_Pa55w0rd",
    "signup_ts": None,
    "JobSheet": ["79dc3d3a-c40b-47e8-8cf4-207c2de7e36","c85a5633-2803-4826-ae5a-82474c238d5","0348ae36-202a-4bfc-a92d-849607fd541" ]
}

def magic_cypher():
    # # Add uniqueness constraints.
    # # graph.run("CREATE CONSTRAINT ON (q:Question) ASSERT q.id IS UNIQUE;")
    with open('data/mocks/CQC_data.json') as g:
        data = json.load(g)

    query = """
    WITH $json as data
    UNWIND data as q

    MERGE (location:CQCLocation {id:q.loc.locationId}) ON CREATE
    SET location.name = q.loc.name, location.web_link = q.loc.website, location.bed_count = q.loc.numberOfBeds, 
    location.registrationStatus = q.loc.registrationStatus, location.registrationDate = q.loc.registrationDate, location.deregistrationDate = q.loc.deregistrationDate, location.onspdLongitude = q.loc.onspdLongitude, location.onspdLatitude = q.loc.onspdLatitude

    MERGE (owner:PROVIDER {id:q.loc.providerId}) ON CREATE SET owner.postalAddressCounty = q.loc.postalAddressCounty
    MERGE (owner)-[:Provides]->(location)

    FOREACH (name IN q.loc.specialisms | MERGE (tag:specialism {name:name.name})  MERGE (location)-[:Specilises_In]->(tag)) 
    FOREACH (a IN q.loc.reports | MERGE (location)<-[:REPORTS]-(answer:REPORT {id:a.linkId}) ON CREATE SET answer.reportDate = a.reportDate, answer.reportUri= a.reportUri, answer.firstVisitDate = a.firstVisitDate)

    FOREACH (serviceType IN q.loc.gacServiceTypes | 
     MERGE (gacServiceType:gacServiceTypes {name:serviceType.name}) 
     MERGE (location)-[:Supplies_gacServiceType]->(gacServiceType) ) 

    """
    graph.run(query,json=data)

def register_client(client):
    print(f"Start registration for CLIENT : {client}")
    query = """
    WITH $json as data
    UNWIND data as q

    MERGE (client:CLIENT {id:q.id}) ON CREATE
    SET client.name = q.name, client.status = q.status, client.houseNumber = q.houseNumber, 
    client.location = q.location, client.JobSheet = q.JobSheet, client.password = q.password
    """
    
    print(f"Start graph execution for client {client}")
    graph.run(query,json=client)
    print(f"Complete graph execution for client {client}")
    
    
register_client(external_data)