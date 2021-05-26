import os
import cmd
import azure.keyvault.secrets
import azure.identity
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

import secrets as sec

def retrieveSecret(SecretName):
    keyVaultName = os.environ[sec.AZURE_KEYVAULT_NAME]
    KVUri = f"https://{keyVaultName}.vault.azure.net"

    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KVUri, credential=credential)

    print(f"Retrieving your Zoom password from {keyVaultName}.")

    retrieved_secret = client.get_secret(SecretName)

    secret = retrieved_secret.value

    return secret