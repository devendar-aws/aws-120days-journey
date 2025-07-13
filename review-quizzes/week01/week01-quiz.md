# 🧠 Review Quiz – Day 7 (IAM + EC2 + S3 + Git + Linux)

**Date:** July 12, 2025  
**Devendar's Score:** ✅ 17 / 20

---
---

## 🧪 Week 01 Review Questions (MCQs & Fill in the Blanks)

These questions helped reinforce key concepts from IAM, EC2, S3, Git, and Linux covered in Week 01.

### ✅ Multiple Choice Questions (1–15)

1. **Which AWS service is global?**  
   **Answer:** B. IAM

2. **What command shows the AWS CLI identity of a user?**  
   **Answer:** C. `aws sts get-caller-identity`

3. **What port is used to SSH into an EC2 instance?**  
   **Answer:** B. 22

4. **How do you connect to GitHub via SSH?**  
   **Answer:** C. `ssh -T git@github.com`

5. **Which command is used to install Apache on Ubuntu?**  
   **Answer:** C. `sudo apt install apache2 -y`

6. **What tool is used to manage public access in S3?**  
   **Answer:** B. Block Public Access settings

7. **What type of key is typically used for EC2 login?**  
   **Answer:** C. `.pem` (RSA)

8. **Which of these will stage changes in Git?**  
   **Answer:** D. `git add .`

9. **What is the default HTML file Apache looks for?**  
   **Answer:** A. `index.html`

10. **What service allows hosting a static website without a server?**  
   **Answer:** B. S3

11. **What must be added to access a static S3 site publicly?**  
   **Answer:** C. Bucket Policy + BPA disabled

12. **Where do you set the homepage for S3 Static Website Hosting?**  
   **Answer:** C. Website Hosting configuration

13. **Which command updates package lists in Ubuntu?**  
   **Answer:** B. `sudo apt update`

14. **Which file stores GitHub public key on local system?**  
   **Answer:** C. `id_ed25519.pub`

15. **Which branch is preferred on GitHub?**  
   **Answer:** C. `main`

---

### ✅ Fill in the Blanks (16–20)

16. **Command to install Apache on Ubuntu**:  
   `sudo apt install apache2 -y`

17. **.pem stands for**:  
   **Privacy Enhanced Mail**

18. **Command to verify AWS CLI identity**:  
   `aws sts get-caller-identity`

19. **Git files are usually stored in this directory**:  
   `~/.git/`

20. **Default Git branch on GitHub (recent)**:  
   `main` (older systems may use `master`)

---

🧠 Devendar scored: **Approx. 12.5 / 15** in MCQs and **5 / 5** in fill-in-the-blanks  
🔢 **Total Score**: **17.5 / 20**

---

## ✅ Multiple Choice Questions (15 Questions)

| Q# | Question Topic                   | Your Answer | Correct | Explanation |
|----|----------------------------------|-------------|---------|-------------|
| 1  | IAM permissions                  | B           | ✅       | IAM policies define access. |
| 2  | Global vs Regional AWS services  | C           | ✅       | IAM is a global service. |
| 3  | IAM identity check (CLI)         | B           | ✅       | `get-caller-identity` confirms identity. |
| 4  | SSH default port                 | C           | ✅       | Port 22 is used for SSH. |
| 5  | S3 website access                | C           | ✅       | Need both public access + hosting enabled. |
| 6  | S3 bucket naming scope           | B           | ✅       | Bucket names must be globally unique. |
| 7  | EC2 SSH file type                | C           | ✅       | `.pem` is used for EC2 access. |
| 8  | Apache default page              | D           | ✅       | Apache shows its default HTML page. |
| 9  | Git commit vs push               | A           | ❌       | ❗Correct: C – `commit` saves locally, `push` uploads to GitHub. |
| 10 | List files in Linux              | B           | ✅       | `ls` lists directory contents. |
| 11 | Git staging area                 | C           | ✅       | `git add` sends files to staging. |
| 12 | SSH key type for GitHub          | C           | ✅       | GitHub prefers `ed25519`. |
| 13 | File permissions for .pem        | B           | ✅       | `chmod 400` = read-only for user. |
| 14 | Test GitHub SSH connection       | C           | ✅       | `ssh -T git@github.com` confirms access. |
| 15 | Initialize a Git repo            | C           | ✅       | `git init` starts a local Git repo. |

**✅ MCQ Score: 14 / 15**

---

## ✍️ Fill in the Blanks (5 Questions)

| Q# | Prompt                                           | Your Answer                          | Correct | Comment |
|----|--------------------------------------------------|---------------------------------------|---------|---------|
| 16 | Command to install Apache on Ubuntu             | `sudo apt install apache2 -y`        | ✅       | Perfect! |
| 17 | Full form of PEM                                | **Private** Enhanced Mail            | ❌       | ❗Should be: *Privacy* Enhanced Mail |
| 18 | CLI command to check IAM identity               | `aws sts get-caller-identity`        | ✅       | Great recall. |
| 19 | Folder created after `git init`                 | `.ssh`                               | ❌       | ❗Correct: `.git` (SSH keys go in `.ssh`) |
| 20 | Default Git branch today                        | `main` (commented on master switch)  | ✅       | Nice awareness. |

**✅ Fill-in-the-Blanks Score: 3 / 5**

---

## 🎯 Final Score Summary

| Section        | Score      |
|----------------|------------|
| **MCQs**       | 14 / 15    |
| **Fill Blanks**| 3 / 5      |
| **Total**      | **17 / 20 ✅** |

---

## 🌟 Feedback

You're showing **excellent memory, conceptual clarity, and awareness** for Day 6. Just keep refining:
- The difference between `.git` and `.ssh`
