# 📜 Commands Reference – Week 01 (Days 01–07)

This file documents **all the CLI commands** used during Week 1 of my 120-day AWS journey, grouped by service/topic with one-line explanations.

---

## 🧑‍💻 SSH & Permissions


    chmod 400 key.pem
Set strict read-only permission on .pem key file for SSH to work.

    ssh -i "key.pem" ubuntu@<public-ip>
SSH into EC2 instance using .pem key.

    sudo adduser devopsuser
Add a new Linux user named devopsuser.

    sudo usermod -aG sudo devopsuser
Give devopsuser sudo/admin permissions.

    su - devopsuser
Switch to the new user session.

## 🖥️ AWS CLI – IAM, EC2, S3
### IAM

    aws configure
Configure AWS CLI with Access Key, Secret, Region, Output format.

    aws sts get-caller-identity
Verify current authenticated AWS identity.

### EC2

    aws ec2 start-instances --instance-ids <instance-id>
Start a stopped EC2 instance.

    aws ec2 stop-instances --instance-ids <instance-id>
Stop a running EC2 instance.

    aws ec2 allocate-address
Allocate a new Elastic IP (EIP).

    aws ec2 associate-address --instance-id <id> --allocation-id <alloc-id>
Associate EIP with a running EC2 instance.

    aws ec2 disassociate-address --association-id <assoc-id>
Remove EIP association from an instance.

    aws ec2 release-address --allocation-id <alloc-id>
Release unused EIP to avoid charges.

    aws ec2 describe-instances --query "Reservations[*].Instances[*].[InstanceId,PublicIpAddress]" --output table
List all EC2 instances with their public IPs.


### S3 – Bucket + Website Hosting

    aws s3api create-bucket --bucket <bucket-name> --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1
Create a bucket in Mumbai region.

    aws s3 website s3://<bucket-name>/ --index-document index.html
Enable static website hosting on a bucket (older method).

    aws s3 cp index.html s3://<bucket-name>
Upload index.html to the S3 bucket.

    aws s3api put-bucket-policy --bucket <bucket-name> --policy file://policy.json
Attach public read access policy to the bucket.

    aws s3api put-bucket-website --bucket <bucket-name> --website-configuration file://website-hosting-config.json
Enable website hosting using a JSON config.

    aws s3api get-bucket-policy --bucket <bucket-name>
Retrieve current bucket policy.
### 🔐 SSH Keygen (GitHub)

    ssh-keygen -t ed25519 -C "devendar.aws@gmail.com"
Generate SSH key pair (ED25519) for GitHub authentication.

    cat ~/.ssh/id_ed25519.pub
Display public key content (to copy to GitHub).

    eval "$(ssh-agent -s)"
Start the SSH agent in the background.

    ssh-add ~/.ssh/id_ed25519
Add your SSH private key to the agent.

    ssh -T git@github.com
Test connection to GitHub using SSH.

### 🧱 Git Basics via CLI

    git init
Initialize a new local Git repo.

    git remote add origin git@github.com:devendar-aws/aws-120days-journey.git
Add a remote pointing to your GitHub repo via SSH.

    git branch -M main
Rename current branch to main.

    git add .
Stage all changed files.

    git commit -m "Initial commit"
Commit changes with a message.

    git push -u origin main
Push code to GitHub main branch.

### 🐧 Linux & Apache Commands

    sudo apt update
Update package list in Ubuntu.

    sudo apt install apache2 -y
Install Apache web server.

    sudo systemctl start apache2
Start Apache service.

    sudo systemctl enable apache2
Enable Apache to auto-start on reboot.

    echo "<h1>Hello from EC2</h1>" | sudo tee /var/www/html/index.html
Replace Apache default page with a custom HTML.

    ls -l
List files with details.

    pwd
Print current working directory.

    cd ..
Move to parent directory.

    mv oldname newname
Rename a file or folder.

### 📦 GitHub Troubleshooting / Merging

    git pull origin main --allow-unrelated-histories
Fix push failure due to unrelated histories by merging.

    git status
Show current status of Git working directory.

    git log
View commit history.

### 🧪 Bonus: File Permissions

    ls -la
List all files with hidden files and permissions.

    chmod +x filename.sh
Make a file executable.

    > filename.txt
Empty a file without deleting it.
