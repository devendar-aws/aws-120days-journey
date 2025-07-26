# Week 03 Cheat Sheet – Lambda, DynamoDB, API Gateway, CloudWatch

---

## ✅ Lambda Basics

| Concept               | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| What is Lambda?        | Serverless compute that runs code on triggers (API, S3, etc.)              |
| handler(event, context)| `event` is the input; `context` gives runtime info                         |
| Use Cases              | REST APIs, automation, event pipelines                                     |

---

## ✅ DynamoDB Basics

| Concept        | Description                                   |
|----------------|-----------------------------------------------|
| Type           | NoSQL – Key-Value + Document Store            |
| Table          | Collection of items                           |
| Item           | A row (JSON object)                           |
| Attribute      | Columns of item (e.g., taskId, status)        |
| Partition Key  | Primary key used for unique identification    |

**Python Example**:
```
import boto3
table = boto3.resource('dynamodb').Table('YourTableName')
```
---

## ✅ API Gateway Integration
| Feature           | Role                                                  |
| ----------------- | ----------------------------------------------------- |
| Trigger           | Invokes Lambda via HTTP requests                      |
| Request Handling  | Parses body, headers, query params                    |
| Response Handling | Formats response, adds status codes                   |
| CORS              | Cross-origin access (Access-Control-Allow-Origin: \*) |

---

## ✅ Lambda TODO Project – CRUD Flow
| HTTP Method | Task         | Lambda Action           | DynamoDB Effect   |
| ----------- | ------------ | ----------------------- | ----------------- |
| POST        | Create Task  | `put_item()`            | Add new item      |
| GET         | Read Task(s) | `scan()` / `get_item()` | Fetch data        |
| PUT         | Update Task  | `update_item()`         | Modify attributes |
| DELETE      | Delete Task  | `delete_item()`         | Remove item       |

### Sample Payloads:
```
// POST
{
  "task": "create",
  "taskId": "001",
  "description": "Study Lambda",
  "status": "pending"
}

// PUT
{
  "task": "update",
  "taskId": "001",
  "description": "Study Lambda Deeply",
  "status": "done"
}
```

---

## ✅ CloudWatch Logs
| Term       | Meaning                                           |
| ---------- | ------------------------------------------------- |
| Log Group  | `/aws/lambda/<function-name>`                     |
| Log Stream | Unique log per Lambda invocation                  |
| Log Events | Shows `print()` output, errors, flow of execution |
| Use Case   | Debug Lambda, trace payloads, understand failures |

---

## ✅ Interview Questions Start – Key Topics
| Question                         | Sample Answer                                                  |
| -------------------------------- | -------------------------------------------------------------- |
| Who triggers Lambda?             | API Gateway, S3, EventBridge, etc.                             |
| What is the Lambda payload?      | JSON input via `event` param                                   |
| Why error handling is important? | For debugging and tracing failures                             |
| What are status codes used for?  | Indicate success (200), client error (400), server error (500) |


---

## ✅ Assessment 03 Topics Covered
| Area                | Subtopics                         |
| ------------------- | --------------------------------- |
| Lambda + DDB Logic  | CRUD operations, Boto3 methods    |
| Payloads            | Structure, event-based branching  |
| Error Handling      | Try-except, print debugging       |
| Logs                | Tracing in CloudWatch             |
| Interview Readiness | Practice Qs, real-world scenarios |

