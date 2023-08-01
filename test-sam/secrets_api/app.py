import os

import json
import requests
# from aws_secretsmanager_caching import SecretCache, SecretCacheConfigs

def lambda_handler(event, context):
    # # Instantiate secret cache with specific configuration
    # secret_cache = SecretCache(SecretCacheConfig())

    # # Get the secrets from the cache
    # secret_object = secret_cache.get_secret_string('test_secret')

    # # Secrets are returned as a JSON string, so load it as a Python object
    # secrets = json.loads(secret_object)
    secret_name = event['pathParameters']['secret_name']
    # # Use the secrets to authenticate an HTTP request
    # response = requests.get(
    #     'http://example.com',
    #     auth=(secrets['username'], secrets['password'])
    # )
    headers = {"X-Aws-Parameters-Secrets-Token": os.environ.get('AWS_SESSION_TOKEN')}
    secrets_extension_endpoint = "http://localhost:" + \
    "2773" + \
    "/secretsmanager/get?secretId=" + \
    secret_name
  
    r = requests.get(secrets_extension_endpoint, headers=headers)
  
    secret = json.loads(r.text)["SecretString"] # load the Secrets Manager response into a Python dictionary, access the secret

    return {
        'statusCode': 200,
        'body': secret
    }