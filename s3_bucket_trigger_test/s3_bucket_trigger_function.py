import json


def lambda_handler(event, context):
    print('Hello, s3 trigger')
    return {
        'statusCode': 200,
        'body': json.dumps('S3 bucket trigger test')
    }
