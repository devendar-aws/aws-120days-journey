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

