## Day 02 Practice

# Even or Odd
n = int(input("Enter a number: "))
if n % 2 == 1:
    print(f"{n} is an Odd number")
else:
    print(f"{n} is an Even number")

# Even or Odd counter
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"{i} - Even")
    else:
        print(f"{i} - Odd")
           

# Fizz Buzz
for n in range(1, 51):
    if n % 3 == 0 and n % 5 == 0:
        print(f"{n} FizzBuzz")
    elif n % 3 == 0:
        print(f"{n} Fizz")
    elif n % 5 == 0:
        print(f"{n} Buzz")
    else:
        print(n)


# Factorial with while
n = int(input("Enter a number: "))
factorial = 1
temp = n

while temp > 1:
    factorial *= temp
    temp -= 1

print(f"{n}! = {factorial}")


# Password Attempt Checker
correct_password = "secret123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered = input("Enter password: ")
    if entered == correct_password:
        print("Access granted")
        break
    else:
        print("Incorrect password")
        attempts += 1

if attempts == max_attempts:
    print("Too many attempts")


# Sum of Even Numbers (1–100)
total = 0
for n in range(1, 101):
    if n % 2 == 0:
        total += n
print("Sum of even numbers from 1 to 100 is:", total)

# Print First 10 Multiples of a Number (Input by User)
n = int(input("Enter a number: "))
print(f"First 10 multiples of {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# Prime Number Checker
n = int(input("Enter a number: "))
is_prime = True

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break

if n > 1 and is_prime:
    print(f"{n} is a Prime number")
else:
    print(f"{n} is not a Prime number")


# Print All Prime Numbers Between 1 to 50
print("Prime numbers between 1 and 50:")
for n in range(2, 51):
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")


# Skip Multiples of 4
for n in range(1,21):
    if n % 4 ==0:
        continue
    else:
        print(n)
# OR
for n in range(1,21):
    if n % 4 ==0:
        continue
    print(n)
