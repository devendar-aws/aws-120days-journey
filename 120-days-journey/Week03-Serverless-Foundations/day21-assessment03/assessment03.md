# 📘 Assessment 03: Lambda Flow + DynamoDB Logic (Day 21 – July 26)

## ✅ Objective
Test conceptual clarity of AWS Lambda integration with API Gateway and DynamoDB, as well as error handling, status codes, and response flow.

---

## 🔹 Q1. Explain the flow of Lambda with API Gateway and DynamoDB.

When triggered via API Gateway, the Lambda function first connects to DynamoDB using the `boto3` library. It targets a specific table using the environment variable (table name). Inside the `lambda_handler`, it reads the `httpMethod` (e.g., GET, PUT) and routes the logic accordingly.  

The function takes the incoming payload, performs the intended CRUD operation on the DynamoDB table, and returns a JSON response with a status code.  
Meanwhile, logs of every invocation are automatically generated in **CloudWatch Logs** → `Log Group` → `Log Stream` → `Log Events`.

---

## 🔹 Q2. Why is `taskId` the partition key in this TODO App?

Partition key is the **unique identifier** to access a specific item from the table. In this project, `taskId` is used as the partition key to perform **CRUD operations** on the exact task we want to work with.

---

## 🔹 Q2 Follow-up: How does the PUT operation update a task?

When a PUT request is sent via cURL/Postman/Browser, the payload is passed through API Gateway to Lambda. Lambda identifies the task using the partition key (`taskId`) from the payload and updates the relevant fields. After modification, a response payload with `statusCode` and a success message is returned.

---

## 🔹 Q3. Why is error handling important in Lambda functions?

Error handling makes it easy to:
- **Locate bugs** in a multi-stage setup (frontend → API Gateway → Lambda → DynamoDB)
- Avoid guessing across components
- Get precise logs in CloudWatch

Typical errors:
- Missing IAM permission for DynamoDB
- Incorrect payload format (JSON)
- CORS errors (when calling via browser)
- Resource not found
- Lambda timeout

Using `try-except` and returning meaningful error messages saves debugging time.

---

## 🔹 Q4. Who is the original "client"?

The **user** who triggers the action (via browser, frontend app, CLI like cURL/Postman). The **Lambda + API Gateway + DynamoDB** system serves this client.

---

## 🔹 Q5. What is a Payload?

Payload = **Actual Data** sent or received in an API call.  
- **Request Payload**: Sent by user/client (e.g., task details in POST/PUT)
- **Response Payload**: Sent by Lambda to the client (e.g., success message or error)

---

## 🔹 Q6. Why is `statusCode` so important?

- Tells whether the operation was successful (`200`), invalid (`400`), or failed (`500`)
- Guides frontend/client behavior
- Helps in debugging without opening logs
- Makes the API response **standard and understandable across systems**
- Without `statusCode`, API Gateway may show errors like `502 Bad Gateway`

---

## 🧠 Reflection

> "All these are going on top of my head."  
Still, I could answer all questions with clarity and honesty. Some were completely new (like payload, statusCode), but I understood them during the quiz itself.  
I now see how Lambda, API Gateway, DynamoDB, CloudWatch, and response structures work together.  
This assessment gave me confidence that I’m learning the real cloud engineering flow.

