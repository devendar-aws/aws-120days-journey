# 📘 Assessment-01: IAM, EC2, S3 Revision

**Date:** July 11, 2025  
**Theme:** IAM + EC2 + S3  
**Type:** Scenario-based + CLI-practical  
**Evaluator:** ChatGPT (Skill-based)

---

## ❓ Questions Attempted

---

### 1️⃣ Create a new IAM user who can log in to the Console with S3 ReadOnly permissions.

**🧠 Your Answer:**  
> I will login to my aws account using root credentials, search IAM in the search box and select the IAM service.  
> I will click on Users > Create User > give User details:  
> 1. User Name: assessment-1, check "Provide user access to the AWS Management Console", and select "I want to create an IAM user".  
> 2. Create custom password, uncheck "Users must create new password at next sign-in", and click Next.  
> 3. Attach Policy: Select **AmazonS3ReadOnlyAccess**, then click Next.  
> 4. Review and click "Create User".  
> 5. Download the credentials CSV file. Done.

✅ **Score:** `1 / 1`  
💬 Excellent step-by-step flow. Matches production use-case.

**✅ Ideal Answer:**  
Create IAM user with:
- Management Console access
- Custom password
- Attach `AmazonS3ReadOnlyAccess` policy
- Save credentials
- Optionally, tag user and enforce MFA later

---

### 2️⃣ A user cannot access a public object in S3 despite having correct IAM permissions. Why?

**🧠 Your Answer:**  
> 1. The user might be logging in through a different user credentials.  
> 2. There are no objects inserted yet in the bucket.  
> 3. The object doesn't have read permission.

✅ **Score:** `0.5 / 1`  
💬 Mentioned good ideas but missed main causes like BPA or missing bucket policy.

**✅ Ideal Answer:**  
- Check if **Block Public Access (BPA)** is disabled for the bucket  
- Ensure the **bucket policy** allows `s3:GetObject` for `"Principal": "*"`  
- Verify object exists and is correctly named (key match)  
- Confirm if IAM user’s permission and bucket policy are in sync  
- Confirm region of access matches bucket region

---

### 3️⃣ SSH into an EC2 instance fails with `.pem` file — causes?

**🧠 Your Answer:**  
> 1. Check permissions on the `.pem` file — must be 400: `chmod 400 key.pem`  
> 2. Ensure you're using the correct public IP  
> 3. Command used: `ssh -i "key.pem" ubuntu@<public-ip>`

✅ **Score:** `1 / 1`  
💬 Solid. Covered all practical checks.

**✅ Ideal Answer:**  
- `.pem` must have permission `chmod 400`  
- Command format: `ssh -i key.pem ubuntu@<PublicIP>`  
- Instance must be in **running** state  
- Port 22 must be open in the **Security Group**

---

### 4️⃣ S3 CLI upload fails using `aws s3 cp file.txt s3://mybucket/` — possible causes?

**🧠 Your Answer:**  
> 1. Check if the source file `file.txt` exists.  
> 2. Confirm IAM user has write permission (`s3:PutObject`).  
> 3. Review bucket policy and ACLs.  
> 4. Confirm bucket allows public or authorized writes if needed.

✅ **Score:** `1 / 1`  
💬 Clear, correct, and comprehensive.

**✅ Ideal Answer:**  
- Check if the file path exists  
- IAM user must have `s3:PutObject` permission on the bucket  
- Bucket policy and ACLs must allow the action  
- CLI must be configured correctly with proper access/secret keys

---

### 5️⃣ Static website hosted via EC2 shows nothing. Why?

**🧠 Your Answer:**  
> 1. `/var/www/html/` must have `index.html`  
> 2. Apache should be installed using:  
>   `sudo apt update`  
>   `sudo apt install apache2 -y`  
> 3. Apache should be started and enabled:  
>   `sudo systemctl start apache2`  
>   `sudo systemctl enable apache2`  
> 4. Public IP should be correctly opened in browser with `http://<Public-IP>`

✅ **Score:** `1 / 1`  
💬 Excellent structure. Real-world helpful checklist.

**✅ Ideal Answer:**  
- Verify Apache is installed and running  
- Ensure `index.html` is present in `/var/www/html/`  
- Security Group must allow **port 80 (HTTP)**  
- Access via `http://<Public-IP>` should return the page

---

## 🧮 Final Score Summary

| Question | Max | Score | Comments |
|----------|-----|-------|----------|
| Q1       | 1   | 1     | Perfect  |
| Q2       | 1   | 0.5   | Missed BPA details |
| Q3       | 1   | 1     | Spot on |
| Q4       | 1   | 1     | Excellent |
| Q5       | 1   | 1     | Great structure |
| **Total**| **5** | **4.5 / 5** | Well done! |

---

## 🪞 Reflection

- ✅ IAM & EC2 flow feels intuitive now  
- 🟡 S3 permissions & policy handling needs 1 more revision  
- 💭 Felt confident thinking in real-time and applying concepts  
- 🧭 Learning Git, IAM, EC2, CLI from scratch has started building real confidence  
- 🎯 This is how cloud interviews will feel — apply and explain

---

## 🧰 Tip

> Don’t memorize — **understand patterns**, **read policies slowly**, and **use CLI to validate assumptions**.

---

