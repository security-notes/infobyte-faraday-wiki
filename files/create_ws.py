# -*- coding: utf-8 -*-
import click
from requests import Session

@click.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True)
@click.option('--server_address', prompt=True, help='Faraday server url', default='http://localhost:5985')
@click.option('--workspace_name', prompt=True)
def create_workspace(username, password, server_address, workspace_name):
    print('Authentication to server {0}'.format(server_address))
    session = Session()
    # authentication to faraday server
    session.post(server_address + '/_api/login', json={'email': 'faraday', 'password': 'Password123'})
    # create new workspace
    ws_payload = {
            "customer":"",
            "name":workspace_name,
            "type":"Workspace",
            "users":["faraday"],
            "public":False,
            "children":[],
            "duration":{"start_date":"","end_date":""},
            "scope":[],
            "description":""
            }

    res = session.post(server_address + '/_api/v2/ws/', json=ws_payload)
    assert res.status_code == 201
    print('Workspace {0} created'.format(workspace_name))


create_workspace()
