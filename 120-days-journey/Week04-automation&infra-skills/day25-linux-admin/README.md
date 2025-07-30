# ✅ Day 25 – Linux Admin Practice with EC2 Instance (Not a Project)

**Date:** July 30, 2025  
**Focus:** Core Linux admin concepts inside an EC2 instance (Ubuntu)  
**Theme:** Strengthening fundamentals for AWS EC2, CLI, webserver setup, and service control

---

## 📌 Topics Covered

### ✅ Step 1: Created a New EC2 Instance (Ubuntu)
- Launch an EC2 instance with Ubuntu AMI.
- Used existing key pair for SSH access.
- Ensured port 22 (SSH) is open in inbound rules.
- Connected via SSH from local terminal.

### ✅ Step 2: Basic Linux Commands Practice
- Checked current user: `whoami`
- Created new user: `sudo adduser devuser`
- Switched to new user: `su - devuser`
- Understood `touch`, `ls`, `mkdir`, `cd`, `chmod`, `chown` commands.
- Handled permission issues while accessing `/home/devuser` from `/home/ubuntu`
- Explored file ownership with `ls -l` and changed permissions.
- Confirmed empty file creation with correct permissions.

### ✅ Step 3: Installed and Configured NGINX Webserver
- Installed NGINX: `sudo apt update && sudo apt install nginx`
- Checked service status: `sudo systemctl status nginx`
- Verified port 80 is listening: `sudo ss -tuln | grep :80`
- Confirmed NGINX welcome page accessible only **after** allowing port 80 in security group.
- Added HTTP inbound rule: `0.0.0.0/0` → Port 80
- Accessed the welcome page using EC2 public IP. [NGINX Webpage](./screenshots/nginx-page.png)

### ✅ Step 4: Compared NGINX and Apache
- Understood both are web servers.
- Verified that Apache was not currently installed.
- Realized installing NGINX doesn’t mean Apache is present.
- Recalled previous Apache static page project for comparison.
- Learned how to stop and remove a service if needed.

### ✅ Step 5: Hosting Static Web Page on EC2
- HTML and CSS files should be placed in `/var/www/html`
- Page is accessible only when the instance is **running**
- Compared with S3 website hosting:
  - S3 static site uses bucket objects
  - Accessible anytime via website endpoint
  - EC2 site is down if instance is stopped

---

## 🔐 Security Concepts Practiced

- Compared **HTTP vs HTTPS**
  - HTTPS is encrypted and more secure
- Discussed HTTPS usage:
  - For S3: HTTPS is by default when using CloudFront or website endpoints
  - For EC2: Requires SSL certificate via Let's Encrypt or ACM
- Public IP is used when accessing services over HTTPS
- Private IP is for internal communication only

---

## 🔧 Systemd and Service Management

- Checked if service is enabled on boot:  
  `systemctl is-enabled nginx`
- To enable at boot:  
  `sudo systemctl enable nginx`
- To disable from starting at boot:  
  `sudo systemctl disable nginx`

---

## ❓ EC2 Instance Management Clarification

- Stopped instances do **not incur compute charges**
- However, EBS volumes **do** incur storage cost even when instance is stopped
- It’s okay to keep stopped instances if EBS usage is within Free Tier

---

## ✅ Final Confirmation

- This is **not** considered a project.
- It was a **Linux EC2 Admin practice day**, strengthening foundational skills.
- NGINX was installed on an existing instance, not a fresh one.

---

## 📘 Summary

| Section            | Covered |
|--------------------|---------|
| EC2 Basics         | ✅       |
| Linux Commands     | ✅       |
| NGINX Setup        | ✅       |
| HTTP vs HTTPS      | ✅       |
| EC2 vs S3 Hosting  | ✅       |
| Boot Services      | ✅       |
| Instance Charges   | ✅       |

---

## Linux Commands:  
- Step 1: Users and Groups
- Step 2: File Permissions and Ownership
- Step 3: Managing Services with `systemctl`


