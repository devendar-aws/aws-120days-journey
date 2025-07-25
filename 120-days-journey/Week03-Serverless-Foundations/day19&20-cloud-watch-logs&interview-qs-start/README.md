#  ~] TODO App with CloudWatch Logging (Project 2 – Day 19 & 20) (25 July, 2025)

This is an extended version of my TODO App built using **AWS Lambda + API Gateway + DynamoDB**, with new features for **monitoring**, **debugging**, and **command-line testing**. It aligns with my 120-day sankalpa to reach ₹18 LPA by building real-world projects the honest way — no fake experience.

---

##  ~E Day 19 – CloudWatch Logs Setup

###  M-' What I Did

- ✅ Enhanced the Lambda function to include multiple `print()` statements for debugging.
- ✅ Used `json.dumps(..., indent=2)` for clean, readable log formatting.
- ✅ Deployed the updated Lambda function and API Gateway resources.
- ✅ Opened **CloudWatch > Log Groups > Stream > Events** to validate logs.

###  M-5 Logs Tracked

- Incoming event object
- HTTP method detected
- Routing decisions inside Lambda
- DynamoDB response
- Final API return payload

###  ~M Sample Log Snippet

```plaintext
 M-% Received event:
{
  "httpMethod": "POST",
  "taskId": "1",
  "description": "Try Lambda",
  "status": "pending"
}
 M-- HTTP Method: POST
 M-$ Returning response:
{
  "statusCode": 200,
  "body": "{\"message\": \"Task created successfully\"}"
}
```
---

### ~E Day 20 – Testing + Interview Q&A + Logs Summary
✅ cURL-Based API Testing

Tested all 4 operations using curl directly from the command line.
#### POST
```curl -X POST https://your-api-url/dev/todo \
  -H "Content-Type: application/json" \
  -d '{"httpMethod": "POST", "taskId": "1", "description": "Try Lambda", "status": "pending"}'```

### GET
```curl -X GET https://your-api-url/dev/todo \
  -H "Content-Type: application/json" \
  -d '{"httpMethod": "GET"}'```

### PUT
```curl -X PUT https://your-api-url/dev/todo \
  -H "Content-Type: application/json" \
  -d '{"httpMethod": "PUT", "taskId": "1", "description": "Updated task", "status": "done"}'```

### DELETE
```curl -X DELETE https://your-api-url/dev/todo \
  -H "Content-Type: application/json" \
  -d '{"httpMethod": "DELETE", "taskId": "1"}'```

✅ All responses were correct.
✅ CloudWatch logs showed accurate operation tracking.
✅ Verified API flow, logs, and return status codes.


## M-/ Interview Practice (Lambda Logs)

- How to verify logs for a Lambda-backed API Gateway?
  - → Go to CloudWatch > Log Group > Log Stream > Expand log event.
- What’s the use of event and context in Lambda?
  - → event handles request input; context gives metadata & methods.
- Why use print() and what does return do?
  - → print() shows internal flow in logs; return is the HTTP response.
- Why use json.dumps(..., indent=2)?
  - → For readable multi-line JSON logs — helps in debugging.


##  ~L Summary of Learnings
| Area               | Insights                                                         |
| ------------------ | ---------------------------------------------------------------- |
| ✅ Lambda Debugging | Can now debug API flow via CloudWatch using clear logs.          |
| ✅ curl Proficiency | Can hit APIs and test all CRUD ops without Postman.              |
| ✅ JSON Formatting  | `indent=2`/`indent=4` controls log readability in nested JSON.   |
| ✅ Dev Confidence   | Feel more confident reading request→handler→response life cycle. |

## M-  Keywords

`Lambda` · `API Gateway` · `DynamoDB` · `CloudWatch Logs` · `curl` · `Monitoring` · `Debugging` · `Event` · `Context`

## ~T Sankalpa Reflection

I didn't just code today — I tested like an engineer, observed like a monitor, and answered like a job-ready candidate. These two days gave me the confidence that I can not only build cloud systems but also explain, test, and debug them — the DevOps way, with clarity.
