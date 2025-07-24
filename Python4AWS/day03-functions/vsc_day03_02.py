## Day 03 Practice

# Sum of two numbers

def sum_two_numbers(a, b):
    return a+b
addition = sum_two_numbers(int(input("Enter First number:")), int(input("Enter Second number:")))

print(addition)

# Factorial function

n = int(input("Enter a number for factorial:"))
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result
print(f"Factorial of {n} is", factorial(n))

# Prime Checker

n = int(input("Enter a number:"))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(f"{n} is Prime:", is_prime(n))

# Max of three numbers

a = int(input("Enter First number: "))
b = int(input("Enter Second number: "))
c = int(input("Enter Third number: "))

def max_of_three(a, b, c):
    return max(a,  b, c)
result = max_of_three(a, b, c)
print(f"Max of three numbers is", result)
# or
print(f"Max of three numbers is {result}")

# Palindrome Checker

def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

word = (input("Enter a word: "))
result = is_palindrome(word)

if result:
    print(f"{word} is a Palindrome")
else:
    print(f"{word} is not a Palindrome")

