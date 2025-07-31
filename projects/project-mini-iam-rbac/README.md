# 🛡️ Mini IAM RBAC Demo – AWS CLI + Console (Day 26)

## 📅 Date: July 30, 2025  
## 📁 Type: Mini Project  
## 🎯 Goal: Demonstrate IAM RBAC using AWS Groups and Policies via CLI

---

## 📌 Project Summary

This mini project demonstrates **Role-Based Access Control (RBAC)** using AWS IAM Groups, Users, and Policies.

We created two IAM users with distinct responsibilities:
- **`devuser`** with full EC2 access via a managed group policy.
- **`audituser`** with read-only access to IAM via a custom policy.

This was achieved entirely through **AWS CLI** commands, followed by **login verification via AWS Console** and **cleanup operations**.

---

## 🧱 IAM Architecture

Users Groups Policies  

devuser → devgroup → AmazonEC2FullAccess (AWS managed)  
audituser→ auditgroup → IAMReadOnlyCustomPolicy (custom)  

---

## 🔧 Steps Performed

1. **Create IAM Users**
   - `devuser`
   - `audituser`

2. **Create IAM Groups**
   - `devgroup`
   - `auditgroup`

3. **Attach Policies**
   - AWS managed policy `AmazonEC2FullAccess` to `devgroup`
   - Custom JSON policy `IAMReadOnlyCustomPolicy` to `auditgroup`

4. **Add Users to Groups**

5. **Login as Users**
   - Verified `devuser` can launch EC2
   - Verified `audituser` can only view IAM console, not edit

6. **Cleanup**
   - Remove users from groups
   - Detach policies
   - Delete users, groups, and custom policy

---

## 📜 Custom IAM Policy Used

**IAMReadOnlyCustomPolicy.json**
```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:Get*",
        "iam:List*"
      ],
      "Resource": "*"
    }
  ]
}
```
---

## 💻 CLI Commands Used
> See full CLI log [here](./../../120-days-journey/Week04-automation\&infra-skills/day26-iam-project/README.md)

✅ Created users, groups  
✅ Attached managed and custom policies  
✅ Added users to groups  
✅ Verified console access  
✅ Performed full cleanup  

#@ ✅ Learning Outcomes  
- Understood group-based IAM management
- Practiced creating and attaching custom IAM policies
- Gained clarity on separation of duties via group permissions
- Hands-on AWS CLI for real-world IAM scenarios

##📁 Cleanup Summary
- `devuser`, `audituser` – deleted
- `devgroup`, `auditgroup` – deleted
- `IAMReadOnlyCustomPolicy` – deleted

##📚 Resources
- AWS IAM Documentation
- IAM Policy Generator
- AWS CLI Official Guide

## 🧠 Status: ✅ Completed on Day 26

> This mini project will strengthen my confidence in AWS IAM fundamentals and group-level access control using both AWS CLI and Console.
