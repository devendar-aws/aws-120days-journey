# 🧠 AWS Cheat Sheet – Devendar (Day 1 to Day 13)

---

## 🔐 1. IAM (Identity & Access Management)

| Concept        | Details |
|----------------|---------|
| IAM User       | Human identity with long-term credentials (access key & secret). |
| IAM Role       | No credentials. Temporary access assumed by AWS services. |
| IAM Policy     | JSON document defining permissions (Allow/Deny + Actions + Resources). |
| Types of Policies | AWS Managed, Customer Managed, Inline (directly attached). |
| Use in EC2     | Role lets EC2 access services (like S3) without `aws configure`. |
| Best Practice  | Avoid using root account or storing access keys inside EC2. |

---

## 📦 2. S3 (Simple Storage Service)

| Concept           | Details |
|-------------------|---------|
| Bucket            | Top-level container for storing objects. Globally unique. |
| Object            | Actual file stored in the bucket. |
| Static Website Hosting | Enable hosting via bucket properties. |
| Versioning        | Keep multiple versions of the same object. |
| Storage Classes   | Standard, IA, One Zone IA, Glacier, Deep Archive. |
| Access Control    | IAM policies, bucket policies, and ACLs. |
| CLI Commands      | `aws s3 cp`, `sync`, `ls`, `rm`, `rb` |

---

## 🖥️ 3. EC2 (Elastic Compute Cloud)

| Concept            | Details |
|--------------------|---------|
| AMI                | Amazon Machine Image – template with OS and config. |
| Instance Type      | Defines CPU, RAM – e.g., `t2.micro`. |
| Key Pair           | SSH key for EC2 access (`.pem` file). |
| Security Group     | Acts as firewall – controls traffic via ports. |
| Instance Lifecycle | `pending → running → stopped → terminated`. |
| User Data          | Startup script (e.g., install Apache). |
| Elastic IP         | Static IP, manually allocated and associated. |
| Public IP          | Assigned on start; changes after stop/start. |
| Tags               | Key-value pairs (e.g., Name: DevendarEC2). |
| Connect            | `ssh -i key.pem ec2-user@<public-ip>`. |
| Apache Setup       | `yum install httpd`, `systemctl start/enable httpd`. |

---

## 💾 4. EBS (Elastic Block Store)

| Concept            | Details |
|--------------------|---------|
| EBS Volume         | Persistent block storage for EC2. |
| Delete on Termination | Configurable – volume may persist after termination. |
| Attach/Detach      | Can move volume between instances. |
| Types              | `gp3`, `io2`, `sc1`, `st1`. |

---

## 🔐 5. Security Group vs NACL

| Feature           | Security Group           | NACL                     |
|-------------------|--------------------------|---------------------------|
| Scope             | Instance-level           | Subnet-level              |
| Stateful          | ✅ Yes                   | ❌ No (stateless)         |
| Rules             | Only allow               | Allow & Deny              |
| Default Inbound   | Deny all                 | Allow all                 |
| Default Outbound  | Allow all                | Allow all                 |

---

## 🔑 6. Key Pairs

| Concept     | Details |
|-------------|---------|
| Purpose     | SSH into EC2 Linux instance. |
| Format      | `.pem` for Linux, convert to `.ppk` for Windows (PuTTY). |
| Security    | Cannot download `.pem` again. Store safely. |

---

## 🌐 7. Public IP vs Elastic IP

| IP Type     | Changes on Restart? | Static? | Usage |
|-------------|---------------------|---------|--------|
| Public IP   | ✅ Yes               | ❌ No   | Default, temporary access |
| Elastic IP  | ❌ No                | ✅ Yes  | Persistent, production apps |

---

## 🧾 8. Tags in EC2

| Concept    | Details |
|------------|---------|
| Name Tag   | Human-readable name for EC2 instance. |
| Use Cases  | Billing, automation, filtering, reports. |
| CLI Usage  | `--filters "Name=tag:Name,Values=YourTag"` |

---

## 💻 9. AWS CLI

| Command                             | Description |
|-------------------------------------|-------------|
| `aws configure`                     | Setup CLI with access keys, region, output. |
| `aws ec2 describe-instances`        | Show instance details. |
| `--query`                           | Filter output using JMESPath syntax. |
| `--output table/json/text`          | Format the CLI result. |
| `aws s3 cp`, `ls`, `rm`, `sync`     | Interact with S3 buckets. |
| EC2 + Role = No CLI config needed   | Role provides temporary credentials automatically. |