### ✅ Step 1: Users and Groups
- cat /etc/passwd to diaplay the list of users
- cat /etc/shadow
- cat /etc/group to display the list of groups
#### 1. Create a new user
```
sudo adduser devuser
```
- Adds a new user named `devuser`.
- Prompts you to set a password and user details.
- A group is also created with the same name, automatically.

#### 2. Check current user
```
whoami
```
- Displays the currently logged-in user.

#### 3. Switch to another user
```
su - devuser
```
- Switches to the `devuser` user with their full login shell and environment.

#### 4. Check user ID and group ID
```
id
```
- Shows user ID (`uid`), group ID (`gid`), and groups the user belongs to.

#### 5. Check login users
```
who
```
- Lists all users currently logged into the system.

#### 6. Create a new group
```
sudo addgroup `devgroup`
```
- Creates a group named `devgroup`.

#### 7. Add user to group
```
sudo usermod -aG devgroup devuser
```
- Adds `devuser` to the `devgroup` group (-aG means append to group).

#### 8. Verify group membership
```
groups devendar
```
- Lists all groups devendar is part of.


### ✅ Step 2: File Permissions and Ownership
#### 1. Create an empty file
```
touch test.txt
```
- Creates a new, empty file called `test.txt`.

#### 2. Check file permissions
```
ls -l
```
- Lists files in long format with permissions, owner, group, and size.

#### 3. Change file permissions
```
chmod 764 test.txt
```
- Sets permissions:  
-rwxrw-r--  
  - Owner: 7 = read, write, execute
  - Group: 6 = read, write
  - Others: 4 = read

```
chmod g-w test.txt
```
- Sets permission:  
-rwxr--r--  
  - Owner: 7 = read, write, execute
  - Group: 4 = read
  - Others: 4 = read

```
chmod o-w test.txt
```
- Sets permission:
-r-xr--r--
  - Owner: 5 = read, execute
  - Group: 4 = read
  - Others: 4 = read

```
chmod o+w test.txt
```
- Sets permission:
-rwxr--r--
  - Owner: 7 = read, write, execute
  - Group: 4 = read
  - Others: 4 = read

#### 4. Change ownership of file
```
sudo chown devuser:devgroup test.txt
```
- Changes file owner to `devuser` and group to `devgroup`.

#### 5. Check numeric permission representation
```
stat test.txt
```
- Shows detailed file status, including permissions in octal (e.g., 0764).


### ✅ Step 3: Managing Services with systemctl
#### 1. Check if port 80 is listening (for webserver)
```
sudo ss -tuln | grep :80
```
- Verifies that a service (like Nginx) is listening on port 80.

#### 2. Start Nginx service
To start the service, first install `nginx` in the instance  
```
sudo apt update
sudo apt install nginx -y
```
Then:  
```
sudo systemctl start nginx
```
- `Starts` the `Nginx` web server.

#### 3. Check service status
```
sudo systemctl status nginx
```
- Displays whether `Nginx` is active, loaded, and running or dead.

#### 4. Enable service at boot
```
sudo systemctl enable nginx
```
- Makes sure `Nginx` automatically starts on system reboot.

#### 5. Disable service at boot
```
sudo systemctl disable nginx
```
- Prevents `Nginx` from starting automatically on reboot.

#### 6. Check if a service is enabled at boot
```
systemctl is-enabled nginx
```
- Returns `enabled` or `disabled` based on boot-time status.

#### 7. Stop the Nginx service
```
sudo systemctl stop nginx
```
- Gracefully `stops` the web server.

#### 8. Restart the Nginx service
```
sudo systemctl restart nginx
```
- `Stops` and `starts` `Nginx` again (used when configs are changed).

#### 9. Reload the service (if config changes made without stopping)
```
sudo systemctl reload nginx
```
- Applies configuration changes without downtime.
