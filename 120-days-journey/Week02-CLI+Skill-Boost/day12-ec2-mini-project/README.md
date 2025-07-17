# 📁 Day 12 – EC2 Mini Project: Portfolio Hosting on Apache

## 📌 Project Objective
Host a static portfolio website on an EC2 instance using Apache, and expose it to the internet using a public IP. This is a **Mini Project** for hands-on practice with EC2 basics and Apache web server configuration.

---

## 🛠️ Tech Stack
- **AWS EC2**
- **Amazon Linux 2**
- **Apache Web Server**
- **Static HTML Portfolio**

---

## 🧱 Project Architecture

[Local Git Bash/Terminal]  
|  
| SSH  
v  
[EC2 Instance (Amazon Linux 2)]  
|  
| Apache + HTML files  
v  
[Portfolio Website hosted via Public IP]  

---

## 🚀 Steps Followed

### 1. ✅ Launch EC2 Instance
- **AMI**: Amazon Linux 2
- **Instance Type**: t2.micro (Free tier)
- **Key Pair**: Reused or created new one
- **Security Group**:
  - Inbound Rules: HTTP (80), SSH (22) from your IP
- **User Data Script (for Apache setup + initial HTML)**:

      #!/bin/bash
      yum update -y
      yum install -y httpd
      systemctl start httpd
      systemctl enable httpd
      echo "<h1>Mini Portfolio Site</h1>" > /var/www/html/index.html

### 2. ✅ Connect to EC2
`ssh -i your-key.pem ec2-user@<your-ec2-public-ip>`

### 3. ✅ Replace Default HTML with Portfolio Files
- Used `nano` or uploaded files using `scp`
- Replaced `/var/www/html/index.html` with custom `index.html`
- Verify Permissions & Restart Apache
  - Make sure Apache can serve it:
    - `sudo chown apache:apache /var/www/html/index.html`
    - `sudo chmod 644 /var/www/html/index.html`
  - Then restart Apache:
    - `sudo systemctl restart httpd`

### 4. ✅ Access Your Portfolio Site
- In browser: `http://<your-ec2-public-ip>`
- If Apache is running and HTML is in place, your portfolio appears live.

## 🧪 Validation
- ✅ Apache running: sudo systemctl status httpd
- ✅ Index file exists: ls `/var/www/html/`
- ✅ Public IP opens website

## 🧠 Learnings
- User data script runs on first boot
- Apache must be enabled + started
- Port 80 must be open in Security Group
- Amazon Linux 2 uses yum package manager

## 🐞 Debug Notes (if any)
- Ensure correct permissions when editing `/var/www/html`
- Apache not starting? Check logs: `sudo journalctl -xe`
- Public IP not working? Verify SG and Apache status

## 📂 Files Used
- `index.html` – Your static site
- `userdata.sh` – Script to auto install Apache and deploy HTML
