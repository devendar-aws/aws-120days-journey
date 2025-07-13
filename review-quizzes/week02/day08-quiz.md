🧠 Day 8 Mini Assessment – 10 MCQs

These are certification-style, based only on what you’ve learned till now (IAM, EC2, S3, Git, CLI, Apache, EIP).
💡 Instructions:

    Choose A/B/C/D for each.

    Answer one by one or all at once — your choice.

1. Which AWS service is GLOBAL in scope?
A. S3
B. EC2
C. `IAM`
D. VPC

2. What command is used to view the current IAM identity in AWS CLI?
A. aws iam list-users
B. aws ec2 describe-instances
C. `aws sts get-caller-identity`
D. aws s3 ls

3. What does chmod 400 key.pem ensure?
A. The file is deleted after use
B. Only root can access the file
C. `Only the file owner can read it`
D. It disables the key file

4. What is the correct sequence to host a static website on S3 (via CLI)?
A. Create bucket → Set ACL → Upload → Add CloudFront
B. `Create bucket → Upload files → Enable Static Website → Set Bucket Policy`
C. Create bucket → Enable versioning → Upload → Set IAM policy
D. Upload files → Enable Logging → Add public read access

5. Elastic IP is useful when...
A. You want to block internet access
B. You want a new IP every reboot
C. `You want a persistent static IP`
D. You want to save cost by stopping the instance

6. Which Linux command updates the package index?
A. sudo apt install
B. apt-get upgrade
C. `sudo apt update`
D. yum install update

7. You get Permission denied (publickey) error while SSHing. Likely cause?
A. Apache not installed
B. Port 80 is closed
C. `Wrong or missing key file`
D. S3 bucket is private

8. Git command to initialize a new repo in the folder:
A. git start
B. `git init`
C. git create
D. git repo-new

9. What happens when you run git add .?
A. Commits all files
B. Deletes everything
C. `Stages all changes for commit`
D. Pushes code to GitHub

10. What is the correct command to check Apache service status?
A. apachectl list
B. `systemctl status apache2`
C. sudo apache-check
D. httpd --status


# 📘 Week 01 – Review Quiz & Answers

This file captures the 10-question review quiz at the end of Week 01 to help reinforce key AWS concepts, CLI commands, Git basics, and real-world troubleshooting.

---

## ✅ Quiz Results

| Q# | Question Focus | Your Answer | Correct Answer | ✅/❌ | Notes |
|----|----------------|-------------|----------------|------|-------|
| 1  | IAM global/regional? | C | **C** | ✅ | IAM is a **global** service (not regional like EC2/S3). |
| 2  | Identity check via CLI | C | **C** | ✅ | `aws sts get-caller-identity` confirms CLI identity. |
| 3  | Key permissions for SSH | C | **C** | ✅ | `chmod 400` ensures `.pem` key security. |
| 4  | S3 static website steps | B | **B** | ✅ | Correct order: bucket → upload → enable hosting → bucket policy. |
| 5  | Purpose of Elastic IP | C | **C** | ✅ | Static public IP persists across reboots. |
| 6  | Update packages on EC2 | C | **C** | ✅ | `sudo apt update` refreshes package lists on Ubuntu. |
| 7  | SSH auth failure reason | C | **C** | ✅ | SSH key mismatch or absence is common issue. |
| 8  | Start Git locally | B | **B** | ✅ | `git init` initializes a Git repo in current directory. |
| 9  | Stage all files for commit | C | **C** | ✅ | `git add .` stages all modified/created files. |
| 10 | Check Apache status | B | **B** | ✅ | `systemctl status apache2` checks Apache service health. |

---

## 🏁 Final Score: **10/10**

🎉 Perfect score! Your retention of Week 01 concepts is excellent — you're well-aligned for AWS certification and interviews.

---

### 📌 Concepts Reviewed
- IAM vs regional services
- S3 static website configuration steps
- EC2 SSH key security
- Elastic IP lifecycle
- Apache setup and verification
- Git basics: init, add, commit, branch
- CLI commands: `chmod`, `systemctl`, `aws sts`, `apt update`

---

🔁 **Tip**: Use this file for quick revision before assessments or interviews. More quizzes coming weekly!

