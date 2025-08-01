## ✅ Day 22&23 Checklist - EC2 Automation (July 28, 2025)

| Task | Status |
|------|--------|
| Launched EC2 (Amazon Linux, t2.micro) | ✅ |
| Connected via SSH using local bash | ✅ |
| Created `backup.sh` script for systemd logs | ✅ |
| Installed `cronie`, enabled `crond` | ✅ |
| Added cron job to run `backup.sh` every 2 mins | ✅ |
| Improved script with logging, error handling | ✅ |
| Verified cron logs, understood `tail -f` | ✅ |
| Created and tested `s3_upload.sh` | ✅ |
| Attached IAM role for S3 access | ✅ |
| Setup cron to upload to S3 every 6 hrs | ✅ |
| Verified upload logs and S3 success | ✅ |

🧠 **Learning Level Today**: 🔥 Deep Practical Cron + Scripting + S3 Automation

---

## ✅ CI/CD Project – Task Checklist (Day 24)

| #  | Task Description                                      | Status |
|----|--------------------------------------------------------|--------|
| 1  | Create `index.html` and `style.css`                    | ✅     |
| 2  | Create S3 bucket and configure static website hosting  | ✅     |
| 3  | Create `.github/workflows/deploy.yml` GitHub Action    | ✅     |
| 4  | Add GitHub Secrets for AWS credentials                 | ✅     |
| 5  | Configure workflow: install AWS CLI + sync to S3       | ✅     |
| 6  | Push code to GitHub and trigger deployment             | ✅     |
| 7  | Debug and fix any deployment errors                    | ✅     |
| 8  | Confirm deployment live on S3 URL                      | ✅     |
| 9  | Write detailed README.md with diagram + learnings      | ✅     |
| 10 | Create cheat sheet for CI/CD                           | ✅     |
| 11 | Push to GitHub repo `ci-cd-s3-project`                 | ✅     |
| 12 | Add badges or further improvements                     | ✅     |

> 🧘‍♂️ Done with truth, clarity, and calm.

---

## ✅ Day 25 Checklist — Linux Admin Basics

| #   | Task                                                                 | Status  |
|-----|----------------------------------------------------------------------|---------|
| 1   | Launched EC2 Instance (Ubuntu)                                       | ✅ Done  |
| 2   | Connected via SSH                                                    | ✅ Done  |
| 3   | Created new Linux user                                               | ✅ Done  |
| 4   | Created a new group                                                  | ✅ Done  |
| 5   | Added user to the group                                              | ✅ Done  |
| 6   | Verified user and group list (`cat /etc/passwd`, `cat /etc/group`)  | ✅ Done  |
| 7   | Created a file with specific permissions using `chmod`              | ✅ Done  |
| 8   | Changed file ownership with `chown` and `chgrp`                      | ✅ Done  |
| 9   | Verified permission changes using `ls -l`                            | ✅ Done  |
| 10  | Installed and started `nginx` using `systemctl`                      | ✅ Done  |
| 11  | Checked service status with `systemctl status nginx`                | ✅ Done  |
| 12  | Verified port 80 listening (`sudo ss -tuln | grep :80`)             | ✅ Done  |
| 13  | Opened port 80 in Security Group (SG)                                | ✅ Done  |
| 14  | Accessed NGINX welcome page via public IP                            | ✅ Done  |
| 15  | Understood difference between HTTP and HTTPS                         | ✅ Done  |
| 16  | Discussed static hosting: EC2 vs S3                                  | ✅ Done  |
| 17  | Learned how to check boot services using `systemctl is-enabled`     | ✅ Done  |
| 18  | Clarified instance billing: stopped vs terminated                    | ✅ Done  |

---

## ✅ Day 26 – Checklist (July 30, 2025)

## 🧠 Goal: IAM Role-Based & Group-Based Access Control – Hands-On via AWS CLI and Console

| Task No. | Task                                                                 | Status |
|----------|----------------------------------------------------------------------|--------|
| 1        | Create IAM users `devuser` and `audituser` via CLI                  | ✅     |
| 2        | Set login access and password with reset requirement                | ✅     |
| 3        | Create IAM groups: `devgroup` and `auditgroup`                      | ✅     |
| 4        | Attach AWS managed policy `AmazonEC2FullAccess` to `devgroup`       | ✅     |
| 5        | Create custom policy `IAMReadOnlyCustomPolicy` (IAM-only access)    | ✅     |
| 6        | Attach custom policy to `auditgroup`                                | ✅     |
| 7        | Add users to their respective groups (`devuser`, `audituser`)       | ✅     |
| 8        | Log in to AWS Console as `devuser` and `audituser` and verify roles| ✅     |
| 9        | Confirm that group permissions work as expected                     | ✅     |
| 10       | Detach policies and remove users from groups                        | ✅     |
| 11       | Delete users, groups, and custom policy                             | ✅     |
| 12       | Document all steps and commands in `README.md`                      | ✅     |

---

## ✅ Day 27 Checklist — August 1, 2025

## 📌 Theme: Review + Assessment 04 (Cron, Linux Permissions, CI/CD)

| No. | Task Description                                  | Status     |
|-----|--------------------------------------------------|------------|
| 1   | Cron Quiz (9 questions)                          | ✅ Done     |
| 2   | Linux File Permissions Quiz (10 questions)       | ✅ Done     |
| 3   | Bonus Mixed Quiz (5 challenging questions)       | ✅ Done     |
| 4   | CI/CD Quiz (10 questions)                        | ✅ Done     |
| 5   | Review answers + explanations                    | ✅ Done     |
| 6   | Honest scoring and tracking                      | ✅ Done     |
| 7   | Generate `assessment04.md` with answers & score  | ✅ Done     |
| 8   | Generate `checklist.md` with task table          | ✅ Done     |
| 9   | Push changes to GitHub repo                      | ✅ Done     |
| 10  | Maintain 100% focus & honesty                    | ✅ Done     |

---
