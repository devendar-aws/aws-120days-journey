# 📁 Week 03 - Lambda + DynamoDB + API Gateway

This week, I integrated core AWS services — Lambda, DynamoDB, and API Gateway — to build a full CRUD backend system. Here's a summary of all the commands and components involved each day.

---

## ✅ Day 15: Lambda Basics


### Create a new Lambda function from AWS Console (Python 3.13 runtime)
#### Create test event:
```
{
  "task": "lambda"
}
```
- Used lambda_handler(event, context)
- Printed sample messages
- Understood the role of event-driven code execution

---

## ✅ Day 16: DynamoDB Basics
### DynamoDB Table Creation  
Table Name: Tasks
Partition Key: taskId (String)

#### Sample Item (PutItem in Test):
```
{
  "task": "create",
  "taskId": "001",
  "description": "Complete project",
  "status": "pending"
}
```
- Explored boto3 usage: import boto3, table.put_item(), table.get_item()
- Handled ResourceNotFoundException when region mismatch occurred

---

## ✅ Day 17: API Gateway Link
# Created API Gateway
- Resource: /tasks
- Methods: GET, POST, PUT, DELETE
- Integration type: Lambda Function

# Sample Test using cURL
```
curl -X POST https://your-api-id.execute-api.region.amazonaws.com/dev/tasks \
  -H "Content-Type: application/json" \
  -d '{"task": "create", "taskId": "003", "description": "Try Lambda", "status": "pending"}'
```
- Learned how HTTP methods trigger specific logic in lambda
- Enabled CORS to avoid frontend errors

---

## ✅ Day 18 & 19: Lambda Project - CRUD on TODOList
### Used Python Dictionary-based routing logic:
```
http_method = event['httpMethod']
if http_method == 'POST':
    # Create logic
elif http_method == 'GET':
    # Read logic
elif http_method == 'PUT':
    # Update logic
elif http_method == 'DELETE':
    # Delete logic
```
#### POST, GET, PUT, DELETE now working fully!
- Full CRUD flow functional
- Used boto3.resource('dynamodb') and conditionally handled exceptions
- Payloads passed via cURL / browser

---

## ✅ Day 20: CloudWatch Logs
# Access logs:  
AWS Console > CloudWatch > Log Groups > /aws/lambda/your-function-name

# Print sample logs:
```
print("Function triggered")
print("Payload:", event)
```
- Verified execution trace and debug information
- Learned structure of Log Group > Log Stream > Log Events

---

















































