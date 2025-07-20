import json
def lambda_handler(event, context):
    for key, value in event.items():
        print(f"{key} = {value}")
    return {
        'statusCode': 200,
        'body': 'Event logged.'
    }