---

## 🔍 10. EC2 Metadata

| Endpoint                                      | Description |
|-----------------------------------------------|-------------|
| `http://169.254.169.254/latest/meta-data/`    | Base URL for metadata access. |
| `/public-ipv4`, `/local-ipv4`                 | Fetch public and private IPs. |
| `/iam/info`                                   | View IAM role attached to instance. |
| Example: `curl http://169.254.169.254/latest/meta-data/public-ipv4` | Get instance's public IP. |

---

### ✅ The IP 169.254.169.254 is always the same for all EC2 instances — it never changes.
- It’s a reserved link-local IP by AWS for the Instance Metadata Service (IMDS).  
🔒 `169.254.169.254` remains the same — always accessible inside the instance.  
`169.254.169.254` = Fixed internal portal for your EC2’s brain 🧠 (metadata).

---
### 🧠 1. IAM Role vs IAM User

| Feature        | IAM **User**                  | IAM **Role**                              |
| -------------- | ----------------------------- | ----------------------------------------- |
| Identity Type  | Long-term human identity      | Temporary identity for AWS services       |
| Credentials    | Access Key + Secret Key       | No credentials; uses **temporary tokens** |
| Login Possible | ✅ Yes (console + CLI)         | ❌ No console login (unless assumed)       |
| Example Use    | Devendar accessing S3 via CLI | EC2 instance accessing S3 without keys    |
| Security Model | Manual access control         | Fine-grained, **least privilege**         |

#### ✅ Interview line:

    "IAM User is a human with credentials. IAM Role is a temporary identity assumed by services like EC2 or Lambda to perform actions without exposing secrets."

---

### 🧠 2. CLI Access vs Role Access in EC2

| Method                                              | Description                                                                                                                                                                                           |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🔑 **CLI via `aws configure`**                      | You manually set up access key + secret key in the EC2 or your terminal. Requires credentials to be stored in the instance. **(Not recommended for production)**                                      |
| 🎭 **Role-based Access (IAM Role attached to EC2)** | No need to store credentials. The instance automatically gets **temporary security credentials** via **Instance Metadata (169.254.169.254)**. This is the **safest** and most **recommended** method. |

#### ✅ Interview line:

    "Instead of storing access keys inside EC2, we attach an IAM Role. The EC2 then fetches temporary credentials from the instance metadata endpoint — secure and dynamic."

---

### 🧪 3. EC2 Describe with --filters

The `--filters` flag is used to filter EC2 instances based on key-value pairs like tag, instance-type, state, etc.

- Get Instance ID by Tag Name
    aws ec2 describe-instances \ 
    --filters "Name=tag:Name,Values=dev-instance" \ 
    --query "Reservations[*].Instances[*].InstanceId" \ --output text

- Get Public IP of Running Instances Only
    aws ec2 describe-instances \
    --filters "Name=instance-state-name,Values=running" \
    --query "Reservations[*].Instances[*].PublicIpAddress" \
    --output text

#### ✅ Interview line:

    "--filters allows us to target specific EC2 resources using key-value pairs — especially useful when there are many instances running in different states or environments."

---

### ⚙️ 4. AWS CLI Command Architecture (1-liner)

- Every AWS CLI command follows a structured 4-part format:  
`aws <service> <operation> [--filters/--query/options] [--output format]`

  - Example:  
    aws ec2 describe-instances --query "Reservations[*].Instances[*].InstanceId" --output table

| Part                 | Value                             |
| -------------------- | --------------------------------- |
| `aws`                | CLI tool                          |
| `ec2`                | Service                           |
| `describe-instances` | Operation                         |
| `--query`            | Optional filter for output fields |
| `--output`           | Output format (json, table, text) |

#### ✅ Interview line:

    "AWS CLI follows a consistent structure: aws service action [options], where filters like --query and --output refine what we see."

---

Q: What is the default IP 169.254.169.254 used for in EC2?  
A: "169.254.169.254 is an internal IP managed by the Instance Metadata Service (IMDS), used to fetch instance-specific data like IAM roles, instance ID, public IP etc., accessible only from within the instance."









































