## ✅ Day 08 – Commands Used (S3 + AWS CLI Mastery)
### 🔧 AWS Configuration

`aws configure`  
`aws configure list`

### 🪣 Bucket Management

`aws s3api create-bucket --bucket <bucket-name> --region ap-south-1`  
`aws s3 ls`                             # List all S3 buckets  
`aws s3 ls s3://<bucket-name>`         # List contents of specific bucket  

### 📂 File Upload & Deletion

`aws s3 cp <filename> s3://<bucket-name>/`          # Upload a single file  
`aws s3 rm s3://<bucket-name>/<filename>`           # Delete object from bucket  
`aws s3 rb s3://<bucket-name> --force`              # Remove bucket (even if not empty)  

### 🔐 Public Access Config

    aws s3api put-public-access-block \
      --bucket <bucket-name> \
      --public-access-block-configuration '{
         "BlockPublicAcls": false,
         "IgnorePublicAcls": false,
         "BlockPublicPolicy": false,
         "RestrictPublicBuckets": false
     }'

    aws s3api put-bucket-policy \
      --bucket <bucket-name> \
      --policy file://public-read-policy.json

### 🔄 Sync vs Copy (Explored Concepts)

`aws s3 cp <file> s3://<bucket-name>/`              # One-time copy  
`aws s3 sync <local-folder> s3://<bucket-name>/`    # Sync folder (upload)  
`aws s3 sync <local-folder> s3://<bucket-name>/ --delete`  # Sync + remove extraneous files  

## 🔗 Optional (To try later)

`aws s3 presign s3://<bucket-name>/<filename>`      # Generate temp signed URL  

## 📁 Optional Files

`public-read-policy.json`   # JSON file for bucket access  
`s3-upload.sh`              # Shell script to upload and return public URL (todo)  

