## 🧱 LAYER 1: Global Infrastructure

    ┌────────────────────────────────────────────────────┐
    |🌍 Internet                                         |
    |      │                                             |
    |      ▼                                             |
    |🌐 AWS Global Network (Edge Locations + Regions)    |
    |  └── 📍 Region (e.g., ap-south-1)                  |
    |       └── 🗃️ Availability Zones (AZs: isolated DCs)|
    └────────────────────────────────────────────────────┘

## 🌐 LAYER 2: Networking – VPC, Subnets, Routing

    ┌────────────────────────────────────────────────────┐
    │                 VPC (Your Private Network)         │
    │ ┌─────────────┐   ┌─────────────┐   ┌────────────┐ │
    │ │ PublicSubnet│   │PrivateSubnet│   │NAT Gateway │ │
    │ │   (IGW)     │   │  (No IGW)   │   │(Optional)  │ │
    │ └────┬────────┘   └────┬────────┘   └────┬───────┘ │
    │      ▼                 ▼                 ▼         │
    │   EC2 (Web App)     EC2 (DB Server)    Route Table │
    │   SG: Allow 22, 80  SG: Allow only 3306│ IGW/NAT   │
    └────────────────────────────────────────────────────┘

## 💻 LAYER 3: Compute Layer

    ┌─────────────────────────────────────────────────────────────────────┐
    |                                                                     |
    |         ┌────────────┐         ┌────────────┐                       |
    |         │   EC2      │         │  Lambda    │                       |
    |         │(Web Server)│         │(Serverless)│                       |
    |         └────┬───────┘         └─────┬──────┘                       |
    |              ▼                       ▼                              |
    |      Auto Scaling Group        Triggered by events (S3, API, etc.)  |
    |              │                                                      |
    |              ▼                                                      |
    |    Load Balancer (ALB/NLB)                                          |
    └─────────────────────────────────────────────────────────────────────┘

## 📦 LAYER 4: Storage Layer

    ┌─────────────────────────────────────────────────────────────────────┐
    | ┌──────────────┐         ┌──────────────┐        ┌──────────────┐   |
    | │   S3 Bucket  │◄───────►│Static Hosting│        │ Object Files │   |
    | └──────┬───────┘         └──────┬───────┘        └──────┬───────┘   |
    |        ▼                        ▼                       ▼           |
    |  Website Hosting       Public File Access         Logs / Backups    |
    |                                                                     |
    | ┌────────────┐                                                      |
    | │    EBS     │ ← Attached to EC2                                    |
    | └────────────┘                                                      |
    |                                                                     |
    | ┌────────────┐                                                      |
    │ |    EFS     │ ← Shared file system across EC2                      |
    | └────────────┘                                                      |
    └─────────────────────────────────────────────────────────────────────┘

## 🔐 LAYER 5: Identity and Access Management

    ┌────────────────────────────┐
    │         IAM                │
    │ ┌──────┐ ┌──────┐ ┌──────┐ │
    │ │User  │ │Group │ │Role  │ │
    │ └──┬───┘ └──┬───┘ └──┬───┘ │
    │    ▼        ▼        ▼     │
    │  Policies (Allow/Deny)     │
    └────────────────────────────┘

## 📡 LAYER 6: Access & Automation

    ┌────────────────────────────────────────────┐
    | ┌────────────┐        ┌──────────────┐     |
    | │  AWS CLI   │        │ SDK (Python) │     |
    | └────┬───────┘        └──────┬───────┘     |
    |      ▼                       ▼             |
    | Terminal Commands     Automate via Boto3   |
    |                                            |
    | ┌────────────┐        ┌─────────────────┐  |
    │ | User Data  │        │  CloudFormation │  |
    │ | (EC2 Init) │        │ Infra as Code   │  |
    | └────────────┘        └─────────────────┘  |
    └────────────────────────────────────────────┘

## 📊 LAYER 7: Monitoring, Logging & Billing

    ┌────────────────────────────────────────────┐
    |   ┌────────────┐                           |
    │   | CloudWatch │ ← Logs, Metrics, Alarms   |
    |   └────┬───────┘                           |
    |        ▼                                   |
    | Log EC2, Lambda, S3                        |
    |                                            |
    | ┌──────────────┐                           |
    | │ CloudTrail   │ ← Who did what in AWS     |
    | └──────────────┘                           |
    |                                            |
    | ┌──────────────┐                           |
    | │ Cost Explorer│ ← Billing Analysis        |
    | └──────────────┘                           |
    └────────────────────────────────────────────┘

## 🎯 Full Flow
    ┌───────────────────────────────────────────────────────────────────────────────┐
    |User → Route 53 (DNS) → Load Balancer (ALB) → EC2 (Public Subnet)              |
    |                                            → S3 (Static Assets)               |
    |                                            → RDS (in Private Subnet)          |
    |                                            → Logs to CloudWatch               |
    |                                            → IAM Role allows access to S3     |
    |                                            → Lambda handles async processing  |
    └───────────────────────────────────────────────────────────────────────────────┘



## ✅ Devendar’s Mental Stack (Suggested Layers)

|----------------------------------------------------------------------|
| Level 0 | AWS Global Infra (Region, AZ, Edge)                        |
| Level 1 | Networking (VPC, Subnets, NAT, IGW)                        |
| Level 2 | IAM & Security (Users, Roles, SGs, KMS)                    |
| Level 3 | Compute & Storage (EC2, S3, EBS, EFS)                      |
| Level 4 | Automation & DevOps (Lambda, CodePipeline, GitHub Actions) |
| Level 5 | Observability & Cost (CloudWatch, Trail, Budgets)          |
| Level 6 | Real-World Project Services (Athena, Glue, RDS, Route 53)  |
| Level 7 | Data & AI (Bonus: SageMaker, Redshift, etc.)               |
|----------------------------------------------------------------------|
