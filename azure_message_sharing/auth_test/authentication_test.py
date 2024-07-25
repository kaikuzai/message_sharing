import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

default_credential = DefaultAzureCredential()
account_url = "https://messagesharingstorage.blob.core.windows.net/"


blob_service_client = BlobServiceClient(
        account_url=account_url,
        credential=default_credential)

print(os.curdir)

# creating a container
container_name = str(uuid.uuid1())
container_client = blob_service_client.create_container(container_name)



