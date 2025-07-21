# 🔥 Day 16 - DynamoDB Basics (21 July, 2025)
## 📂 Title: Perform CRUD Operations on DynamoDB via Lambda (Using Test Events)
### 🧭 Goal: Build serverless backend logic using Lambda to handle Create, Read, Update, and Delete operations on a DynamoDB table. Validate functionality using test events.

### ✅ What I Did Today

### Created DynamoDB Table via Console
- Table Name: `Tasks`
- Primary Key: `taskId` (String)
- Initial Item Inserted: Manually added one item for testing.
      {
        "taskId": "001",
        "description": "Initial task from console",
        "status": "incomplete"
      }

- Wrote Lambda Function (`lambda_function.py`)

      import json
      import boto3

      dynamodb = boto3.resource('dynamodb')
      table = dynamodb.Table('Tasks')

      def lambda_handler(event, context):
          print("RAW EVENT:", json.dumps(event))

          task = event.get("task")
          if not task:
              return {"error": "Missing 'task' in event", "event": event}

          print(f"TASK: {task}")

          try:
              if task == "create":
                  task_id = event.get("taskId")
                  description = event.get("description")
                  if not task_id or not description:
                      return {"error": "Missing 'taskId' or 'description' in create"}

                  table.put_item(Item={
                      "taskId": task_id,
                      "description": description,
                      "status": event.get("status", "incomplete")
                  })
                  print(f"Created item with taskId: {task_id}")
                  return {"message": "Item created"}

              elif task == "read":
                  task_id = event.get("taskId")
                  if not task_id:
                      return {"error": "Missing 'taskId' in read"}

                  response = table.get_item(Key={"taskId": task_id})
                  item = response.get("Item")
                  if not item:
                      return {"error": f"No item found with taskId: {task_id}"}
                  print(f"Read item: {item}")
                  return item

              elif task == "update":
                  task_id = event.get("taskId")
                  description = event.get("description")
                  status = event.get("status")
                  if not task_id or not description or not status:
                      return {"error": "Missing 'taskId', 'description', or 'status' in update"}

                  table.update_item(
                      Key={"taskId": task_id},
                      UpdateExpression="SET description = :desc, #s = :stat",
                      ExpressionAttributeNames={"#s": "status"},
                      ExpressionAttributeValues={":desc": description, ":stat": status}
                  )
                  print(f"Updated item with taskId: {task_id}")
                  return {"message": "Item updated"}

              elif task == "delete":
                  task_id = event.get("taskId")
                  if not task_id:
                      return {"error": "Missing 'taskId' in delete"}

                  table.delete_item(Key={"taskId": task_id})
                  print(f"Deleted item with taskId: {task_id}")
                  return {"message": "Item deleted"}

              else:
                  return {"error": f"Unknown task '{task}'", "event": event}

          except Exception as e:
              print(f"EXCEPTION: {str(e)}")
              return {"error": "Exception occurred", "details": str(e), "event": event}


- Handled all 4 operations: `create`, `read`, `update`, `delete`
- Used `if-elif` logic to route each operation
- Connected to `Tasks` table using `boto3`
- Implemented error handling and logging
- Tested Lambda via Console `Test Events`
- Created 4 different test events (one for each operation)
- Executed and validated the result for each event
- Deployed multiple versions (debugged syntax + stale code issues) #indentation error, reserved keyword error
- Fixed Issues by Re-deploying Clean Function
- Deleted and re-created the Lambda function when test events were not picked up correctly
- Confirmed clean runs after re-deployment

### 🧩 DynamoDB Table Schema
| Attribute   | Type   | Role                             |
| ----------- | ------ | -------------------------------- |
| taskId      | String | Primary Key                      |
| description | String | Task details                     |
| status      | String | e.g., "incomplete" or "complete" |

### 🧪 Test Event JSONs Used
#### ➕ Create [output](./screenshots/create_output.png)

    {
      "task": "create",
      "taskId": "002",
      "description": "Learn AWS Lambda",
      "status": "incomplete"
    }

#### ➕ Create2 [output](./screenshots/create2_output.png)

    {
      "task": "create",
      "taskId": "003",
      "description": "Create an extra item",
      "status": "incomplete"
    }
#### ➕ Create_without_taskid [output](./screenshots/create_without_tid_output.png)

    {
      "task": "create",
      "description": "test without taskId"
    }

#### 📖 Read [output](./screenshots/read_output.png)

    {
      "task": "read",
      "taskId": "001"
    }

#### 📝 Update [output](./screenshots/update_output.png)

    {
      "task": "update",
      "taskId": "003",
      "description": "Created an extra item",
      "status": "complete"
    }

#### ❌ Delete [output](./screenshots/delete_output.png)

    {
      "task": "delete",
      "taskId": "003"
    }

### 🛠️ Lambda Highlights
- Language: `Python 3.13`
- Library: `boto3`
- Handler: `lambda_function.lambda_handler`
- IAM Role with permissions for: `AmazonDynamoDBFullAccess` for now
- or can also use
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "dynamodb:GetItem",
        "dynamodb:UpdateItem",
        "dynamodb:DeleteItem"
     ],
     "Resource": "arn:aws:dynamodb:<region>:<account-id>:table/Tasks"
    }  
for least privileges


### 🧠 Learnings & Fixes
- 🚫 Problem: Lambda ran old code despite deploying new test event
- ✅ Fix: Deleted and recreated Lambda function
- 🧠 Lesson: AWS Lambda sometimes caches old code/config – recreate if needed
- 💡 Used logs and error messages to debug efficiently
- 🛡️ Added validation for required fields in JSON
- 🧾 Used reserved keyword workaround for status in DynamoDB updates 
