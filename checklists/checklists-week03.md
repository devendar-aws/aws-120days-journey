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

# ✅ TODO App - Progress Checklist (Day 18 & Day 19)

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

