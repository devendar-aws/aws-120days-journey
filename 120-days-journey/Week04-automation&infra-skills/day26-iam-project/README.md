# IAM RBAC DEMO – AWS IAM Group-Based Access Control

## 📅 Date: July 30, 2025  
## 🏗️ Type: Mini Project  
## 🌱 Goal: Learn and demonstrate AWS Identity and Access Management (IAM) using Role-Based Access Control (RBAC) with Users, Groups, and Policies.

---

## 🎯 Objective

Simulate a real-world IAM RBAC setup using:
- **Two IAM users**: `devuser`, `audituser`
- **Two IAM groups**: `devgroup`, `auditgroup`
- **Different IAM policies**: EC2 FullAccess for `devgroup`, IAM read-only custom policy for `auditgroup`

This exercise helps understand how to:
- Attach AWS managed policies
- Create and assign custom policies
- Use groups to manage user access
- Test permission boundaries
- Clean up IAM entities securely

---

## 🔧 Step-by-Step Implementation
### 1️⃣ Create IAM Users

- **devuser**
  - Login access: Enabled
  - Password reset on first login: ✅ Yes
- **audituser**
  - Login access: Enabled
  - Password reset on first login: ✅ Yes

### 2️⃣ Create IAM Groups

- **devgroup**
  - Attached Policy: `AmazonEC2FullAccess` (AWS Managed)
- **auditgroup**
  - Attached Policy: *Custom policy with read-only IAM access*

### 3️⃣ Attach Users to Groups

- `devuser` ➡️ `devgroup`
- `audituser` ➡️ `auditgroup`

### 4️⃣ Custom IAM Policy: `IAMReadOnlyCustomPolicy`

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:Get*",
        "iam:List*",
        "iam:Generate*"
      ],
      "Resource": "*"
    }
  ]
}
```
- Attached this policy only to `auditgroup`

## 🔍 Testing Access
### ✅ `devuser`:
- Can launch, stop, and manage EC2 instances
- ❌ Cannot view or access IAM users, roles, or policies

### ✅ `audituser`:
- Can list IAM users, groups, roles, and policies
- ❌ Cannot manage or view EC2 resources

## 🧹 Cleanup

After validation, all resources were deleted from the AWS Console:
- Deleted users: `devuser`, `audituser`
- Deleted groups: `devgroup`, `auditgroup`
- Deleted custom policy: `IAMReadOnlyCustomPolicy`

## ✅ Key Learnings
- IAM groups help manage access at scale
- AWS managed policies offer quick permission setups
- Custom policies allow fine-grained control
- Login password reset can be enforced using the `--password-reset-required` flag
- Always clean up after permission experiments to maintain security hygiene

## 🔚 End of Day Status
- IAM RBAC Demo completed
- ACcess control verified
- Cleanup done
- Pushed to GitHub


## AWS CLI Commands used for the IAM RBAC (Role Based Access Control)
### ✅ 1. Create IAM users with console login access and force password reset
```
aws iam create-user --user-name devuser
aws iam create-user --user-name audituser

aws iam create-login-profile --user-name devuser --password "Devuser@123" --password-reset-required
aws iam create-login-profile --user-name audituser --password "Audituser@123" --password-reset-required
```
### ✅ 2. Create IAM groups
```
aws iam create-group --group-name devgroup
aws iam create-group --group-name auditgroup
```
### ✅ 3. Attach AWS managed policy to devgroup
```
aws iam attach-group-policy \
  --group-name devgroup \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess
```
### ✅ 4. Create custom policy JSON for IAM read-only access
### (Saved locally as iam-readonly-custom-policy.json)
```
nano iam-readonly-custom-policy.json 
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:Get*",
        "iam:List*",
        "iam:Generate*"
      ],
      "Resource": "*"
    }
  ]
}
```
### ✅ 5. Create custom IAM policy from the JSON file
```
aws iam create-policy \
  --policy-name IAMReadOnlyCustomPolicy \
  --policy-document file://iam-readonly-custom-policy.json
```
### ✅ 6. Attach custom policy to auditgroup
```
aws iam attach-group-policy \
  --group-name auditgroup \
  --policy-arn arn:aws:iam::`<your-account-id>`:policy/IAMReadOnlyCustomPolicy
```
### ✅ 7. Add users to respective groups
```
aws iam add-user-to-group --user-name devuser --group-name devgroup
aws iam add-user-to-group --user-name audituser --group-name auditgroup
```
---

## 🧹 Cleanup Commands (after testing)
### ✅ Detach policies from groups
```
aws iam detach-group-policy \
  --group-name devgroup \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess

aws iam detach-group-policy \
  --group-name auditgroup \
  --policy-arn arn:aws:iam::`<your-account-id>`:policy/IAMReadOnlyCustomPolicy
```
### ✅ Remove users from groups
```
aws iam remove-user-from-group --user-name devuser --group-name devgroup
aws iam remove-user-from-group --user-name audituser --group-name auditgroup
```
### ✅ Delete user login profiles
```
aws iam delete-login-profile --user-name devuser
aws iam delete-login-profile --user-name audituser
```
### ✅ Delete IAM users
```
aws iam delete-user --user-name devuser
aws iam delete-user --user-name audituser
```
### ✅ Delete groups
```
aws iam delete-group --group-name devgroup
aws iam delete-group --group-name auditgroup
```
### ✅ Delete custom policy
```
aws iam delete-policy \
  --policy-arn arn:aws:iam::`<your-account-id>`:policy/IAMReadOnlyCustomPolicy
```
