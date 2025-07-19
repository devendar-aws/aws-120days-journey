# 🚀 EC2 (Elastic Compute Cloud) – Learning Summary by Devendar Nandaiahgari

## 🔹 Introduction

Amazon EC2 (Elastic Compute Cloud) is the foundational compute service in AWS that allows users to launch and manage virtual servers on demand. This document summarizes my learnings, experience, and key takeaways from working hands-on with EC2 in real-world projects.

---

## ✅ Key Concepts I Learned

- **EC2 Basics**:
  - What is EC2 and how it's different from physical servers
  - AMI (Amazon Machine Image) and its importance
  - Instance types (T2, T3, M5, etc.) and use cases

- **Launch Process**:
  - Selecting AMI, instance type, key pair, security groups, and storage
  - Role of user data in automation (bootstrapping)
  - How to SSH into EC2 using Git Bash or Terminal

- **Security Groups & Key Pairs**:
  - Inbound/Outbound rules for enabling HTTP/HTTPS/SSH
  - Generating and using `.pem` key securely

- **Instance Lifecycle Management**:
  - Start, Stop, Reboot, Terminate
  - Elastic IP and Public/Private IP behavior
  - What happens to data in instance-store vs EBS-backed volumes

- **Pricing Model**:
  - On-Demand, Reserved, Spot, and Savings Plans
  - Use of `t2.micro` for Free Tier experiments

---

## 💼 Projects I Applied EC2 In

### 🔸 Project: Hosting a Static Portfolio Site on EC2
- **Use Case**: Needed more control than S3 static hosting
- **Stack**: EC2 (Amazon Linux 2), Apache, GitHub
- **Steps I Took**:
  - Launched EC2 instance using Free Tier (t2.micro)
  - Used user-data script to install Apache and deploy site on boot
  - Configured security group to allow HTTP traffic
  - Synced GitHub repo with Apache's `/var/www/html` directory
  - Automated future site changes via Git pull
- **Outcome**: Website was live, resilient, and low-cost

---

## 🔧 Common Errors I Solved

- **Permission denied (publickey)** while SSH → Fixed by checking `.pem` file permissions (`chmod 400`)
- **Website not loading** → Enabled port 80 in Security Group
- **Changes not reflecting** → Synced with GitHub and restarted Apache

---

## 🧠 My Personal Takeaways

- EC2 gives total control over the OS and software stack
- IAM Roles can securely give access to S3/CloudWatch without hardcoding credentials
- Every instance should be tagged well for cost tracking
- Security groups act as virtual firewalls — must be configured carefully
- User data can automate 80% of launch tasks

---

## 🛠️ Tools & Commands Practiced

| Tool/Command        | Purpose                            |
|---------------------|------------------------------------|
| `ssh -i key.pem`    | Connect to EC2 instance            |
| `sudo yum install`  | Install packages on Amazon Linux   |
| `chmod 400 key.pem` | Secure the private key             |
| `sudo systemctl`    | Start/stop Apache                  |
| AWS Console         | Launch/manage instance             |
| IAM Role + EC2      | Give temporary permissions         |
| Metadata URL        | Access instance metadata via IMDS  |

---

## 📚 What’s Next

- Set up **EC2 Auto Scaling** and **Load Balancer**
- Use **CloudWatch** to monitor EC2 instance health
- Try **Spot Instances** for cost efficiency
- Learn how to use **CloudFormation/Terraform** to provision EC2 instances via code

---

> 🔖 *"EC2 taught me how to think like an infrastructure engineer — balancing cost, security, and performance while staying agile."*

---

🧑‍💻 Prepared by: **Devendar Nandaiahgari**  
🗓️ Date: July 2025  
