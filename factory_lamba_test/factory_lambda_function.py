import json


def lambda_handler(event, context):
    print('Hello, factory lambda')
    return {
        'statusCode': 200,
        'body': json.dumps('Factory lambda test')
    }
