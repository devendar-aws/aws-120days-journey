## 📇 IAM Flashcards

| Concept | Answer |
|--------|--------|
| What is IAM? | AWS Identity and Access Management |
| Main use of IAM | Securely control access to AWS resources |
| IAM resource types | Users, Groups, Roles, Policies |
| What is an IAM user? | Individual identity with credentials |
| What is an IAM role? | Temporary access with assumed identity |
| What is a policy? | JSON document that defines permissions |
| Default user permissions? | None; must be explicitly granted |
| Root user should be used? | Only for initial setup or emergencies |
| Best practice for IAM? | Least privilege, MFA, use roles |
| Where are IAM logs visible? | AWS CloudTrail |

---

## 📇 S3 Flashcards

| Concept | Answer |
|--------|--------|
| What is S3? | Scalable object storage service |
| S3 stands for? | Simple Storage Service |
| What is a bucket? | A container for storing objects |
| Max file size for upload (single PUT)? | 5 GB |
| How to upload files > 5GB? | Use Multipart Upload |
| Are buckets region-specific? | Yes |
| Default bucket access? | Private |
| How to make a static site? | Enable static hosting + public policy |
| What is an object? | File stored in a bucket with metadata |
| Versioning in S3? | Keeps multiple versions of the same object |

---

## 📇 EC2 Flashcards

| Concept | Answer |
|--------|--------|
| What is EC2? | Virtual server in the cloud |
| AMI stands for? | Amazon Machine Image |
| Instance Types | General (t2, t3), Compute (c5), Memory (r5) etc. |
| What is a key pair? | Used for SSH access (private + public key) |
| Default EC2 port for web server? | Port 80 (HTTP) or 443 (HTTPS) |
| How to access EC2? | Use SSH with `.pem` file |
| What is a Security Group? | Virtual firewall for EC2 |
| What is a VPC? | Virtual Private Cloud – network for EC2 |
| Billing granularity? | Per second (Linux), per hour (Windows) |
| Free Tier EC2 usage? | 750 hours/month (t2.micro or t3.micro) |

---

### 📇 Lambda Basics Flashcards

| Concept | Answer |
|--------|--------|
| What is AWS Lambda? | Serverless compute service that runs code on demand |
| Default handler function name? | `lambda_handler` |
| Input format to Lambda? | `event` (JSON), `context` (runtime info) |
| Where are logs stored? | Amazon CloudWatch |
| How to access a key in `event`? | `event.get("key")` | `event.items()`
| Is Lambda free in Free Tier? | Yes, 1M requests + 400,000 GB-seconds per month |
