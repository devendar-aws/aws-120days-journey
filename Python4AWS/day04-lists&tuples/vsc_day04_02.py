# Day 04 Practice
"""
1. Create a list of 5 cities and:
    Print the second city
    Replace the third city with a new one
    Add a new city at the end
    Remove the first city
    Sort and print the list
"""
cities = ["mumbai","hyderabad","chennai","bangalore","delhi"]
print(cities[1])
cities[2] = "lucknow"
print(cities)
cities.append("chennai")
print(cities)
cities.remove("mumbai")
print(cities)
cities.sort()
print(cities)

"""
2. Write a program that:
    Takes a list of numbers
    Prints only even numbers using list comprehension
"""
even = [x for x in range(1,11) if x % 2 == 0]
print(even)

"""
3. Use a tuple to store a person's (name, age) and print a sentence like:
    "Alice is 28 years old."
"""
person = ("Alice", 28)
print(f"{person[0]} is {person[1]} years old")

name = person[0]
age = person[1]

print(f"{name} is {age} years old")

"""
4. Each tuple contains a fruit name and its quantity in stock.
inventory = [("apple", 10), ("banana", 5), ("orange", 8)]

Task: Write a program that prints:
We have 10 apples
We have 5 bananas
We have 8 oranges """

inventory=[("apple", 10), ("banana", 5), ("orange", 8)]

for f_name, quant in inventory:
    print(f"We have {quant} {f_name}s")