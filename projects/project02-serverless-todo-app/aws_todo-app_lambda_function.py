import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Todos')  # Replace with your actual DynamoDB table name

def lambda_handler(event, context):
    method = event['httpMethod']
    
    if method == 'OPTIONS':
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE',
                'Access-Control-Allow-Headers': 'Content-Type'
            },
            'body': json.dumps('CORS preflight')
        }

    if method == 'GET':
        response = table.scan()
        tasks = response.get('Items', [])
        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps(tasks)
        }

    body = json.loads(event.get('body', '{}'))

    if method == 'POST':
        task_id = body.get('taskId')
        description = body.get('description')
        status = body.get('status', 'Pending')

        if not task_id or not description:
            return {
                'statusCode': 400,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': 'Missing taskId or description'})
            }

        table.put_item(Item={
            'taskId': task_id,
            'description': description,
            'status': status
        })

        return {
            'statusCode': 201,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'message': 'Task added successfully'})
        }

    elif method == 'PUT':
        task_id = body.get('taskId')
        description = body.get('description')
        status = body.get('status', 'Pending')

        if not task_id:
            return {
                'statusCode': 400,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': 'Missing taskId'})
            }

        update_expression = "SET "
        expression_attributes = {}
        expression_attribute_names = {}

        if description:
            update_expression += "#desc = :d, "
            expression_attributes[":d"] = description
            expression_attribute_names["#desc"] = "description"

        if status:
            update_expression += "#stat = :s, "
            expression_attributes[":s"] = status
            expression_attribute_names["#stat"] = "status"

        update_expression = update_expression.rstrip(', ')

        table.update_item(
            Key={'taskId': task_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attributes,
            ExpressionAttributeNames=expression_attribute_names  # 👈 added this
        )

        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'message': 'Task updated successfully'})
        }


    elif method == 'DELETE':
        task_id = body.get('taskId')

        if not task_id:
            return {
                'statusCode': 400,
                'headers': {'Access-Control-Allow-Origin': '*'},
                'body': json.dumps({'error': 'Missing taskId'})
            }

        table.delete_item(Key={'taskId': task_id})

        return {
            'statusCode': 200,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'message': 'Task deleted successfully'})
        }

    else:
        return {
            'statusCode': 405,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': 'Method Not Allowed'})
        }
