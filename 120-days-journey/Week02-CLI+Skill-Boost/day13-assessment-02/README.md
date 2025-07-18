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

## ✅ Core Learning Objectives

| Topic                         | Task Description                                           | Done? |
|------------------------------|------------------------------------------------------------|-------|
| AWS CLI                      | Understand `aws configure` flow (access key, region, etc.) | ✅     |
| EC2 CLI Commands             | Practice `describe-instances`, filtering and querying      | ✅     |
| Tag Filtering                | Use `--filters` to get instance by tag name                | ✅     |
| IAM Role vs IAM User         | Clear distinction, use cases, and interview-style clarity  | ✅     |
| Public IP vs Elastic IP      | Difference in lifecycle, allocation, behavior              | ✅     |
| Launch Requirements          | List parameters to launch EC2 via CLI                      | ✅     |
| Instance Lifecycle           | Understand start/stop vs terminate effects                 | ✅     |
| EBS Basics                   | What is EBS, how it's attached and deleted                 | ✅     |
| Security Group               | Firewall-like behavior (inbound/outbound rules)            | ✅     |
| Role Inside Instance         | How IAM role gets automatically applied (no keys)          | ✅     |
| Metadata IP (`169.254...`)   | What it is, how to use it to check IAM role                | ✅     |
| Quiz Review (3 Questions)    | Recap of key tricky questions from assessment              | ✅     |
| Honest Self-Scoring          | 14/15 based on Day13 written answers                       | ✅     |

---

## 🧠 Bonus Knowledge Added Today

| Extra Item                                | Description |
|-------------------------------------------|-------------|
| `curl 169.254.169.254` Practice           | You practiced retrieving metadata from inside instance |
| Clarified wrong flag `--verify`           | AWS CLI uses `--dry-run`, no such `--verify` option    |
| IAM Role Inheritance via Metadata         | Role auto-applies, no manual AWS credentials needed    |
| Instance vs Region Specificity            | EC2 is region-specific, tag names are not unique       |

---
