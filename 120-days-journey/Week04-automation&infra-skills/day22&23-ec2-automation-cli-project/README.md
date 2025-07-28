# ✅ AWS Journey - Day 22: EC2 Automation Project (Backup + S3 Upload with Cron)

Today’s focus was on setting up a lightweight **automation system on an EC2 instance** that:
- Periodically backs up system logs using `journalctl`
- Uploads the logs to an S3 bucket every 6 hours
- Runs entirely through scheduled `cron` jobs

---

## 📍 Step-by-Step Breakdown

### 1. ✅ Launched EC2 Instance (CLI Practice Instance)
- AMI: **Amazon Linux 2023 (AL2023) 6.12**
- Instance Type: **t2.micro** (Free Tier)
- Name: `dev-amazon-linux-cli`
- SSH Access: Enabled (Port 22 open in SG)
- Key Pair Used: `dev-ec2.pem`

### 2. ✅ Connected via Local Bash (Not EC2 console)
```
ssh -i dev-ec2.pem ec2-user@<your-ec2-public-ip>
```

---

## 📝 Part 1: Log Backup Script (`backup.sh`)
### 🛠️ Script Creation

Created `backup.sh` using `nano`:  
```
#!/bin/bash
timestamp=$(date +"%Y-%m-%d_%H-%M")
mkdir -p ~/backup
sudo journalctl --since "5 minutes ago" > ~/backup/systemd_log_$timestamp.txt
```
### 🧪 Tested Script
```
chmod +x backup.sh
./backup.sh
```
### 🔍 Validated Commands

Checked absolute paths for cron usage:  
```
which sudo
which journalctl
```
---

## ⚙️ Part 2: Setup Cron for Log Backup
### ✅ Installed Cronie (Amazon Linux)
```
sudo dnf install cronie -y
```
### ✅ Enabled and Started `crond` service
```
sudo systemctl enable crond
sudo systemctl start crond
sudo systemctl status crond
```
### 🕒 Cron Entry

Initially:
```
*/2 * * * * /usr/bin/sudo /home/ec2-user/backup.sh >> /home/ec2-user/cron.log 2>&1
```
Later updated to (removed sudo for ec2-user simplicity): Since using inside ec2 and the backup.sh doesn't need sudo
```
*/2 * * * * /home/ec2-user/backup.sh >> /home/ec2-user/cron.log 2>&1
```
### 🧪 Cron Validation
```
crontab -e
crontab -l
ls ~/backup
cat ~/cron.log
```
### 🧠 Learnings:
- Cron jobs do not run when instance is stopped
- Once restarted, cron jobs auto-resume due to `crond` being enabled
- `tail -f` shows live log output in terminal

## 💡 Improved `backup.sh` (With Logging and Error Handling)
```
#!/bin/bash

DATE=/usr/bin/date
JOURNALCTL=/usr/bin/journalctl
timestamp=$($DATE '+%Y-%m-%d_%H-%M')
backup_file="/home/ec2-user/backup/systemd_log_${timestamp}.txt"

# Capture errors if any
{
  echo "[$($DATE)] Running journalctl..."
  $JOURNALCTL -xe > "$backup_file"
  echo "[$($DATE)] Done. File saved to $backup_file"
} || {
  echo "[$($DATE)] ERROR: journalctl failed"
}
```
### 📄 Log Output

All cron activity logged at:
```
cat ~/cron.log
```
---

## ☁️ Part 3: Automate Upload to S3 (`s3_upload.sh`)
### 📁 Bucket Used  
Used pre-existing CLI-created bucket: `dev-cli-bucket-01`

### 🛠️ Script Creation  
Created and saved via:
```
nano ~/s3_upload.sh
```
```
#!/bin/bash

# Folder to back up
SOURCE_DIR="$HOME/backup"

# Destination bucket
BUCKET_NAME="dev-cli-bucket-01"

# Timestamped folder in S3
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
S3_PATH="s3://${BUCKET_NAME}/backup_$TIMESTAMP"

# Upload using AWS CLI
aws s3 cp "$SOURCE_DIR" "$S3_PATH" --recursive

# Log result
if [ $? -eq 0 ]; then
  echo "$(date): Backup successful to $S3_PATH" >> ~/upload_log.txt
else
  echo "$(date): Backup failed" >> ~/upload_log.txt
fi
```

### 🧪 Permissions and Testing
```
chmod +x ~/s3_upload.sh
~/s3_upload.sh
```
### 🪪 Resolved: “Unable to locate credentials”
- Attached IAM Role with AmazonS3FullAccess to EC2 instance
- Then tested script again ✅

### 🕒 S3 Upload Cron Setup
```
0 */6 * * * /home/ec2-user/s3_upload.sh
```
### 🧾 Upload Log

Check S3 success/failure logs here:
```
cat ~/upload_log.txt
```
### 📦 Outputs
- `/home/ec2-user/backup/`: Periodic log backups
- `~/cron.log`: Cron job activity logs
- `~/upload_log.txt`: S3 upload logs
- `s3://dev-cli-bucket-01/backup_<timestamp>/`: Uploaded logs

### ✅ Key Learnings Today
- Creating and managing EC2 via CLI
- Writing and debugging shell scripts (`.sh`)
- Cron scheduling and logging
- Using `journalctl` with timestamps
- Absolute paths in cron context
- IAM Role attachment for S3 access
- Automation pipeline: EC2 → Cron → Backup → S3
