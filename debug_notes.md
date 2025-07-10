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
```bash
git pull origin main --allow-unrelated-histories
# Then resolved the merge message (left as default)
git push origin main



## 🧭 [Day 5] Local Branch Was master, Not main

**Problem:**
Push failed due to branch name mismatch.

**Fix:**
    ```bash
       git branch -M main

This renamed local branch to main to match remote.
