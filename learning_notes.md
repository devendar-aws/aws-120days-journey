# 📘 Learning Notes: Concepts, Commands, and Clarity from the 120-Day AWS Journey

This document captures key learnings, insights, and memorable technical concepts I (Devendar) encountered throughout my 120-day AWS learning journey.

---

## 📅 [Day 1] Sankalpa & Setup

- Understood the importance of setting clear, measurable goals (₹18 LPA, SAA-C03 certification, real projects).
- Learned GitHub basics:
  - Creating a repository
  - Writing a meaningful `README.md`
  - Structuring folders by week/day for clarity

---

## 📅 [Day 2] IAM + EC2 Intro

- IAM is used to securely control access to AWS services and resources.
- Created an IAM user with Admin permissions and enabled MFA.
- Learned how to:
  - Generate Access Key ID and Secret
  - Use `aws configure` to set up AWS CLI
  - Verify CLI setup using `aws sts get-caller-identity`
- IAM is a **global** service, unlike regional ones like EC2 or S3.
- Discovered that you can log in via **IAM user** using an **Account Alias**.

---

## 📅 [Day 3] S3 Static Website Hosting (Manual)

- Created an S3 bucket in ap-south-1 and learned region-specific limitations.
- Enabled Static Website Hosting.
- Understood:
  - Buckets are globally unique.
  - Public access must be explicitly enabled.
  - Website is accessed via the bucket’s endpoint.

---

## 📅 [Day 4] Apache Server on EC2 (Manual)

- Launched an EC2 instance, opened ports 22 and 80 in the security group.
- Connected via SSH using `.pem` key.
- Installed Apache and hosted a static website.
- Learned:
  - What is an AMI (Amazon Machine Image)?
  - Role of ports and security groups
  - Use of `systemctl`, `apt`, `sudo`, `tee`, and `index.html`
- Realized that launching an instance automatically starts it.

---

## 📅 [Day 5] Linux + Git + GitHub via CLI

- Understood `.pem` (Privacy Enhanced Mail) used by AWS vs `.pub` (public key) for GitHub.
- Key Types:
  - RSA (used for EC2)
  - ED25519 (used for GitHub)
- Generated SSH key with `ssh-keygen -t ed25519` for GitHub.
- Added key to GitHub and connected via `ssh -T git@github.com`.
- Learned Git basics:
  - `git init`, `add`, `commit`, `remote`, `push`
  - `git branch -M main` to align local with remote branch
  - `.git` folder stores local repo metadata
- Realized that changes sit in **staging area** after `git add`, and only move to history after `git commit`.
- Learned how to push from CLI by resolving "unrelated histories" error through merging branches and switching to `main`.
- Understood how to debug and correct SSH key errors.
- Captured GitHub CLI workflow using dedicated repo folder (`aws-cli-test`).

---

## 📅 [Day 6] Assessment + EIP + Review + Practice

- Revised all key concepts from IAM, EC2, S3, Git.
- Understood Elastic IP:
  - Public IP changes every restart.
  - EIP provides static IP.
  - Charges apply only if EIP is unassociated while allocated.
  - Can allocate, associate, disassociate, release via CLI or Console.
- Scored ~4/5 in assessment with partial answers.
- Realized GitHub, CLI, S3 concepts are getting stronger.

## 📅 [Day 7] Project 1 Completion + Resume/Profile V1

- Completed Project 1: Static Website Hosting with S3
- Created project folder under projects/project1-static-s3
- Added README, screenshot, bucket policy, website config.
- Created Resume V1:
  - Honest + strategic
  - No fake experience
  - 18 LPA goal highlighted
  - Amazon roles mapped to data/cloud context
- Added week01 summary, debug_notes.md, learning_notes.md, and README.md files.


## 📅 [Day 16] DynamoDB Basics - CRUD operations
- DynamoDB reserved keywords (like status, name, etc.) must be aliased using ExpressionAttributeNames.
- Indentation in Python is strict — even one space can cause syntax errors.
- Lambda Deployment Delay: After updating code, ensure it is fully deployed before re-testing.
- Partition Key = Primary Key when only one key is defined (e.g., taskId).

---

## 📅 [Day 17] API Gateway + Lambda Integration

- Understood the purpose and working of Amazon API Gateway.
- Linked API Gateway (REST API) with AWS Lambda to expose functions via HTTPS endpoints.
- Created Resources (`/tasks`) and Methods (POST, GET, PUT, DELETE).
- Tested end-to-end flow using `curl` commands from CLI.
- Learned how to use test events in Lambda and troubleshoot integration issues.
- Realized importance of correct region, deployment stage, and method types.

---

## 📅 [Day 18] Lambda CRUD with DynamoDB

- Connected Lambda to DynamoDB to implement TODO app.
- Handled JSON payloads to perform:
  - POST (create)
  - GET (read)
  - PUT (update)
  - DELETE (delete)
- Used `boto3` in Python to interact with DynamoDB.
- Understood Lambda role permissions for DynamoDB access.
- Used separate functions or conditions for each task inside Lambda handler.

---

## 📅 [Day 19] CloudWatch Logs & Debugging

- Used Amazon CloudWatch Logs to monitor Lambda invocations and errors.
- Learned how to add `print()` statements to debug within Lambda.
- Explored Log Groups and Log Streams per Lambda function.
- Realized logs are created only after first invocation post deployment.
- Improved logging clarity using consistent structure (`event`, `response`, etc.).

---

## 📅 [Day 20] Interview Qs + Cleanup

- Started preparing short answers to common AWS interview questions:
  - What is Lambda?
  - How does API Gateway integrate with Lambda?
  - How does DynamoDB work with Lambda?
- Reviewed entire TODO app flow and refined the code, logs, and comments.
- Organized project folder and ensured each operation works reliably.

---

## 📅 [Day 21] Assessment 3 + Week 3 Review

- Took **Assessment 03** covering:
  - Lambda Basics
  - DynamoDB CRUD
  - API Gateway integration
  - Debugging via CloudWatch
- Realized gaps in DynamoDB error handling and ExpressionAttributeNames.
- Completed week03 checklist, updated learning_notes.md and commands-week03.
- Felt confident about building REST APIs using AWS-native services alone.

## ✨ More learnings will be added as I go deeper into AWS, DevOps, and cloud project building.

Stay tuned. This file will help me quickly revise and reinforce everything when needed.
