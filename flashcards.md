## 📇 IAM Flashcards

| Concept | Answer |
|--------|--------|
| What is IAM? | AWS Identity and Access Management |
| Main use of IAM | Securely control access to AWS resources |
| IAM resource types | Users, Groups, Roles, Policies |
| What is an IAM user? | Individual identity with credentials |
| What is an IAM role? | Temporary access with assumed identity |
| What is a policy? | JSON document that defines permissions |
| Default user permissions? | None; must be explicitly granted |
| Root user should be used? | Only for initial setup or emergencies |
| Best practice for IAM? | Least privilege, MFA, use roles |
| Where are IAM logs visible? | AWS CloudTrail |

---

## 📇 S3 Flashcards

| Concept | Answer |
|--------|--------|
| What is S3? | Scalable object storage service |
| S3 stands for? | Simple Storage Service |
| What is a bucket? | A container for storing objects |
| Max file size for upload (single PUT)? | 5 GB |
| How to upload files > 5GB? | Use Multipart Upload |
| Are buckets region-specific? | Yes |
| Default bucket access? | Private |
| How to make a static site? | Enable static hosting + public policy |
| What is an object? | File stored in a bucket with metadata |
| Versioning in S3? | Keeps multiple versions of the same object |

---

## 📇 EC2 Flashcards

| Concept | Answer |
|--------|--------|
| What is EC2? | Virtual server in the cloud |
| AMI stands for? | Amazon Machine Image |
| Instance Types | General (t2, t3), Compute (c5), Memory (r5) etc. |
| What is a key pair? | Used for SSH access (private + public key) |
| Default EC2 port for web server? | Port 80 (HTTP) or 443 (HTTPS) |
| How to access EC2? | Use SSH with `.pem` file |
| What is a Security Group? | Virtual firewall for EC2 |
| What is a VPC? | Virtual Private Cloud – network for EC2 |
| Billing granularity? | Per second (Linux), per hour (Windows) |
| Free Tier EC2 usage? | 750 hours/month (t2.micro or t3.micro) |

---

### 📇 Lambda Basics Flashcards

| Concept | Answer |
|--------|--------|
| What is AWS Lambda? | Serverless compute service that runs code on demand |
| Default handler function name? | `lambda_handler` |
| Input format to Lambda? | `event` (JSON), `context` (runtime info) |
| Where are logs stored? | Amazon CloudWatch |
| How to access a key in `event`? | `event.get("key")` | `event.items()`
| Is Lambda free in Free Tier? | Yes, 1M requests + 400,000 GB-seconds per month |

---

---

##  ~G DynamoDB Flashcards

| Concept | Answer |
|--------|--------|
| What is DynamoDB? | Fully managed NoSQL database by AWS |
| Type of database? | Key-value and document-based |
| What is a primary key? | Uniquely identifies each item (Partition key or Partition + Sort key) |
| Table creation requires? | Table name + primary key definition |
| Read/Write modes? | On-demand or Provisioned |
| SDK to access DynamoDB in Python? | `boto3` |
| Default consistency model? | Eventually consistent (Strong optional) |
| What is a Partition Key? | Determines how data is distributed across partitions |
| How is data retrieved? | Using `GetItem`, `Query`, or `Scan` |
| Best practice for querying? | Use indexes, avoid full table scans |

---

##  ~G API Gateway Flashcards

| Concept | Answer |
|--------|--------|
| What is API Gateway? | Managed service to create and expose APIs |
| Types of APIs supported? | REST, HTTP, WebSocket |
| API Gateway integrates with? | Lambda, EC2, any backend |
| Common methods used? | GET, POST, PUT, DELETE |
| What is a Resource? | URL path like `/tasks` |
| What is a Method? | Operation on a resource (e.g., GET on `/tasks`) |
| Test method in console? | Use "Test" button after selecting a method |
| Deployment requirement? | Create a stage (e.g., `dev`, `prod`) |
| Endpoint type used? | Regional, Edge-Optimized, Private |
| Error troubleshooting tip? | Check method integration, logs, permissions |

---

##  ~G CloudWatch Logs Flashcards

| Concept | Answer |
|--------|--------|
| What is CloudWatch Logs? | Logging service for AWS resources |
| Where are Lambda logs stored? | Under Log Groups > `/aws/lambda/<function-name>` |
| What is a Log Stream? | Individual stream of logs per invocation or instance |
| How to log from Lambda? | Use `print()` in Python code |
| Do logs auto-create? | Only after function is invoked |
| Log retention default? | Never expires unless manually set |
| Useful for debugging? | Yes, can trace errors and outputs |
| How to view logs? | Console > CloudWatch > Logs |
| Can we filter logs? | Yes, with Filter patterns |
| Cost control tip? | Set retention and export logs if needed |

---

##  ~G Lambda CRUD Integration Flashcards

| Concept | Answer |
|--------|--------|
| What does CRUD stand for? | Create, Read, Update, Delete |
| What service handles business logic? | AWS Lambda |
| What handles HTTP requests? | API Gateway |
| Where is data stored? | DynamoDB |
| SDK used in Lambda for DynamoDB? | `boto3.resource("dynamodb")` |
| How to test locally? | Use `curl` with API endpoint |
| Common error source? | Region mismatch or IAM role permissions |
| Best logging practice? | Use structured logs for inputs/outputs |
| Key deployment step in API Gateway? | Deploy to a Stage (e.g., `dev`) |
| Response format in Lambda? | JSON with `statusCode` and `body` |


