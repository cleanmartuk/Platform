import time, uuid, logging
from typing import List, Optional
from pydantic import BaseModel
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable
from py2neo import Graph
import os
from dotenv import load_dotenv
load_dotenv()

graph = Graph("bolt://localhost:7687")


class Client(BaseModel):
    id : str
    status : bool
    name : str
    houseNumber : int
    location : str
    password : str
    JobSheet: List[ str ] = []
    class Config:
        '''Docstring here.'''
        schema_extra = {
            "example": {
                "id": "7f644301-e3f1-4752-90d5-99fbfad91ab3",
                "status" : True,
                "name" : 'John Doe',
                "houseNumber" : 23,
                "location" : "DT1 1SS",
                "password" : "Secret_Pa55w0rd",
                "JobSheet": ["79dc3d3a-c40b-47e8-8cf4-207c2de7e36","c85a5633-2803-4826-ae5a-82474c238d5","0348ae36-202a-4bfc-a92d-849607fd541" ],
            }
        }

external_data = {
    "id": "7f644301-e3f1-4752-90d5-99fbfad91ab4",
    "status": True,
    "name" : 'John Doe',
    "houseNumber" : 23,
    "location" : "DT1 1SS",
    "password" : "Secret_Pa55w0rd",
    "signup_ts": None,
    "JobSheet": ["79dc3d3a-c40b-47e8-8cf4-207c2de7e36","c85a5633-2803-4826-ae5a-82474c238d5","0348ae36-202a-4bfc-a92d-849607fd541" ]
}

faked_data = [{
    "7f644301-e3f1-4752-90d5-99fbfad91ab4":{
    "id": "7f644301-e3f1-4752-90d5-99fbfad91ab4",
    "status": True,
    "name" : 'John Doe',
    "houseNumber" : 23,
    "location" : "DT1 1SS",
    "password" : "Secret_Pa55w0rd",
    "signup_ts": None,
    "JobSheet": ["79dc3d3a-c40b-47e8-8cf4-207c2de7e36","c85a5633-2803-4826-ae5a-82474c238d5","0348ae36-202a-4bfc-a92d-849607fd541" ]
}
}]


def register_client(client):
    print(f"Start registration for register_client : {client}")
    query = """
    WITH $json as data
    UNWIND data as q

    MERGE (client:CLIENT {id:q.id}) ON CREATE
    SET client.name = q.name, client.status = q.status, client.houseNumber = q.houseNumber, 
    client.location = q.location, client.JobSheet = q.JobSheet, client.password = q.password, 
    client.signup_ts = q.signup_ts, client.joined = q.joined, client.status = q.status
    """

    print(f"Start graph execution for client {client}")
    graph.run(query,json=client)
    print(f"Complete graph execution for client {client}")
    return {"success":"client created successfully"}

# register_client(external_data)


def get_client(ref):
    '''To retrieve the profile of a client by id.'''
    print(f"Start retrieval of CLIENT: {ref}")
    query = """
    match (client:CLIENT) where client.id = $ref return client as clt
    """

    print(f"Start graph execution for retrieving client {ref}")
    result = graph.run(query,ref=ref)
    print(f"Complete graph execution for client {ref}")
    # elem = result.single()
    # print(f"result: Name = {elem['clt']['name']},\n ID = {elem['clt']['id']}")

client = get_client("7f644301-e3f1-4752-90d5-99fbfad91ab4")


def created_client( client_profile):
    ''' To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
        The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/
    '''
    print(f"Start graph execution for created_client")
    with auraDriver.session() as session:
            # Write transactions allow the driver to handle retries and transient errors
            result = session.write_transaction(_create_and_return_client, client_profile)
            for row in result:
                print(f"Created client" )
    return {"success" : "created_client"}

