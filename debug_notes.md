# 🛠️ Debug Notes: Challenges, Fixes & Workarounds in My AWS Journey

This file captures all debugging situations and fixes I encountered — so I can revisit and reflect when facing similar issues in the future.

---

## 🧭 [Day 5] GitHub SSH Key Not Matching

**Problem:**  
SSH authentication to GitHub failed with fingerprint mismatch.

**Mistake:**  
I accidentally added this key:  
`ssh-ed25519 AAAAC3...z0Hl devendar.aws@gmail.com`  
instead of:  
`ssh-ed25519 AAAAC3...zOHl devendar.aws@gmail.com`  
(Notice the character difference in the key ending)

**Fix:**  
- Rechecked the public key
- Updated the correct key on GitHub → SSH keys
- Verified using: `ssh -T git@github.com`
- ✅ Output: *Hi devendar-aws! You've successfully authenticated...*

---

## 🧭 [Day 5] Git Push Failed – Unrelated Histories

**Problem:**  
`git push origin main` failed with:  
`fatal: refusing to merge unrelated histories`

**Cause:**  
- GitHub repo was initialized separately.
- Local repo was initialized via `git init` — they had different histories.

**Fix:**

    git pull origin main --allow-unrelated-histories
# Then resolved the merge message (left as default)
    git push origin main

---

## 🧭 [Day 5] Local Branch Was master, Not main

**Problem:**
Push failed due to branch name mismatch.

**Fix:**

    git branch -M main

This renamed local branch to main to match remote.

---

## 🧭 [Day 11] Public read ACL

- ❗ Got `AccessControlListNotSupported` error when using `--acl public-read`  
  👉 Root Cause: The bucket had **ACLs disabled via Block Public Access (BPA)**  
  ✅ Fix: Removed `--acl public-read` from the script. Upload + access worked correctly.

- 🧰 EC2 instance had no `unzip` package  
  ✅ Fix: Installed using `sudo apt install unzip`, enabling AWS CLI installation.

---

## 🧭 [Day 16] Lambda + DynamoDB CRUD
| 🕒 Time          | 🔧 Issue                                                 | 🧠 Root Cause                                                         | ✅ Fix                                                     |
| ---------------- | -------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------- |
| ✅ Initial        | Getting consistent `"Item created"` response             | None                                                                  | Lambda Create (PUT) was working correctly                 |
| ❌ Update Error 1 | `ValidationException: reserved keyword: status`          | `"status"` is a **reserved word** in DynamoDB                         | Used `ExpressionAttributeNames` to alias `status` as `#s` |
| ❌ Update Error 2 | `Syntax error: expected an indented block after 'elif'`  | Python indentation error after `elif task == "update":`               | Fixed indentation under the `elif` block                  |
| ❌ Deployment lag | Lambda ran old version after update                      | Lambda still executing **previous version** due to ongoing deployment | Waited for deployment to complete or redeployed manually  |
| ✅ Final          | Create, Read, Update, Delete all working via test events | -                                                                     | Clean, tested function for all CRUD operations            |

---
