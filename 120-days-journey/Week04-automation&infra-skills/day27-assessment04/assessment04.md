# 🧪 Assessment 04 — Day 27

## 🧠 Quiz 1: Cron (9 Questions)

| Q# | Question Summary                                      | Your Answer | Correct | Explanation |
|----|-------------------------------------------------------|-------------|---------|-------------|
| 1  | `0 5 * * *`                                           | B           | ✅      | Daily at 5 AM |
| 2  | `*/10 * * * *`                                        | C           | ✅      | Every 10 minutes |
| 3  | Every Monday at 6:30 AM                               | A           | ✅      | `30 6 * * 1` |
| 4  | chmod for `rwxr-xr--`                                 | B           | ✅      | 754 |
| 5  | Who can edit `-rw-r--r--`                             | A           | ✅      | Only owner |
| 6  | Schedule job every 10 minutes                         | A           | ✅      | `*/10 * * * *` |
| 7  | Cron file for current user                            | B           | ❌      | Correct: C (`crontab -e`) |
| 8  | `0 2 * * * /home/user/backup.sh`                      | B           | ✅      | 2 AM daily |
| 9  | `*/15 9-17 * * 1-5` meaning                           | A           | ✅      | 15-min intervals on weekdays |

**🧾 Score: 8 / 9**

---

## 🧠 Quiz 2: Linux Permissions (10 Questions)

| Q# | Question Summary                                      | Your Answer | Correct | Explanation |
|----|-------------------------------------------------------|-------------|---------|-------------|
| 1  | `-rwxr-xr--` meaning                                  | A           | ✅      | Owner: rwx, Group: r-x, Others: r-- |
| 2  | Recursively change permissions                        | C           | ✅      | `chmod -R` |
| 3  | Make script executable by all                         | B           | ✅      | `chmod a+x` |
| 4  | Numeric value of `rwxr-xr--`                          | B           | ✅      | 754 |
| 5  | What does 6 represent                                 | B           | ✅      | Read + write |
| 6  | `chmod o+x` affects?                                  | A           | ❌      | Correct: C (Others) |
| 7  | Full permission for owner only                        | A           | ✅      | 700 |
| 8  | Secure config file permission                         | D           | ❌      | Correct: B (600) |
| 9  | Group-only read                                       | A           | ❌      | Correct: B (440) |
| 10 | Owner read/write only                                 | C           | ✅      | `rw-------` |

**🧾 Score: 7 / 10**

---

## 🧠 Bonus Quiz: Linux Permissions + Cron (5 Questions)

| Q# | Question Summary                                      | Your Answer | Correct | Explanation |
|----|-------------------------------------------------------|-------------|---------|-------------|
| 1  | What does `S` mean in `-rw-r-Sr--`                    | —           | ❌      | Correct: B (Setgid, no execute) |
| 2  | Cron every 10 mins, weekdays, working hours           | B           | ✅      | `*/10 9-17 * * 1-5` |
| 3  | Directory listable but not readable/writable          | D           | ✅      | `011` (x only) |
| 4  | What `chmod 2755` does                                | —           | ❌      | Correct: A (setgid + rwxr-xr-x) |
| 5  | Common cause for cron not working                     | D           | ✅      | All of the above |

**🧾 Score: 3 / 5**  
(*2 skipped due to unfamiliarity, not counted as wrong in this score.*)

---

## 🧠 Quiz 3: CI/CD (10 Questions)

| Q# | Question Summary                                      | Your Answer | Correct | Explanation |
|----|-------------------------------------------------------|-------------|---------|-------------|
| 1  | CI means?                                             | B           | ✅      | Continuous Integration |
| 2  | Tool for CI                                           | GitHub      | ✅      | GitHub Actions is valid |
| 3  | Purpose of Continuous Deployment                      | C           | ✅      | Auto release to production |
| 4  | GitHub Actions trigger                                | A           | ✅      | Commit or PR |
| 5  | What are `jobs`?                                      | B           | ❌      | Correct: D (independent units of work) |
| 6  | File path for GitHub Actions workflow                 | D           | ✅      | `.github/workflows/*.yml` |
| 7  | `runs-on` keyword                                     | C           | ✅      | OS/environment |
| 8  | Purpose of `secrets`                                  | B           | ✅      | Secure credentials |
| 9  | Practice to keep code always deployable               | A           | ✅      | Continuous Delivery |
| 10 | What does `steps` define?                             | C           | ✅      | Sequence of tasks in a job |

**🧾 Score: 9 / 10**

---

## ✅ Final Summary for Day 27

| Quiz                       | Total Questions | Correct Answers | Score (%) |
|---------------------------|------------------|------------------|-----------|
| Cron Quiz                 | 9                | 8                | 88.9%     |
| Linux Permissions         | 10               | 7                | 70%       |
| Bonus (Hard)              | 5                | 3                | 60%       |
| CI/CD                     | 10               | 9                | 90%       |

**🎯 Total Questions Attempted:** 34  
**✅ Correct:** 27  
**📊 Overall Accuracy:** ~79.4%

💡 **Feedback**:
- Excellent command on cron expressions and CI/CD concepts.
- Linux file permissions are good, but slight improvements needed on group/others level nuances and setuid/setgid bits.

---

