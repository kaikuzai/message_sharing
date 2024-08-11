import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, ContainerClient
import datetime
import json
import logging

app = func.FunctionApp()
default_credential = DefaultAzureCredential()
account_url = "https://messagesharingstorage.blob.core.windows.net/"
container_name = "messages"

@app.route(route="HttpExample", auth_level=func.AuthLevel.ANONYMOUS)
def HttpExample(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
@app.route(route="welcome", auth_level=func.AuthLevel.ANONYMOUS)
def HttpWelcome(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python welcome Http trigger function handled a request')

    response = {
        "reply":"This is the welcome message"
    }

    return func.HttpResponse(
        json.dumps(response),
        mimetype="application/json",
        status_code=200
        )

@app.route(route="MessageCounter", auth_level=func.AuthLevel.ANONYMOUS)
def MessageCounter(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Message Counter endpoint was triggered')

    appended_list = []


    # create blob service client 
    blob_service_client = BlobServiceClient(
        account_url=account_url, 
        credential=default_credential
        )

    container_client = blob_service_client.get_container_client(
        container=container_name
        )

    container_list = container_client.list_blobs()

    for i in container_list:
        appended_list.append(i.name)

    list_size = len(appended_list)

    response = {
        "length":list_size
    }

    return func.HttpResponse(
        json.dumps(response),
        status_code=200, 
        mimetype="application/json"
    )

@app.route(route="MessageUploader", auth_level=func.AuthLevel.ANONYMOUS)
def MessageReader(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('MessageReader has been initialized')

    try:
        req_body = req.get_json()
        file_name = req_body.get('fileName')
        file_content = req_body.get('content')

        blob_client = BlobServiceClient(
            account_url=account_url,
            credential=default_credential
            )
        
        
        container_client = blob_client.get_container_client(
            container=container_name
        )

        container_client.upload_blob(
            name=file_name,
            data=file_content,
            overwrite=True 
            )
        


    except Exception as exception:
        logging.error(f'There was an error uploading the file: {exception}')