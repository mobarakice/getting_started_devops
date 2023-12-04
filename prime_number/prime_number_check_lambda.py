import json
from utility.utility import Utility

util = Utility()


def lambda_handler(event, context):
    number = event['number']
    prime = util.is_prime(number)

    msg = ""
    if prime:
        msg = f"{number} is a prime number."
    else:
        msg = f"{number} is not a prime number."

    return {
        'statusCode': 200,
        'body': json.dumps(msg)
    }
