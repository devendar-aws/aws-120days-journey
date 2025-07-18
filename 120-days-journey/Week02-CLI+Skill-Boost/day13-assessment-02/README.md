# 🧠 Day 13 – AWS CLI Mastery & EC2 Deep Dive (July 18, 2025)

Today we focused on mastering the AWS Command Line Interface (CLI) and explored advanced querying with EC2, IAM Roles, and metadata.

---

## ✅ Topics Covered

### 🔹 AWS CLI Essentials
- `aws configure` with Access Key, Secret, Region, Output
- Syntax structure: `aws <service> <command> --flags`

### 🔹 EC2 with CLI
- `aws ec2 describe-instances`
- Fetching: Instance ID, Public IP, State, Tags
- Using `--query` and `--filters` to refine output
- Format outputs as `text`, `table`, or `json`

### 🔹 Instance Metadata
- IP `169.254.169.254` to fetch metadata from inside instance
- Only accessible within the EC2 instance
- Used to get IAM role, instance ID, region, IP, etc.

### 🔹 IAM vs IAM Role
| IAM User         | IAM Role                          |
|------------------|------------------------------------|
| Used by humans   | Used by AWS services               |
| Has credentials  | No credentials, assumed by EC2     |
| Full access keys | Fine-grained permission control    |

### 🔹 Practice Tasks
- ✅ Find Public IP using Tag Name
- ✅ Get Volume ID using Instance State filter

---

## 🧠 Interview & Cert Tips
- Use `--query` with dot notation for nested values
- IAM Role doesn't require access keys
- Metadata IP is same across all instances (non-routable)
- Use `--output table` for readable CLI output
- Describe-instances is the most used CLI command in EC2

---

