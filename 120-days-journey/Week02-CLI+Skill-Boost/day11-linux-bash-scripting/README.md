# 📅 Day 11 – Linux Bash Scripting (Week 2)

**Date:** July 16, 2025  
**Theme:** Learn Bash Scripting to Automate AWS CLI Tasks  
**Track:** Week 2 – CLI + Dev Skill Boost

---

## ✅ Today's Accomplishments

| Task                                                                 | Status |
| -------------------------------------------------------------------- | ------ |
| Understood the basics of bash scripting                             | ✅      |
| Created and tested `backup.sh` and `move.sh`                        | ✅      |
| Used conditional expressions (`-z`, `-d`, `-p`) in scripts           | ✅      |
| Uploaded files to S3 using script (`s3-upload.sh`)                  | ✅      |
| Debugged ACL error (`AccessControlListNotSupported`)                | ✅      |
| Learned difference: `--acl public-read` vs bucket policy            | ✅      |
| Understood presigned URLs with `aws s3 presign`                     | ✅      |
| Reviewed IAM Groups (vs Users & Roles)                              | ✅      |
| Practiced quizzes: Bash, IAM                                        | ✅      |

---

## 🧠 Key Concepts Covered

- Bash script basics: `#!/bin/bash`, `chmod +x`, `echo`, `$1`, `$#`, `if`, `else`
- Condition flags:  
  - `-z`: check if string is empty  
  - `-d`: check if directory exists  
  - `-p`: check if port is in use (conceptual)
- Automating AWS CLI with parameters
- Presigned URL usage for secure, temporary access
- IAM Groups: Assign shared permissions across users
- ACL vs Bucket Policy (object vs bucket-level control)

---

## 🐚 Scripts You Built

### 1. `backup.sh`
Takes a directory and creates a timestamped `.tar.gz` backup.


    #!/bin/bash
    DIR=$1
    if [ -z "$DIR" ]; then
      echo "Usage: ./backup.sh <directory>"
      exit 1
    fi
    tar -czf "${DIR}_$(date +%F).tar.gz" "$DIR"

### 2. move.sh

Moves all files from one directory to another.

    #!/bin/bash
    SRC=$1
    DEST=$2
    if [ ! -d "$SRC" ] || [ ! -d "$DEST" ]; then
      echo "Source or destination not found."
      exit 1
    fi
    mv "$SRC"/* "$DEST"/

## 3. s3-upload.sh

Uploads file to S3 and returns the object URL.

    #!/bin/bash
    FILE=$1
    BUCKET="dev-cli-bucket-01"
    aws s3 cp "$FILE" s3://$BUCKET/
    echo "https://$BUCKET.s3.ap-south-1.amazonaws.com/$FILE"

    ⚠️ Note: Removed --acl public-read since bucket already has a public-read policy.

## 4. aws s3 presign demo

`aws s3 presign s3://dev-cli-bucket-01/test.txt --expires-in 300`

🪛 Debug Notes

    ❗ Got AccessControlListNotSupported error when using --acl public-read on a bucket that already had a public policy.

    ✅ Fixed it by removing the ACL flag in the upload script.

    ✅ Verified upload via S3 object URL and presigned URL.

    ✅ Installed unzip and AWS CLI in EC2 using sudo apt install unzip && sudo apt install awscli.

📝 IAM Group Recap

    IAM Group = Collection of users with shared permission policies.

    No trust policy like roles.

    Easier management of access at team-level.

🏁 Completion Badge

✅ Day 11 Completed – Bash Scripting, Presign URLs, IAM Group Concepts