@staticmethod
def _create_and_return_client(tx, client_profile):
    # To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
    # The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/
    print(f"Start graph execution for _create_and_return_client")
    query = """
    WITH $client_profile as data
    UNWIND data as q

    MERGE (client:CLIENT {id:q.id}) ON CREATE
    SET client.name = q.name, client.status = q.status, client.houseNumber = q.houseNumber, 
    client.location = q.location, client.JobSheet = q.JobSheet, client.password = q.password, 
    client.signup_ts = q.signup_ts, client.joined = q.joined, client.status = q.status
    """
    result = tx.run(query, client_profile=client_profile)
    try:
        return [{"p1": row["p1"]["name"], "p2": row["p2"]["name"]}
                for row in result]
    # Capture any errors along with the query and data for traceability
    except ServiceUnavailable as exception:
        logging.error("{query} raised an error: \n {exception}".format(
            query=query, exception=exception))
        raise




def create_client(applicant):
    now = time.time()
    id = str(uuid.uuid4())
    print(f" ID = {id}")
    client = {}
    client["id"] = id
    client["status"]= True
    client["name"]= applicant["name"]
    client["houseNumber"]= applicant["houseNumber"]
    client["location"]= applicant["location"]
    client["password"]= applicant["password"]
    client["signup_ts"]= now
    client["joined"]= time.ctime(now)
    client["JobSheet"]=[]
    
    # print(f"Triggering created_client")
    # created_client(client)
    # print(f"Triggered created_client")
    print(f"Triggering register_client")
    register_client(client)
    print(f"Triggered register_client")
    faked_data.append({id: client})
    return faked_data

# create_client(external_data)


def retrive_client(ref=0):
    ref = '7f644301-e3f1-4752-90d5-99fbfad91ab4'
    print("Triggered retrive_client")
    reqst = faked_data
    for clnt in reqst:
        print(f"clnt = {clnt[ref]}")
        if clnt[ref] != {}:
            return clnt[ref]
        else:
            return f"{ref} was notfound"
            
            
#  ##
#  ## AURA GDB ACTIONS
#  ##           
# gdbUri = os.getenv('neo4j_gdbUri')
# gdbUser = os.getenv('neo4j_gdbUser')
# gdbPword = os.getenv('neo4j_gdbPword')

# print (f"gdbUri = {gdbUri}, gdbUser = {gdbUser}, gdbPword = {gdbPword}")
# auraDriver = GraphDatabase.driver(gdbUri, auth=(gdbUser, gdbPword))          
            
# def create_client_profile(self, client_info):
#     with self.auraDriver.session() as session:
#         # Write transactions allow the driver to handle retries and transient errors
#         result = session.write_transaction(
#             self._create_and_return_client_profile, client_info)
#         for row in result:
#             print("Created client_profile: {p1}".format(p1=row['p1']))

# @staticmethod
# def _create_and_returnclient_info(tx, client_info):
#     # To learn more about the Cypher syntax, see https://neo4j.com/docs/cypher-manual/current/
#     # The Reference Card is also a good resource for keywords https://neo4j.com/docs/cypher-refcard/current/
#     query = (
#         "CREATE (p1:CLIENT) set p1 += $person_ref "
#         "RETURN p1"
#     )
#     result = tx.run(query, person_ref=client_info)
#     try:
#         return [{"p1": row["p1"]["name"], "p2": row["p2"]["name"]} for row in result]
#     # Capture any errors along with the query and data for traceability
#     except ServiceUnavailable as exception:
#         logging.error("{query} raised an error: \n {exception}".format(
#             query=query, exception=exception))
#         raise

# def find_client_profile(self, person_name):
#     with self.auraDriver.session() as session:
#         result = session.read_transaction(self._find_and_return_client_profile, client_id)
#         for row in result:
#             print("Found person: {row}".format(row=row))

# @staticmethod
# def _find_and_return_client_profile(tx, client_id):
#     query = (
#         "MATCH (p:CLIENT) "
#         "WHERE p.name = $client_ref "
#         "RETURN p.name AS name"
#     )
#     result = tx.run(query, client_ref=client_id)
#     return [row["name"] for row in result]
        