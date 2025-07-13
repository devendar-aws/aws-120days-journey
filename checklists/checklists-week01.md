### ✅ Day 1 – Sankalpa + Setup (July 6)

| Task | Status |
|------|--------|
| 🛕 Performed Sankalpa + Spiritual Initiation | ✅ |
| 📘 Created main GitHub repo `aws-120days-journey` | ✅ |
| 📁 Created folder structure: `week01-foundation/day01-sankalpa-setup` | ✅ |
| 📝 Wrote Day 1 `README.md` with personal vow, goal, roadmap | ✅ |
| 🎯 Defined 18 LPA goal, project flow, certification path | ✅ |
| 🧭 Setup 120-day tracker (Excel/Notion/manual) | ✅ |
| ✅ Marked Day 1 complete in tracker/log | ✅ |

### ✅ Day 2 – IAM + EC2 Basics (July 7)

| Task | Status |
|------|--------|
| 👤 Created IAM user with admin access | ✅ |
| 🔒 Enabled MFA and generated Access Keys | ✅ |
| 🧾 Configured AWS CLI via `aws configure` | ✅ |
| 🧠 Verified identity with `aws sts get-caller-identity` | ✅ |
| 💻 Launched EC2 instance (Free Tier, Ubuntu) | ✅ |
| 🔐 Created new key pair `.pem` file | ✅ |
| 🚪 Added SSH rule (port 22) in security group | ✅ |
| 🔌 Connected to EC2 via SSH using Git Bash | ✅ |
| 📁 Created folder: `week01-foundation/day02-iam-ec2-basics/` | ✅ |
| 📝 Wrote Day 2 `README.md` with IAM & EC2 steps | ✅ |
| ✅ Marked Day 2 complete in tracker/log | ✅ |

### ✅ Day 3 – S3 Static Website Hosting (July 8)

| Task | Status |
|------|--------|
| 🪣 Created S3 bucket `dev-s3-day3` in `ap-south-1` | ✅ |
| 🔐 Disabled Block Public Access | ✅ |
| 🌐 Enabled Static Website Hosting | ✅ |
| 📤 Uploaded `index.html` file | ✅ |
| 🔓 Applied public-read bucket policy | ✅ |
| 🌍 Verified website is live via S3 endpoint | ✅ |
| 📁 Created folder: `week01-foundation/day03-s3-static-website/` | ✅ |
| 🖼️ Added screenshot of live website | ✅ |
| 📝 Wrote Day 3 `README.md` documenting setup | ✅ |
| ✅ Marked Day 3 complete in tracker/log | ✅ |

### ✅ Day 4 Checklist – Apache Static Website on EC2

| Task                                                                 | Status |
|----------------------------------------------------------------------|--------|
| 📦 Launch new EC2 (Ubuntu) in `ap-south-1` region                    | ✅     |
| 🔐 Create + attach security group with port 22 + 80 open             | ✅     |
| 📁 SSH into instance using your `.pem` key (CLI)                     | ✅     |
| 🔧 Install Apache (`sudo apt install apache2`)                       | ✅     |
| ▶️ Start + enable Apache (`systemctl start apache2`, `enable`)       | ✅     |
| 📄 Replace default `index.html` with your custom HTML                | ✅     |
| 🌐 Open `http://<EC2 Public IP>` in browser and verify the webpage   | ✅     |
| 📸 Take screenshot of live Apache-hosted site                        | ✅     |
| 📁 Create `week01-foundation/day04-apache-ec2/` folder in GitHub     | ✅     |
| 📝 Add detailed `README.md` for Day 4 (commands, reflections, etc.)  | ✅     |
| ☁️ Upload screenshot to GitHub folder                                | ✅     |
| ✅ Mark Day 4 complete in tracker + master checklist                 | ✅     |


### ✅ Day 5 Checklist (Linux + Git + GitHub via CLI)

| Task                                                                                   | Status |
|----------------------------------------------------------------------------------------|--------|
| 🔐 Created a new Linux user (`devopsuser`) on EC2 and switched into it                 | ✅     |
| 🔑 Generated new SSH key using `ssh-keygen -t ed25519`                                 | ✅     |
| 🗝️ Added SSH public key to GitHub > Settings > SSH Keys                                | ✅     |
| 🔗 Verified GitHub SSH connection using `ssh -T git@github.com`                        | ✅     |
| 📂 Initialized local repo folder `aws-cli-test/`, ran `git init`                       | ✅     |
| 🔄 Set remote origin and resolved branch mismatch using `git branch -M main`           | ✅     |
| 🔄 Resolved "unrelated histories" by merge method or manual fix                        | ✅     |
| 🐛 Performed first real GitHub debugging: SSH mismatch, wrong key, branch issues       | ✅     |
| 📝 Created and pushed `learning_notes.md` and `debug_notes.md`                         | ✅     |
| 📁 Updated GitHub `week01-foundation/day05-linux-git-cli/README.md` with learnings     | ✅     |
| 🧭 Marked Day 5 complete in master tracker and repo                                    | ✅     |

### ✅ Day 6 Checklist (Revision + Assessment + SSH/Git Integration)

| Task                                                                                  | Status |
|---------------------------------------------------------------------------------------|--------|
| 🔁 Revised IAM, EC2, and S3 core concepts from Days 2–4                                | ✅     |
| 🧠 Attempted 5 real-world scenario-based assessment questions                          | ✅     |
| 📝 Wrote answers for all 5 questions (self-evaluation)                                | ✅     |
| 📊 Evaluated score based on completeness and accuracy                                 | ✅     |
| 🧾 Created `assessment-01.md` file with all Q/A, improved answers, notes              | ✅     |
| 💻 Connected to EC2 via CLI                                                           | ✅     |
| 🔐 SSH GitHub setup: validated `.ed25519` key connection from EC2                     | ✅     |
| ⚙️ Resolved PTY allocation warning (understood it's harmless for Git use)             | ✅     |
| 🔁 Practiced Git pull/push from EC2 CLI                                               | ✅     |
| 📁 Updated GitHub Day 6 folder: `README.md`, screenshots, checklist, assessment file  | ✅     |
| ✅ Marked Day 6 complete in tracker and master checklist                              | ✅     |

## ✅ Checklist for Day 07

| Task                                                                 | Status |
|----------------------------------------------------------------------|--------|
| Completed S3 Static Website Hosting Project                         | ✅     |
| Wrote Project README and added screenshot                           | ✅     |
| Uploaded to GitHub under `projects/project01-s3-static-website/`             | ✅     |
| Created honest Resume/Profile V1                                    | ✅     |
| Mapped Amazon past roles into relevant cloud experience              | ✅     |
| Avoided CTC, fake titles, and salary discussions in resume          | ✅     |
| Added summary: "Actively targeting ₹18 LPA+ AWS Cloud roles..."     | ✅     |
| Exported resume as PDF and added to GitHub                          | ✅     |
| Finalized Week 01 README, Learning Notes, Debug Notes               | ✅     |
| Prepared for Week 02: Project Push + CLI Proficiency                | ✅     |
