### ✅ Day 08 Checklist – AWS CLI + S3

| Task                                                     | Status |
|----------------------------------------------------------|--------|
| Configured AWS CLI and verified setup                    | ✅     |
| Created and listed S3 bucket via CLI                     | ✅     |
| Uploaded file to S3 using `aws s3 cp`                    | ✅     |
| Disabled BPA (Block Public Access)                       | ✅     |
| Applied public-read bucket policy                        | ✅     |
| Accessed file via HTTPS S3 object URL                    | ✅     |
| Understood difference between static site vs object link | ✅     |
| Understood `cp` vs `sync` and `--delete` flag            | ✅     |
| Explored 7-layer AWS mental architecture                 | ✅     |
| Bonus: `s3-upload.sh` script                             | ❌     |
| Bonus: `aws s3 presign` usage                            | ❌     |


### ✅ Day 09 Checklist – EC2 Deep Dive

| Task                                                     | Status |
| -------------------------------------------------------- | ------ |
| Understood EC2 core components                           | ✅      |
| Launched EC2 instance via CLI                            | ✅      |
| Verified public IP and key pair                          | ✅      |
| SSH access using correct user + `.pem`                   | ✅      |
| Identified AMI mismatch and fixed it                     | ✅      |
| Terminated EC2 instance safely                           | ✅      |
| Understood SGs: inbound vs outbound                      | ✅      |
| Bonus: Used `aws ec2 describe-*` for instance details    | ✅      |


### ✅ Day 10 + Day 09 (CLI Carryover) Checklist

| Task                                                                | Status |
|---------------------------------------------------------------------|--------|
| Understood IAM Role structure: Trust vs Permission policies         | ✅     |
| Compared Managed vs Inline Policies                                 | ✅     |
| Created IAM Role via Console and attached to EC2                    | ✅     |
| Accessed S3 from EC2 without access keys                            | ✅     |
| Understood how EC2 assumes a role (temporary credentials)           | ✅     |
| Understood why `create-role` from EC2 CLI failed (access denied)    | ✅     |
| CLI demo: Create snapshot from EBS volume                           | ✅     |
| CLI demo: Create volume from snapshot                               | ✅     |
| Described snapshots and volumes to verify                           | ✅     |


## ✅ Day 11 Checklist – Linux Bash Scripting + IAM Deep Dive

| Task                                                                 | Status |
|----------------------------------------------------------------------|--------|
| Understood basics of Bash scripting (echo, variables, loops, etc.)   | ✅     |
| Wrote `backup.sh` to zip files and move to backup folder             | ✅     |
| Wrote `s3-upload.sh` to upload files to S3                           | ✅     |
| Made `.sh` files executable and ran them successfully                | ✅     |
| Explored `--acl public-read` vs bucket policy                        | ✅     |
| Debugged ACL error (`AccessControlListNotSupported`)                | ✅     |
| Understood `aws s3 presign` to generate time-limited access links    | ✅     |
| Learned IAM Groups: purpose and usage                                | ✅     |
| IAM Quiz + Linux Quiz                                                | ✅     |
| Certification-style Quiz                                             | ✅     |
| Reflected on question difficulty and mock test plan                  | ✅     |
