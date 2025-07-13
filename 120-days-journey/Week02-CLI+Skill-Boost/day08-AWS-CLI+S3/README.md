# 🗓️ Day 08: AWS CLI + S3 Mastery (July 13, 2025)

## ✅ What I Did Today

- Configured AWS CLI using `aws configure`
- Verified credentials, region, and config files `aws configure list`
- Created an S3 bucket via CLI using `aws s3api create-bucket`, 
- Uploaded files via `aws s3 cp`
- Disabled BPA (Block Public Access) using `put-public-access-block`
- Attached a public-read bucket policy using `put-bucket-policy`
- Accessed uploaded file via HTTPS object URL
- Understood the difference between:
  - `aws s3 cp` vs `aws s3 sync`
  - Static website endpoint vs S3 object URL
  - Default vs deleted file behavior with `--delete`
- Explored how HTTP/HTTPS access works in S3 (no explicit port config)
- Understood 7-layer AWS architecture (Global Infra → Monitoring)
- Created a unified mental model of AWS system design

## 🔁 Not Done (Optional Task)

- [ ] Script `s3-upload.sh`: Upload file + return public URL
- [ ] `aws s3 presign` usage: Generate temporary pre-signed link

## 💡 Notes
- Use `--dryrun` before `--delete` in sync
- Only `sync --delete` removes files from destination
- Use `aws s3 presign` for temporary secure sharing

---

🎯 Next: EC2 Deep Dive (Day 09)
