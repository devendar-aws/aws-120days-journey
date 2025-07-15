# 📅 Day 10: IAM Roles, Policies & EC2 Access Control (with EBS Snapshot CLI carry-over) (July 15, 2025)

## 📌 Summary

Today focused on mastering **IAM Roles & Policies** for securely accessing AWS services **without access keys** — especially for EC2. You also completed the **CLI demo of EBS Snapshot** carried over from Day 09.

---

## 🔐 IAM Roles & Policies – Core Concepts

### ✅ Role Components
- **Trust Policy** → Who can assume the role (e.g., EC2)
- **Permission Policy** → What the role can do (e.g., S3FullAccess)

### ✅ Types of Policies
| Type          | Scope         | Reusable | Best For                         |
|---------------|---------------|----------|----------------------------------|
| **Managed**   | Roles/Users   | ✅ Yes   | Reuse, AWS-provided permissions  |
| **Inline**    | One identity  | ❌ No    | Tight control, one-off rules     |

---

## 🧠 Key Learnings

- IAM Role assumption via EC2 metadata (temporary credentials)
- Role attachment allows EC2 to access S3 without keys
- CLI role creation requires elevated permissions (not possible from EC2 by default)
- Difference between **Managed** and **Inline** policies
- Confirmed that **trust policy** = WHO, **permission policy** = WHAT
- Used `aws s3 ls` from EC2 after role assignment
- EBS Snapshot creation, volume from snapshot, and verification via CLI

---

## 🔧 Commands Practiced (Including Day 09 Carryover)

### IAM Role (Console & CLI Reference)

# List roles
`aws iam list-roles`

# Attach managed policy to role
    aws iam attach-role-policy \
      --role-name ec2-s3-access-role \
      --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess

# EC2 S3 Test

`aws s3 ls`



