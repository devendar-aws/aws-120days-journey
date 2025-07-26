# ✅ Day 21 – Lambda & DDB Assessment (26 July, 2025)

## 🎯 Focus
- Revision of Lambda CRUD logic
- Complete Assessment 03: Lambda Flow + DynamoDB Logic

---

## 📘 What I Did Today

- ✅ Reviewed how Lambda communicates with DynamoDB via `boto3`
- ✅ Understood importance of environment variables (like table name)
- ✅ Took a quiz on Lambda flow, DynamoDB logic, partition key, PUT update, error handling, status codes, payloads
- ✅ Understood status codes (`200`, `400`, `500`) and why they are essential
- ✅ Realized how `taskId` acts as partition key for performing precise item operations
- ✅ Practiced explaining full Lambda + API Gateway + DDB + CloudWatch flow in words

---

## 🧠 What I Learned

- Lambda reads the `httpMethod` and routes logic inside handler
- All logs (including errors) go to CloudWatch → Log Group → Log Stream
- PUT uses the same partition key (`taskId`) to update existing item
- Error handling makes debugging easier in a distributed flow
- Payload = data sent/received (Request/Response)
- Status codes are standard and vital for professional APIs

---

## 🔍 Reflection

This day tested everything I practiced in the last 4–5 days. The assessment helped me *consolidate* my understanding. I now feel more confident explaining the backend cloud flow in interviews and documentation.

---

