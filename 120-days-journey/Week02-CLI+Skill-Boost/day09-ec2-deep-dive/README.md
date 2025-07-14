# 🧱 Day 09 – EC2 Deep Dive via Console & CLI (July 14, 2025)

## 📌 Objectives

- Understand EC2 fundamentals: instances, AMI, instance types, key pairs, security groups
- Learn how Security Groups control inbound & outbound traffic
- Launch and SSH into EC2 via CLI
- Terminate EC2 instance safely
- Prepare for certification + real-world DevOps tasks

---

## ⚙️ Topics Covered

- EC2 components: AMI, instance types, key pairs, EBS, Subnets
- Inbound vs Outbound Rules in Security Groups
- Public IP vs Private IP
- SSH via `.pem` key and username mapping
- Common SSH issues and fixes (permissions, AMI mismatch)
- Differences between EC2 via Console vs CLI

---

## 🖥️ Commands Used


# Launch EC2 Instance via CLI
    aws ec2 run-instances \
      --image-id ami-021a584b49225376d \  # Ubuntu 22.04 LTS (Mumbai)
      --instance-type t2.micro \
      --key-name dev-ec2 \
      --security-group-ids sg-0506b8cd5b286e777 \
      --subnet-id subnet-0d514b947c5a0fa73 \
      --associate-public-ip-address \
      --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=dev-cli-instance}]' \
      --output json

# Get Public IP
    aws ec2 describe-instances \
      --filters "Name=tag:Name,Values=dev-cli-instance" \
      --query "Reservations[*].Instances[*].PublicIpAddress" \
      --output text

# SSH into Instance
    ssh -i "EC2 Keys/dev-ec2.pem" ubuntu@<public-ip>

# Terminate Instance
    aws ec2 terminate-instances --instance-ids <instance-id>



##🧠 Key Learnings

- Inbound Rule = source (who can enter EC2)
- Outbound Rule = destination (where EC2 can talk to)
- 0.0.0.0/0 means open to all IPv4 addresses
- Key pair mismatch or wrong AMI causes SSH failure
- Amazon Linux uses ec2-user, Ubuntu uses ubuntu

## 🛠️ Bonus Tips

- Use --associate-public-ip-address when using custom subnets
- Use chmod 400 to secure .pem key
- Use verbose SSH for debugging: `ssh -i "EC2 Keys/dev-ec2.pem" ubuntu@13.203.207.64 -v`  
This will give a detailed log of what’s happening 
- Always confirm AMI ID when launching from CLI
