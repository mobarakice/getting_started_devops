import json


def lambda_handler(event, context):
    print('Hello, api gateway')
    return {
        'statusCode': 200,
        'body': json.dumps('AWS API Gateway test')
    }
