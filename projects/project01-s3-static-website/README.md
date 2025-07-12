# 📦 Project 1: AWS S3 Static Website Hosting with IAM & CLI Automation

## 🧠 Problem Statement
Organizations need a simple, cost-effective, and scalable way to host static websites (e.g., marketing pages, documentation, portfolios) without managing servers.

## 🎯 Business Objective
Deploy a secure and publicly accessible static website on AWS using S3, IAM, and CLI tools — automating as much as possible for repeatable and scalable setup.

---

## ⚙️ Project Objective
Build and deploy a static HTML website on S3 using IAM permissions and AWS CLI, while applying security best practices and demonstrating automation.

---

## 🧰 Tools & Services Used
- **Amazon S3** – Website Hosting
- **IAM** – User + Permissions for CLI access
- **AWS CLI** – Full automation (bucket creation, policy, upload)
- **HTML** – Sample webpage
- **Public Bucket Policy** – Controlled access
- **Bucket Versioning & Encryption** – Default config

---

## 📌 Key Deliverables
- S3 Bucket (region: `ap-south-1`) with unique name.
- Public read permissions applied via bucket policy.
- Static HTML page deployed to the bucket.
- Website accessible via **S3 endpoint URL**.
- Commands and steps documented clearly.
- Screenshots showing live website.

---

## 🚀 Steps Performed

### 1️⃣ Create S3 Bucket

    aws s3api create-bucket \
      --bucket devendar-static-site \
      --region ap-south-1 \
      --create-bucket-configuration LocationConstraint=ap-south-1

### 2️⃣ Enable Static Website Hosting (CLI or Console)

    {
      "IndexDocument": {
      "Suffix": "index.html"
      },
      "ErrorDocument": {
      "Key": "error.html"
     }
    }

### 3️⃣ Add Bucket Policy (Public Read)

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "PublicReadGetObject",
          "Effect": "Allow",
          "Principal": "*",
          "Action": "s3:GetObject",
          "Resource": "arn:aws:s3:::devendar-static-site/*"
        }
      ]
    }

### 4️⃣ Upload Website Files

    aws s3 cp index.html s3://devendar-static-site/

    Index.html

    <html>
      <head>
        <title>Dev's S3 Static Site</title>
      </head>
      <body style="text-align:center; padding-top:50px;">
        <h1>Welcome to AWS 120days Journey _/\_</h1>
        <p>This website is hosted on AWS S3 via CLI as part of my 120-Day Journey</p>
      </body>
    </html>

### 5️⃣ Access Website

- [AWS S3Static Website](http://devendar-static-site.s3-website.ap-south-1.amazonaws.com)

### ✅ Success Criteria (KPIs)

Site loads via public S3 endpoint

Secure bucket policy (public read only)

No server required

IAM + CLI access worked

Clean documentation and screenshots

### 📸 Screenshots

✅ S3 bucket settings

✅ Bucket policy

✅ Static website live URL

### 🧘 Reflections

This project helped me understand how S3 is used for static hosting and how IAM permissions and CLI automation can reduce manual effort. It was my first end-to-end deployment without any fake setup — a real confidence booster.
