# Day 3: Static Website Hosting on AWS S3 🌐

📅 **Date:** July 8, 2025  
📦 **Project:** Deploy a public website using AWS S3  
🎯 **Goal:** Host a fully accessible HTML site using S3, understand bucket policies and static hosting

---

## ✅ Key Steps

1. Created S3 bucket `dev-s3-day3` in `ap-south-1`
2. Disabled Block Public Access (all 4 options)
3. Uploaded `index.html`
4. Enabled Static Website Hosting in bucket properties
5. Added public read bucket policy
6. Tested website via S3 endpoint

---

## 🖥️ Website Endpoint

🌐 [View Site](http://dev-s3-day3.s3-website.ap-south-1.amazonaws.com)

---

## 🔐 Bucket Policy Used

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::dev-s3-day3/*"
    }
  ]
}

💡 Reflections

    This was my first real project on AWS.

    Learned how S3 works beyond just storage — hosting, access policies, and static sites.

    Now confident in deploying HTML-based public content on the cloud.

📁 Artifacts

    index.html — The site’s content

    bucket-policy.json — For public read access

    README.md — This file documenting the process
