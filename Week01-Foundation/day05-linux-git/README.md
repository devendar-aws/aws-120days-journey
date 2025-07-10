# 📘 Day 5 – Linux + Git + GitHub via CLI

**Date:** July 10, 2025  
**Theme:** Deeper into Linux, Git Basics, and GitHub Integration via CLI

---

## ✅ What I Did Today

- Started the EC2 instance and connected via SSH (`.pem` key).
- Created a new Linux user (`devopsuser`) inside EC2 and switched to it.
- Installed Git inside the EC2 Ubuntu instance.
- Generated an SSH key (`id_ed25519`) using:

      ssh-keygen -t ed25519 -C "your_email@example.com"

Understood difference between:

- .pem (EC2 RSA private key) vs .pub (GitHub public key)
- RSA (used by AWS) vs ED25519 (used by GitHub)

Added the public key to GitHub SSH settings.

- Verified SSH connection using:
  
      ssh -T git@github.com

Created a new directory (aws-cli-test) inside EC2 and initialized Git using:

    git init
    git remote add origin git@github.com:devendar-aws/aws-120days-journey.git

Faced a Git push error due to unrelated histories and fixed it by:

- Pulling remote main branch
- Merging and switching to main using:

        git pull origin main --allow-unrelated-histories
        git branch -M main
        git push origin main

- Successfully pushed from EC2 to GitHub using CLI!

🔧 Key Learnings

- Git key-pairing between local EC2 and GitHub works via SSH public key.
- .git folder tracks all git metadata.
- Git stages changes (git add) and commits them (git commit).
- Unrelated histories error occurs when local and remote Git are initialized separately — fixed by merging and aligning branches.
- First successful push via CLI ✅

🛠️ Commands Used

    sudo apt update
    sudo apt install git
    adduser devopsuser
    su - devopsuser

    ssh-keygen -t ed25519 -C "devendar.aws@gmail.com"
    cat ~/.ssh/id_ed25519.pub
    
    To check if your SSH key is added to the SSH agent (i.e. loaded and ready to use), run this:

    ssh-add -l

    git init
    git remote add origin git@github.com:devendar-aws/aws-120days-journey.git
    git pull origin main --allow-unrelated-histories
    git branch -M main
    git add .
    git commit -m "First push from EC2"
    git push origin main

🐛 Debugging Done

- SSH error due to incorrect key pasting → fixed after reviewing the key carefully.
- Git push failed due to unrelated histories → fixed by allowing pull + merge.
- Resolved EC2 default Git branch being master by switching to main.

See full details in debug_notes.md.
📓 Notes Saved

- All Linux/Git concepts added to learning_notes.md
- All Git/SSH/branch debug steps added to debug_notes.md

📸 Screenshots

- SSH key added to GitHub ✅
- Terminal screenshot of successful git push from EC2 ✅
