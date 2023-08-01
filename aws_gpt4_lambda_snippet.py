import boto3
import base64
from botocore.exceptions import BotoCoreError, ClientError

def get_secret(secret_name, region_name):
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        raise Exception("Couldn't retrieve the secret") from e
    else:
        if 'SecretString' in get_secret_value_response:
            return get_secret_value_response['SecretString']
        else:
            return base64.b64decode(get_secret_value_response['SecretBinary'])

def lambda_handler(event, context):
    secret = get_secret('MyAPIKey', 'us-west-2')
    print(f"API Key: {secret}")
    # Now use the secret (API Key) to make your API request

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
