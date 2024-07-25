import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

appended_list = []

default_credential = DefaultAzureCredential()
account_url = "https://messagesharingstorage.blob.core.windows.net/"
container_name = "messages"

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