import os
import json
# import requests
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig

def lambda_handler(event, context):
    # Instantiate secret cache with specific configuration
    secret_cache = SecretCache(SecretCacheConfig())

    # Get the secrets from the cache
    secret_object = secret_cache.get_secret_string('test_secret')

    # Secrets are returned as a JSON string, so load it as a Python object
    secrets = json.loads(secret_object)

    # # Use the secrets to authenticate an HTTP request
    # response = requests.get(
    #     'http://example.com',
    #     auth=(secrets['username'], secrets['password'])
    # )

    return {
        'statusCode': 200,
        'body': secret_object,
    }

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
    }
