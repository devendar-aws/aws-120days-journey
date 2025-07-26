### ✅ Day 15 checklist – Lambda Basics (20 July, 2025)

| Task                                                                 | Status |
|----------------------------------------------------------------------|--------|
| Created Lambda function using Python                                 | ✅     |
| Understood handler syntax, event + context parameters                | ✅     |
| Created and tested a basic event JSON input                          | ✅     |
| Printed custom fields from event (e.g., name, task, progress)        | ✅     |
| Viewed output in Function Logs and understood log format             | ✅     |
| Used “Deploy” before testing to reflect latest code                  | ✅     |
| Saved code file (`lambda_function.py`) in GitHub                     | ✅     |
| Saved test event JSON in GitHub (`event.json`)                       | ✅     |
| Uploaded key screenshots of console and execution                    | ✅     |
| Created `day15-readme.md` with description and test output           | ✅     |
| Added Day 15 flashcards to `flashcards.md` (Lambda + IAM/S3/EC2)     | ✅     |
| ✅ Day 15 complete                                                    | 🎯     |

---

### ✅ Day 16 Checklist – Lambda CRUD Operations (July 21, 2025)

| Task Category               | Task Description                                                                | Status |
|----------------------------|----------------------------------------------------------------------------------|--------|
| **DynamoDB Setup**         | Created `Tasks` table with `taskId` as Partition Key                           | ✅     |
|                            | Manually inserted an initial item via console                                   | ✅     |
| **Lambda Function**        | Connected Lambda to DynamoDB using `boto3`                                      | ✅     |
|                            | Implemented `create` operation                                                  | ✅     |
|                            | Implemented `read` operation                                                    | ✅     |
|                            | Implemented `update` operation                                                  | ✅     |
|                            | Implemented `delete` operation                                                  | ✅     |
|                            | Handled reserved keyword (`status`) using ExpressionAttributeNames              | ✅     |
|                            | Added log statements for all branches                                           | ✅     |
|                            | Added validation for missing `taskId`                                           | ✅     |
| **Test Events**            | Created test event for `create` and verified                                    | ✅     |
|                            | Created test event for `read` and verified                                      | ✅     |
|                            | Created test event for `update` and verified                                    | ✅     |
|                            | Created test event for `delete` and verified                                    | ✅     |
| **Troubleshooting**        | Solved "stale code" issue by re-creating the Lambda function                    | ✅     |
| **Docs & Wrap-up**         | Cleaned up final Lambda code                                                    | ✅     |
|                            | Completed `README.md`                                                           | ✅     |
|                            | Completed `checklist.md` in table format                                        | ✅     |

---

### ✅ Day 17 Checklist – API Gateway link (22 July, 2025)

| Task                           | Status |
| ------------------------------ | ------ |
| DynamoDB table created         | ✅      |
| Lambda function created        | ✅      |
| IAM permissions attached       | ✅      |
| API Gateway integration done   | ✅      |
| `curl` tested for all CRUD ops | ✅      |
| Code pushed to GitHub          | ✅      |

---

### ✅ TODO App - Progress Checklist (Day 18 & Day 19)

| ✅ Task Done? | Feature / Task                              | Notes / Status                                               |
|--------------|----------------------------------------------|--------------------------------------------------------------|
| ✅           | Create DynamoDB Table                         | Table created with `taskId` as Partition Key                |
| ✅           | Configure IAM Role for Lambda                 | Lambda granted DynamoDB full access via execution role      |
| ✅           | Write Lambda function                         | Handled POST, GET, PUT, DELETE                              |
| ✅           | Set up API Gateway                            | REST API with 4 methods integrated to Lambda                |
| ✅           | Enable CORS in API Gateway                    | Access from HTML/JS frontend enabled                        |
| ✅           | Build HTML/CSS/JS Frontend                    | Clean, minimal UI with dynamic form and list rendering      |
| ✅           | Connect Frontend to API                       | Used `fetch()` with correct endpoints and methods           |
| ✅           | Test POST (Add Task)                          | Tested using cURL and HTML form                             |
| ✅           | Test GET (Fetch Tasks)                        | Tasks correctly retrieved and rendered                      |
| ✅           | Test PUT (Update Task)                        | Tasks updated by `taskId` using dropdown + form             |
| ✅           | Test DELETE (Delete Task)                     | Tasks deleted successfully                                  |
| ✅           | Debug CORS, region mismatch, syntax errors    | Resolved line indent error, wrong region issue              |
| ✅           | Validate full CRUD from frontend              | All operations working end-to-end                           |
| [x]          | Monitor Lambda using CloudWatch Logs          | To be completed on **Day 20**                               |
| [x]          | Start Interview Questions (3 per day)         | Scheduled for **Day 20** onward                             |

---

### 🚀 Final Status:
- ✅ Completed full stack TODO App with frontend + API + Lambda + DynamoDB.
- 🛠️ Debugged deployment and syntax issues with patience and clarity.
- 😌 Feeling satisfied — project is now fully functional.

---


### ✅ Day 20 Checklist – Jul 25, 2025 (AWS Journey – Day 20 of 120)

| Task Description                                                    | Status   |
|---------------------------------------------------------------------|----------|
| Reviewed CloudWatch Logs for all 4 HTTP methods                     | ✅ Done   |
| Printed incoming events using `json.dumps(event, indent=2)`         | ✅ Done   |
| Logged Lambda responses using `json.dumps(resp, indent=2)`          | ✅ Done   |
| Deployed Lambda function and retested endpoints using cURL         | ✅ Done   |
| Wrote detailed `day20_readme.md` with CloudWatch debug insights     | ✅ Done   |
| Began Interview Q&A for tech and scenario-based preparation         | ✅ Done   |
| Answered 5 questions with clarity and correctness                   | ✅ Done   |
| Understood the impact of `indent=2` vs `indent=4` in CloudWatch     | ✅ Done   |

---

### 📋 Day 21 Checklist – July 26 (Saturday)
**Theme:** Lambda + DynamoDB Integration | API Flow | Assessment 03

| Task                                                                 | Status    | Notes |
|----------------------------------------------------------------------|-----------|-------|
| Reviewed Lambda handler logic for all 4 methods (POST, GET, PUT, DELETE) | ✅ Done    | Clear understanding now |
| Recalled how `taskId` is used as partition key                       | ✅ Done    | Used in all operations |
| Understood error handling inside Lambda                              | ✅ Done    | try–except pattern |
| Reviewed where CloudWatch logs are stored                            | ✅ Done    | Group > Stream > Events |
| Learnt the meaning of “payload” (request and response)               | ✅ Done    | Clear concept |
| Learnt the importance of `statusCode` in API Gateway + Lambda flow  | ✅ Done    | Client-visible output |
| Completed full Assessment 03 (6 Questions)                           | ✅ Done    | Answered all honestly |
| Understood the role of the client in the flow                        | ✅ Done    | Frontend/web user |
| Completed README.md summarizing Day 21                               | ✅ Done    | ✔ Posted |
| Wrote Reflection and uploaded `assessment03.md`                      | ✅ Done    | ✔ Posted |

---

## 🌕 Overall Status: **100% Completed**
