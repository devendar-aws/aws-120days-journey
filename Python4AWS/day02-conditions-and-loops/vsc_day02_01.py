## Conditions Practice

# If-elif-else
# Ask for user's age and check voting eligibility

age = int(input("Enter your age: "))

if age <= 0:
    print ("Invalid age.")
elif age < 18:
    print("You are a minor. You are not eligible to vote.")
elif age < 60:
    print("You are an adult. You are eligible to vote.")
else:
    print("You are a senior citizen. You are eligible to vote.")

# Simple Grade Checker

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

# For Loop + Range

print("Numbers from 1 to 10: ")
for i in range(1, 11):
    print(i)

# While loop
# Print numbers from 10 to 1 using while loop

n = 10
while n > 0:
    print(n)
    n-=1

# Break and Continue
# Print even numbers, skip 4, break at 8

for i in range(1, 11):
    if i == 4:
        continue
    if i == 8:
        break
    if i % 2 == 0:
        print(i)
