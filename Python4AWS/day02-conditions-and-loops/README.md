# 🐍 Python Day 02 – Conditions & Loops

## 📅 Date: July 23, 2025  
## 🧠 Concepts Practiced:
- `if`, `elif`, `else` – Conditional branching
- `for`, `while` – Looping structures
- `range()` – Sequence generation
- `break`, `continue` – Loop control

---

## ✅ Code Summary

### 1️⃣ Age Classifier
```
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age.")
elif age < 18:
    print("You are a minor.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
```

### 2️⃣ Score to Grade
```
marks = int(input("Enter your score out of 100: "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 45:
    print("Grade: C")
else:
    print("Grade: Fail")
```

### 3️⃣ `for` Loop with `range()`
```
for i in range(1, 11):
    print(i)
```

### 4️⃣ `while` Loop Countdown
```
n = 10
while n > 0:
    print(n)
    n -= 1
```

### 5️⃣ `Break` & `Continue` in Loop
```
for i in range(1, 11):
    if i == 4:
        continue
    if i == 8:
        break
    if i % 2 == 0:
        print(i)
```

### 📝 Observations
- `range(start, stop)` excludes `stop`
- `break` exits loop early
- `continue` skips current iteration
- Use int(input("Enter a number: ")) for user input
- Use print(n, end=" ") for same-line output in loops
- Avoid unnecessary else blocks — Python loves clarity!
