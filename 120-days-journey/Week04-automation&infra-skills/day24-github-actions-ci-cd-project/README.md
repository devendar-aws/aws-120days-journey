# Day 24 - Project 06 – CI/CD Pipeline for Static Website (GitHub Actions + S3) (July 29, 2025)

## 📌 Project Objective
To automate the deployment of a static website to an S3 bucket using **GitHub Actions**, achieving zero manual steps and enabling continuous integration and delivery with every code commit.

---

## 🔧 Tech Stack Used
- **Frontend**: HTML, CSS
- **CI/CD**: GitHub Actions
- **Cloud Provider**: AWS S3
- **Secrets Management**: GitHub Secrets (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

---

## 🚀 Deployment Flow

```
graph TD
  A[Push Code to GitHub] --> B[GitHub Action Triggered]
  B --> C[Download repo code]
  C --> D[Install AWS CLI]
  D --> E[Configure AWS Credentials]
  E --> F[Sync files to S3 bucket]
  F --> G[Site Deployed 🎉]
```

---

## 🧠 What I Learned
- Creating `.github/workflows/deploy.yml` to define CI pipeline
- Using `aws s3 sync` to copy static files to S3 bucket
- Managing GitHub Secrets securely
- Debugging workflow errors via GitHub Actions logs
- Understanding CI/CD philosophy in real-world DevOps

---

## 📁 Folder Structure
```
main repo/  
│  
├── .github/  
│   └── workflows/  
│       └── deploy.yml  
├── projects  
│   └── project-bonus-ci-cd-with-github-actions/  
│       └── static-site/  
│       │   ├── index.html
│       │   ├── style.css  
│       ├── screenshots/  
│       ├── README.md
```
---

## ✅ Deployment Outcome
- All commits pushed to `main` trigger auto-deployment to S3
- No manual `aws s3 sync` needed anymore
- Verified successful website load from S3 URL

---

## 🧪 Testing
- ✔️ Made a change to HTML
- ✔️ Committed and pushed to GitHub
- ✔️ Observed GitHub Action running
- ✔️ Verified change live on S3-hosted site

---

## 🪪 Author

Devendar Nandaiahgari  
CI/CD Project · Day 24 of Sankalpa (July 29, 2025)  
Truthful · Clean · Job-Ready  

---
