## Cheat sheet comparing Bash scripting and GitHub Actions workflows:
| Feature                | Bash Script                       | GitHub Actions Workflow                    |
| ---------------------- | --------------------------------- | ------------------------------------------ |
| File Type              | `.sh`                             | `.yml` under `.github/workflows/`          |
| Run Location           | Locally (Linux/macOS terminal)    | GitHub-hosted runner (cloud)               |
| Trigger Method         | Manually (or via `cron`)          | Automatically (on push, PR, schedule, etc) |
| Language               | Bash                              | YAML + GitHub Actions syntax               |
| Use Cases              | Local automation, backups, builds | CI/CD, tests, deployments, cloud tasks     |
| Toolchain Needed       | Bash, Shell, Terminal             | GitHub account, GitHub repo, Actions setup |
| Access to AWS CLI etc. | Direct (installed locally)        | Requires secrets + `aws-cli` action        |
| Output Visibility      | Terminal or log files             | GitHub Actions UI (Logs per step)          |
| Parallel Jobs          | Manual scripting                  | Built-in support with `jobs:`              |
| Ecosystem              | Independent/local                 | Integrated with GitHub ecosystem           |

---

