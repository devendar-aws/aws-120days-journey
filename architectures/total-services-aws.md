## 🧱 Visual Snapshot of Skill Pyramid

            🏔️ High-Level Projects + Design
               ───────────────────────────
          ☁️ Lambda | CI/CD | Monitoring | RDS
               ───────────────────────────
          🧱 Subnet | VPC | IAM Roles | EC2 + S3
               ───────────────────────────
          ⚙️ AWS CLI | GitHub | SSH | Policies
               ───────────────────────────
            🎓 Core Theory + Real Projects




## 🧱 Level 1: Core Services
| Domain | Service | Purpose |
|--------|---------|---------|
| Compute | EC2 | Virtual server to host apps |
| Storage | S3 | Object storage, static site hosting|
| Identity | IAM | Users, roles, policies, permissions |
| Networking | VPC | Isolated network (like your own datacenter) |
| CLI & SDK | AWS CLI | Interact with all services via terminal |

---

## 🔁 Level 2: Core Support Services
| Domain | Service | Why It’s Important |
|--------|---------|--------------------|
| Security | Security Groups | Control EC2 traffic (like firewalls) |
| Networking | Internet Gateway (IGW) | Allows EC2 in public subnet to access internet |
| Networking | Elastic IP (EIP) | Static IP for EC2 |
| Networking | Route Table | Controls outbound routing for VPC/subnet |
| Storage | EBS | Persistent block storage for EC2|
| Monitoring | CloudWatch | Logs, metrics, alarms, dashboards |
| Automation | User Data / Scripts | Bootstrap EC2 instances on launch |
| Access Mgmt | Key Pairs | SSH into EC2 securely |

---

### 🚀 Level 3: Real-World Tools (For Projects, Resume, 18 LPA)

| Use Case         | Service                                   | Description                                  |
|------------------|-------------------------------------------|----------------------------------------------|
| Automation       | **Lambda**                                | Serverless functions for triggers, jobs      |
| Analytics        | **Athena + Glue**                         | Query S3 data, ETL pipelines                 |
| DevOps           | **CodePipeline, CodeDeploy, GitHub Actions** | CI/CD for automated deployment pipelines     |
| DNS + Hosting    | **Route 53**                              | Domain routing, custom domain mapping        |
| Architecture     | **Load Balancer (ALB)**                   | Distribute traffic to multiple EC2s          |
| Scaling          | **Auto Scaling Groups**                   | Scale EC2 instances based on demand          |
| Database         | **RDS or DynamoDB**                       | Relational or NoSQL managed databases        |
| Observability    | **CloudTrail**                            | Track user/API activity across AWS           |
| Cost Management  | **Budgets, Cost Explorer**                | Monitor and optimize AWS spend               |






            
