# 📅 Day 2 – IAM & EC2 Basics

**Date:** July 7, 2025  
**Theme:** Secure AWS Access & Launch First EC2 Instance

---

## ✅ What I Did Today

### 🔐 IAM Setup (Identity and Access Management)
- Created a dedicated IAM user: `awscli-user`
- Enabled **programmatic** and **console access**
- Assigned **AdministratorAccess** policy for now  
  > 🔸 *Note: This is temporary for setup. I will refine permissions to least-privilege roles in coming days.*
- Configured **MFA (Multi-Factor Authentication)**
- Created and stored **Access Key ID** and **Secret Access Key**

### 💻 AWS CLI Configuration
- Used `aws configure` to:
  - Input access keys
  - Set default region: `ap-south-1`
  - Set output format: `json`
- Verified connection with:
  ```bash
  aws sts get-caller-identity

🖥️ EC2 Instance Setup (Free Tier)

    Launched a t2.micro Ubuntu EC2 instance (Free Tier eligible)

    Created and downloaded PEM key pair: dev-ec2.pem

    Allowed port 22 (SSH) in the security group

    Connected from local machine using:

    ssh -i "EC2 Keys/dev-ec2.pem" ubuntu@<Public-IP>

🔍 SSH Login Confirmed

    Prompt appeared:

    ubuntu@ip-172-31-XX-XXX:~$

💡 Reflections

    IAM user with AdminAccess is powerful — but needs to be secured later

    SSH login worked after handling correct key path and permissions

    Learned about key pairs, public IPs, and secure EC2 access

    CLI is very intuitive once configured properly

📸 Screenshots & Files

    ✅ IAM User setup (MFA screen)

    ✅ EC2 Dashboard (running instance)

    ✅ SSH terminal proof

    🔒 PEM key stored locally (not shared)

🧠 Key Commands Used

- aws configure
- aws sts get-caller-identity
- ssh -i "dev-ec2.pem" ubuntu@<Public-IP>

🟢 Next Up: Day 3 – S3 Static Website Hosting

Tomorrow, I’ll host my first public static website on S3 — using both the console and CLI. Time to build something real! 🚀
