# 🗓️ Day 17 – Full CRUD with Lambda, API Gateway & DynamoDB (22 July, 2025)

## 📌 Objective  
To build a fully working API that performs **Create, Read, Update, and Delete (CRUD)** operations on a DynamoDB table, powered by **AWS Lambda** and exposed via **API Gateway**, and tested via **cURL** CLI.

---

## 🔧 Tasks Completed

### ✅ 1. **Created DynamoDB Table**
- Table Name: `Todos`
- Partition Key: `taskId` (String)

### ✅ 2. **Created Lambda Function**
- Function Name: `TodoLambdaAPI`
- Written in Python
````bash
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Todos')

def lambda_handler(event, context):
    print("RAW EVENT:", json.dumps(event))

    # 🌐 Parse API Gateway body (if present)
    if "body" in event:
        try:
            body = json.loads(event["body"])
        except Exception as e:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Invalid JSON in body",
                    "details": str(e),
                    "event": event
                })
            }
    else:
        body = event  # For local testing or non-API Gateway events

    task = body.get("task")
    if not task:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": "Missing 'task' in event",
                "event": event
            })
        }

    print(f"TASK: {task}")

    try:
        if task == "create":
            task_id = body.get("taskId")
            description = body.get("description")
            if not task_id or not description:
                return {
                    "statusCode": 400,
                    "body": json.dumps({
                        "error": "Missing 'taskId' or 'description' in create"
                    })
                }

            table.put_item(Item={
                "taskId": task_id,
                "description": description,
                "status": body.get("status", "incomplete")
            })
            print(f"Created item with taskId: {task_id}")
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Item created"})
            }

        elif task == "read":
            task_id = body.get("taskId")
            if not task_id:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "Missing 'taskId' in read"})
                }

            response = table.get_item(Key={"taskId": task_id})
            item = response.get("Item")
            if not item:
                return {
                    "statusCode": 404,
                    "body": json.dumps({"error": f"No item found with taskId: {task_id}"})
                }
            print(f"Read item: {item}")
            return {
                "statusCode": 200,
                "body": json.dumps(item)
            }

        elif task == "update":
            task_id = body.get("taskId")
            description = body.get("description")
            status = body.get("status")
            if not task_id or not description or not status:
                return {
                    "statusCode": 400,
                    "body": json.dumps({
                        "error": "Missing 'taskId', 'description', or 'status' in update"
                    })
                }

            table.update_item(
                Key={"taskId": task_id},
                UpdateExpression="SET description = :desc, #s = :stat",
                ExpressionAttributeNames={"#s": "status"},
                ExpressionAttributeValues={":desc": description, ":stat": status}
            )
            print(f"Updated item with taskId: {task_id}")
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Item updated"})
            }

        elif task == "delete":
            task_id = body.get("taskId")
            if not task_id:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": "Missing 'taskId' in delete"})
                }

            table.delete_item(Key={"taskId": task_id})
            print(f"Deleted item with taskId: {task_id}")
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Item deleted"})
            }

        else:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": f"Unknown task '{task}'",
                    "event": event
                })
            }

    except Exception as e:
        print(f"EXCEPTION: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "Exception occurred",
                "details": str(e),
                "event": event
            })
        }

````

- Logic supports all 4 operations:
  - `create`: Insert new task
  - `read`: Get one task or all
  - `update`: Modify an existing task
  - `delete`: Remove a task
- Environment variable set: `TABLE_NAME=Todos`
- IAM Role: Attached `AmazonDynamoDBFullAccess` policy

### ✅ 3. **Connected Lambda to API Gateway**
- Created **HTTP API** in API Gateway, `TodoAPI`
- Integration: Connected to `TodoLambdaAPI`
- Route: `/todo` with method `ANY`
- Stage: `dev`
- Invoke URL: `https://<your-api-id>.execute-api.ap-south-1.amazonaws.com/dev/todo`

### ✅ 4. **Tested All Operations via `curl`**

#### ➕ Create

	curl -X POST https://<invoke-url>/dev/todo -H "Content-Type: application/json" -d '{"task":"create", "taskId":"task001", "description":"Buy groceries"}'  

Output: (in DDB table)  
taskId - task001  
description - Buy groceries

#### ➕ Read

	curl -X POST https://<invoke-url>/dev/todo -H "Content-Type: application/json" -d '{"task":"read", "taskId":"task001"}'

Output: (on console)  
taskId - task001  
description - Buy groceries

#### ➕ Update

	curl -X POST https://<invoke-url>/dev/todo -H "Content-Type: application/json" -d '{"task":"update", "taskId":"task001", "description":"Buy vegetables"}'

Output: (in DDB table)  
taskId - task001  
description - Buy vegetables

#### ➕ Delete

	curl -X POST https://<invoke-url>/dev/todo -H "Content-Type: application/json" -d '{"task":"delete", "taskId":"task001"}'

Output: (in DDB table)  
taskId -  
description -  


### 📊 Visual Markdown Diagram

	[CURL Request] 				#You interact via terminal curl
     		|
     		v
	[API Gateway Route: /todo]		#API Gateway receives request and forwards it to Lambda
     		|
     		v
	[Lambda Function (with IAM access)]	#Lambda executes Python code using boto3 SDK
     		|
     		v
	[DynamoDB Table]			#DynamoDB stores or modifies data accordingly


#### ✅ Flags in curl command
| Flag | Stands for | Meaning                                                         |
| ---- | ---------- | --------------------------------------------------------------- |
| `-H` | **Header** | Sends extra info like `Content-Type` to the server              |
| `-d` | **Data**   | Sends data (usually JSON) in the request body                   |
| `-X` | **Method** | Tells `curl` which HTTP **method** to use (`GET`, `POST`, etc.) |


####📌 What does -X do exactly?
`-X` stands for "Request Method" (like a command to the server):
| `-X Method` | What it does                                |
| ----------- | ------------------------------------------- |
| `-X GET`    | Ask the server to **get** some data         |
| `-X POST`   | Ask the server to **add** new data          |
| `-X PUT` or `-X PATCH`    | Ask the server to **replace** existing data |
| `-X DELETE` | Ask the server to **delete** something      |


### 🧠 Learnings
- Understood the flow of data from curl → API Gateway → Lambda → DynamoDB.
- Learned difference between `-X`, `-H`, and `-d` in curl.
  - `-d` is used for `POST`, `PUT/PATCH` and `DELETE` methods because these are used to modify the data
  - no need to use `-d` with `GET` method because this doesn't modify any data, it is used only to read the data.
- Realized that API Gateway is the public face, Lambda is the brain, and DynamoDB is the memory.
- First time seeing cloud-native serverless API working end-to-end without any fake setups.

### Debugs
- The lambda functon, dynammoDB table and the API, all should be created in the same region.
- make sure to attach policy to the lambda function

