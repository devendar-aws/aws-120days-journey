# 📘 Day 13 Assessment – AWS CLI, EC2, IAM Role

---

## ✅ Instructions
- Total Questions: 15  
- Format: Written Answers  
- Topics: AWS CLI, EC2, IAM Role, Metadata  
- Marking: ✅ Correct | ❌ Incorrect

---

### 1️⃣ What does `aws configure` do?
**Your Answer:**  
access key, secret access key, region and output format  
**✅ Correct**

---

### 2️⃣ Command to get EC2 instance details?
**Your Answer:**  
aws ec2 describe-instances  
**✅ Correct**

---

### 3️⃣ What info can we get from `describe-instances`?
**Your Answer:**  
Used to know the instanceid, state.name, publicipadress, tags, volume etc.  
**✅ Correct**

---

### 4️⃣ How to get public IP in table format from CLI?
**Your Answer:**  
aws ec2 describe-instances --query "Reservations[*].Instances[*].[PublicIPAddress]" --output table  
**✅ Correct**

---

### 5️⃣ What all is needed to launch an EC2 instance via CLI?
**Your Answer:**  
Image ID, Count of instances, Instance Type, Key-pair name, Security Group ID, Subnet ID, Tag Name  
**✅ Correct**

---

### 6️⃣ Difference between Public IP and Elastic IP?
**Your Answer:**  
Public IP is created every time an instance is started. Elastic IP is allocated and associated to a running instance and the IP remains same.  
**✅ Correct**

---

### 7️⃣ What is a Security Group?
**Your Answer:**  
A firewall with inbound and outbound rules. It decides what traffic can access the instance.  
**✅ Correct**

---

### 8️⃣ Can we connect to instance after stop/start?
**Your Answer:**  
Yes. When stopped, the services are down. When started again, it can be connected.  
**✅ Correct**

---

### 9️⃣ What is EBS?
**Your Answer:**  
Elastic Block System. A memory unit for an instance. Terminated with the instance.  
**✅ Correct** *(Minor note: “System” should be “Store” but allowed)*

---

### 🔟 Why do we use tag name for describing instance?
**Your Answer:**  
To identify instance. EC2 is region-unspecific. InstanceId is unique, but tag names can be same.  
**✅ Correct**

---

### 1️⃣1️⃣ IAM Role vs IAM User?
**Your Answer:**  
IAM role is for services. IAM user is for persons with credentials.  
**✅ Correct**

---

### 1️⃣2️⃣ Why not give access keys but attach IAM role?
**Your Answer:**  
Access keys give full control. IAM role gives only needed permissions.  
**✅ Correct**

---

### 1️⃣3️⃣ Can EC2 access AWS CLI without keys if IAM role is attached?
**Your Answer:**  
Yes. If IAM role has permission, the instance adopts the configuration.  
**✅ Correct**

---

### 1️⃣4️⃣ What flag is used to confirm actions in CLI?
**Your Answer:**  
--verify  
**❌ Incorrect**  
✅ **Correct Answer:** No universal `--verify`. Use `--dry-run`, `--no-cli-pager`, or service-specific flags.

---

### 1️⃣5️⃣ Is IAM role attached to AMI or Instance?
**Your Answer:**  
Instance level  
**✅ Correct**

---

## 📊 Result

| Total Questions | Correct | Incorrect |
|-----------------|---------|-----------|
| 15              | 14      | 1         |

✅ **Score: 14/15** – Excellent!

---

## 🧠 Quick Review Quiz

### ✅ Question 1:  
🔹 What is `169.254.169.254`?

**Your Answer:**  
It’s not a public IP. It’s an internal IP used for instance metadata (IMDS).  
**✅ Correct**  
➡️ It’s always the same and accessible only inside the EC2 instance.

---

### ✅ Question 2:  
🔹 Will that IP change?

**Your Answer:**  
No, it will not change.  
**✅ Correct**  
➡️ It’s a static internal IP hardcoded into AWS EC2 infrastructure.

---

### ✅ Question 3:  
🔹 What is one way to check if IAM Role is attached to the instance from inside?

**Your Answer:**  
Use `curl http://169.254.169.254/latest/meta-data/iam/info`  
**✅ Correct**  
➡️ This confirms role name and credentials from inside the EC2.

