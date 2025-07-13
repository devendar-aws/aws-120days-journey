## 🏛️ Devendar’s Full AWS Architecture (7-Layer View)

📦 From Global Infra to Monitoring — all stitched together in one clear diagram.

### Layer 1: 🌐 Global Infrastructure
    ┌─────────────────────────────────────────────┐
    │         AWS Global Infra (Region + AZs)     │
    │   - Region: ap-south-1                      │
    │   - AZs: ap-south-1a, 1b, 1c                │
    └─────────────────────────────────────────────┘

### Layer 2: 🕸️ Networking
    ┌──────────────────────────────────────────────────────────────┐
    │                         VPC (10.0.0.0/16)                    │
    │ ┌──────────────┐    ┌──────────────┐     ┌──────────────┐    │
    │ │Public Subnet │    │Private Subnet│     │Route Tables  │    │
    │ │10.0.1.0/24   │    │10.0.2.0/24   │     │+ IGW / NAT GW│    │
    │ └──────┬───────┘    └──────┬───────┘     └────┬─────────┘    │
    │        │ EC2 Web           │ RDS / Lambda     │              │
    └────────▼───────────────────▼──────────────────▼──────────────┘

### Layer 3: ⚙️ Compute
    ┌──────────────────────────────────────────────────────────────┐
    │ EC2 Instance (Web App)      Lambda Function (Serverless Task)│
    │ ┌──────────────┐           ┌──────────────────────────────┐  │
    │ │ Apache/Nginx │           │ S3 Event → Lambda → DynamoDB │  │
    │ └─────┬────────┘           └──────────────────────────────┘  │
    │       │                      IAM Role with Permissions       │
    └───────▼──────────────────────────────────────────────────────┘

### Layer 4: 💾 Storage
    ┌──────────────────────────────────────────────────────────────┐
    │ S3 Bucket (Static Assets)   EBS (Attached to EC2)            │
    │ S3 Hosting + Public Access  EFS (Optional for multi-EC2)     │
    └──────────────────────────────────────────────────────────────┘

### Layer 5: 🔐 Identity & Access Management
    ┌──────────────────────────────────────────────────────────────┐
    │ IAM Users, Roles, Policies                                   │
    │ - Role: EC2 → S3 Access                                      │
    │ - Role: Lambda → DynamoDB                                    │
    │ - MFA, Least Privilege, Inline vs Managed                    │
    └──────────────────────────────────────────────────────────────┘

### Layer 6: 🧠 Automation & Control
    ┌──────────────────────────────────────────────────────────────┐
    │ AWS CLI, SDK (boto3), GitHub Actions                         │
    │ EC2 User Data scripts (bootstrapping)                        │
    │ Infra as Code (CloudFormation / Terraform / YAML files)      │
    └──────────────────────────────────────────────────────────────┘

### Layer 7: 📊 Monitoring & Cost
    ┌──────────────────────────────────────────────────────────────┐
    │ CloudWatch: Logs, Metrics, Alarms                            │
    │ CloudTrail: Auditing, API Access History                     │
    │ Budgets + Cost Explorer: ₹ Tracking & Optimization           │
    └──────────────────────────────────────────────────────────────┘
