# Day 15 – Lambda Basics (20 July 2025)

## ✅ Goals Completed
- Created AWS Lambda function in Python
- Triggered manually via console events
- Explored the `event` object and dynamic JSON parsing
- Used logs to validate output and debugging

## 🔧 Lambda Code (Final)

    import json
    def lambda_handler(event, context):
         for key, value in event.items():
             print(f"{key} = {value}")
         return {
            'statusCode': 200,
            'body': 'Event logged.'
        }

## 🧪 Test Events Used

    {
      "name": "Devendar",
      "task": "Lambda Basics",
      "progress": "Day 15"
    }

## 📘 Key Learnings
- AWS Lambda is stateless and event-driven
- event carries payload data (JSON)
- CloudWatch logs help trace behavior
- Use event.get(key) to safely extract fields
- Code is deployed only after clicking “Deploy”

## 📝 Output

    Logs showed:
    
    name = Devendar
    task = Lambda Basics
    progress = Day 15
