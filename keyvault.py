from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

import config as conf

def retrieveSecret(SecretName):
    # Azure Variables
    azClientID = conf.CLIENT_ID
    azClientSecret = conf.CLIENT_SECRET
    azTenantID = conf.TENANT_ID
    azKeyVaultName = conf.KEYVAULT_NAME
    azKVURI = conf.KEYVAULT_URI

    _credential = ClientSecretCredential(
        client_id = azClientID,
        client_secret = azClientSecret,
        tenant_id = azTenantID
    )

    _sc = SecretClient(vault_url=azKVURI, credential = _credential)

    print(f"Retrieving your Zoom password from {azKeyVaultName}.")

    retrieved_secret = _sc.get_secret(SecretName)

    secret = retrieved_secret.value

    return secret