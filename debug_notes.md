# 🛠️ Debug Notes: Challenges, Fixes & Workarounds in My AWS Journey

This file captures all debugging situations and fixes I encountered — so I can revisit and reflect when facing similar issues in the future.

---

## 🧭 [Day 5] GitHub SSH Key Not Matching

**Problem:**  
SSH authentication to GitHub failed with fingerprint mismatch.

**Mistake:**  
I accidentally added this key:  
`ssh-ed25519 AAAAC3...z0Hl devendar.aws@gmail.com`  
instead of:  
`ssh-ed25519 AAAAC3...zOHl devendar.aws@gmail.com`  
(Notice the character difference in the key ending)

**Fix:**  
- Rechecked the public key
- Updated the correct key on GitHub → SSH keys
- Verified using: `ssh -T git@github.com`
- ✅ Output: *Hi devendar-aws! You've successfully authenticated...*

---

## 🧭 [Day 5] Git Push Failed – Unrelated Histories

**Problem:**  
`git push origin main` failed with:  
`fatal: refusing to merge unrelated histories`

**Cause:**  
- GitHub repo was initialized separately.
- Local repo was initialized via `git init` — they had different histories.

**Fix:**

    git pull origin main --allow-unrelated-histories
# Then resolved the merge message (left as default)
    git push origin main

---

## 🧭 [Day 5] Local Branch Was master, Not main

**Problem:**
Push failed due to branch name mismatch.

**Fix:**

    git branch -M main

This renamed local branch to main to match remote.

---

## 🧭 [Day 11] Public read ACL

- ❗ Got `AccessControlListNotSupported` error when using `--acl public-read`  
  👉 Root Cause: The bucket had **ACLs disabled via Block Public Access (BPA)**  
  ✅ Fix: Removed `--acl public-read` from the script. Upload + access worked correctly.

- 🧰 EC2 instance had no `unzip` package  
  ✅ Fix: Installed using `sudo apt install unzip`, enabling AWS CLI installation.

---

## 🧭 [Day 16] Lambda + DynamoDB CRUD
| 🕒 Time          | 🔧 Issue                                                 | 🧠 Root Cause                                                         | ✅ Fix                                                     |
| ---------------- | -------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------- |
| ✅ Initial        | Getting consistent `"Item created"` response             | None                                                                  | Lambda Create (PUT) was working correctly                 |
| ❌ Update Error 1 | `ValidationException: reserved keyword: status`          | `"status"` is a **reserved word** in DynamoDB                         | Used `ExpressionAttributeNames` to alias `status` as `#s` |
| ❌ Update Error 2 | `Syntax error: expected an indented block after 'elif'`  | Python indentation error after `elif task == "update":`               | Fixed indentation under the `elif` block                  |
| ❌ Deployment lag | Lambda ran old version after update                      | Lambda still executing **previous version** due to ongoing deployment | Waited for deployment to complete or redeployed manually  |
| ✅ Final          | Create, Read, Update, Delete all working via test events | -                                                                     | Clean, tested function for all CRUD operations            |

---

## 🧭 [Day 18] API Gateway Testing (cURL vs Browser vs Postman)

**Problem:**  
PUT and DELETE methods failed in Postman with CORS/403 errors.

**Root Cause:**  
- CORS not enabled for all methods (especially PUT/DELETE).
- Postman skips some preflight behavior (like browsers trigger).

**Fix:**  
- Enabled CORS (OPTIONS method) in API Gateway.
- Tested using browser and cURL instead of Postman.

```
curl -X PUT https://<api-id>.execute-api.<region>.amazonaws.com/dev/tasks \
  -H "Content-Type: application/json" \
  -d '{"task": "update", "taskId": "001", "description": "Updated desc", "status": "done"}'
```

---

## 🧭 [Day 19] CloudWatch Logs Not Appearing

**Problem:**  
Lambda executed, but no logs in CloudWatch.

**Root Cause:**
- Missing logs:CreateLogStream or logs:PutLogEvents permissions.
- Lambda role didn’t include basic execution policy.

**Fix:**
- Attached AWSLambdaBasicExecutionRole to Lambda's IAM role.
- Redeployed the function.
- ✅ Logs started appearing in CloudWatch.

---

## 🧭 [Day 19] DynamoDB ResourceNotFoundException

**Problem:**  
PutItem failed even though table name was correct.

**Root Cause:**
- DynamoDB table created in a different AWS region than Lambda.

**Fix:**
- Re-created DynamoDB table in same region as Lambda.
- ✅ All operations (PUT/GET) worked after region match.

---

## 🧭 [Day 20] Browser CORS Error

**Problem:**  
Browser fetch to API Gateway failed:
```
Access to fetch at <API> from origin '<site>' has been blocked by CORS policy
```
**Root Cause:**  
API Gateway did not return Access-Control-Allow-Origin in response.

**Fix:**
- Enabled CORS for all methods (GET, POST, PUT, DELETE).
- Added headers manually in Integration Response > Header Mapping.
- Redeployed the stage.

---

