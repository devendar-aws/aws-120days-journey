# 📘 Week 03 Summary – July 20 to 26, 2025

**Theme:** Serverless Foundations – Lambda, API Gateway, DynamoDB  
**Days Covered:** Day 15 to Day 21  
**Main Project:** ✅ TODO App using Lambda + API Gateway + DynamoDB

---

## 🧠 What I Learned This Week:

- Learnt **Lambda basics** – how to write Python functions in the Lambda environment
- Understood **DynamoDB basics** – tables, partition keys, boto3 usage
- Explored **what API Gateway is** and how it acts as a trigger for Lambda
- **Integrated Lambda + API Gateway + DynamoDB** to build a full working CRUD app
- Learnt how to **check CloudWatch Logs** for debugging errors in real-time
- Understood the **payload flow** from user → API → Lambda → DB
- Implemented **status codes**, basic **error handling**, and modular Lambda logic

---

## 🚧 Project 02: Lambda-Powered TODO App

A simple serverless TODO list with the following features:

| HTTP Method | Action         | Function |
|-------------|----------------|----------|
| POST        | Create a task  | Lambda writes to DynamoDB |
| GET         | Read all tasks | Lambda scans table        |
| PUT         | Update a task  | Lambda updates item by taskId |
| DELETE      | Remove a task  | Lambda deletes item       |

- ✅ Used `taskId` as **Partition Key**
- ✅ Full CRUD flow implemented using cURL and browser
- ✅ Modular Lambda handler based on `event['httpMethod']`
- ✅ All debugging done through **CloudWatch Logs**

---

## 📊 Assessment 03 – Concepts Check

On Day 21, I wrote answers to 6 reflection questions:

- What is payload?
- Who is the client?
- Role of `taskId` in DynamoDB
- PUT request logic flow
- Why error handling matters
- Why status codes are important

✅ Answered all honestly. It helped reinforce the full Lambda → DB → Client flow.

---

## 🧘 Reflections

> Before this week, Lambda and DynamoDB were just words.  
> Now, I feel I can **build real working backend systems** with just Python and a few AWS services.  
> It was frustrating at times, but with every error I debugged via CloudWatch, I grew stronger.

---

## ⛳️ Week Completion:  
✅ 100% Complete – Project, Conceptual Understanding, Assessment, and Real Learning.
