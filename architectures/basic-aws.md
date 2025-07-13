                      🌐 Internet
                          │
            ┌─────────────▼─────────────┐
            │      AWS Global Infra     │
            └─────────────┬─────────────┘
                          │
          ┌───────────────▼───────────────┐
          │        AWS Region (e.g.,      │
          │        ap-south-1)            │
          └───────────────┬───────────────┘
                          │
              ┌───────────▼───────────┐
              │       IAM User        │
              │  (access via CLI/API) │
              └───────────┬───────────┘
                          │
          ┌───────────────▼───────────────┐
          │         S3 Bucket             │
          │  - Stores files/HTML assets   │
          │  - Public or private access   │
          └───────────────────────────────┘
                          │
                          ▼
          https://<bucket>.s3.amazonaws.com/<file>

          ┌─────────────────────────────┐
          │           EC2              │
          │ - Compute instance         │
          │ - Host web servers         │
          │ - Connect via SSH (port 22)│
          └─────────┬──────────────────┘
                    │
                    ▼
           Internet Gateway (via VPC)
