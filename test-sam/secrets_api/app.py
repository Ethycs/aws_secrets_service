import boto3
import json
import base64
import logging
from botocore.exceptions import BotoCoreError, ClientError

import sys
def is_module_imported(name):
    return name in sys.modules


logger = logging.getLogger()
logger.setLevel(logging.INFO)
 

def lambda_handler(event, context):
    # print("Starting lambda")
    # def get_secret(secret_name, region_name):
    #     print(f"Getting secret: {secret_name}")
    #     print(is_module_imported('boto3'))
    #     session = boto3.session.Session()
    #     client = session.client(
    #         service_name='secretsmanager',
    #         region_name=region_name
    #     )
    #     logger.info(f"Getting secret logger: {secret_name}")
    #     try:
    #         get_secret_value_response = client.get_secret_value(
    #             SecretId=secret_name
    #         )
    #     except ClientError as e:
    #         print("Error getting secret: ", e.response['Error']['Code'])
    #         raise Exception("Couldn't retrieve the secret") from e
    #     else:
    #         print("Got secret")
    #         if 'SecretString' in get_secret_value_response:
    #             return get_secret_value_response['SecretString']
    #         else:
    #             return base64.b64decode(get_secret_value_response['SecretBinary'])

    # secret = get_secret('test_secret', 'us-east-2')
    # print(f"API Key: {secret}")
    # # Now use the secret (API Key) to make your API request


    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
    }
