# 📝 Project 02 – [Serverless TODO App](http://todo-app-project-devendar.s3-website.ap-south-1.amazonaws.com/)  
**Duration**: Day 18 & Day 19 (July 23–24, 2025)  
**Status**: ✅ Completed  
**Tech Stack**: HTML, CSS, JavaScript, AWS Lambda, API Gateway, DynamoDB  

---

## 📌 Overview  
This project implements a fully functional TODO list application using a **serverless architecture**. The frontend is built with vanilla HTML/CSS/JavaScript, while the backend is powered by **AWS Lambda functions** exposed via **API Gateway**. Data is persisted in **DynamoDB**, allowing CRUD operations (Create, Read, Update, Delete) without any traditional servers.

---

## 🧩 Architecture  
HTML/JS (Frontend)  
⬇️ fetch()  
API Gateway (REST)  
⬇️ Lambda Integration  
AWS Lambda Function  
⬇️ boto3 SDK  
DynamoDB (NoSQL Storage)

---

## 🔧 Features Implemented

| Operation | Method | Description                         |
|----------:|--------|-------------------------------------|
| Add Task | POST   | Adds a new task to DynamoDB         |
| View All | GET    | Fetches all tasks                   |
| Edit     | PUT    | Updates task `description/status`   |
| Delete   | DELETE | Deletes task using `taskId`         |

---

## 💡 What I Used

- **Frontend**
  - HTML for structure
  - CSS for simple styling
  - JavaScript `fetch()` to call APIs
  - Dropdown + Input Form for interactive editing

- **Backend**
  - Lambda function handling all 4 methods
  - `event["httpMethod"]` conditional logic
  - `boto3` for DynamoDB operations
  - Region set properly to avoid mismatches

- **AWS Services**
  - **DynamoDB** with `taskId` as partition key
  - **Lambda** function with IAM role allowing full access to DynamoDB
  - **API Gateway** with proper CORS and method mappings

---

## 🧪 How I Tested It

- ✅ Used `cURL` from terminal to test all 4 endpoints before wiring frontend
- ✅ Validated functionality directly from the HTML page after frontend was connected
- ✅ Confirmed that tasks were being persisted, updated, and deleted from DynamoDB table

---

## 🧰 Challenges Faced & Solved

| Issue | Root Cause | Fix |
|-------|------------|-----|
| ❌ Update & Delete not working | Lambda syntax error (indentation, missing block) | Carefully re-indented code, verified logic |
| ❌ ResourceNotFoundException | Lambda and DynamoDB in different regions | Aligned both to same region (ap-south-1) |
| ❌ CORS errors | No headers in API Gateway | Added CORS headers in method responses |
| ❌ JSON parsing issues | Missing `Content-Type` header | Ensured headers set in fetch and cURL |

---

## 🎯 What I Learned

- Writing multi-method logic (`POST`, `GET`, `PUT`, `DELETE`) in one Lambda function
- Debugging real-world AWS issues like region mismatch, syntax errors, and CORS
- Clean integration between frontend and serverless backend using API Gateway
- How to organize API calls and state updates from plain JavaScript

---

## 🚀 Outcome

After 2 intense days of development and debugging, I successfully completed the entire flow — **Add**, **View**, **Edit**, and **Delete** tasks — through a responsive frontend and serverless backend.  
All operations now work end-to-end with clean logs and no errors.  
This marks a major milestone in my 120-day journey and gave me deep practical exposure to AWS Lambda and API Gateway integration.

---

## ⏭️ Next Steps

- 🔍 Set up **CloudWatch Logs** for Lambda (Day 20)
- 🧠 Start solving **Interview Questions** (3/day from Day 20)
- 💬 Document project on GitHub with clear commit history

---

_“Simple tools, powerful clarity. One step at a time.”_

