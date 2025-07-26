# Day 05 Practice
student = {"name": "Arjun", "grade": "A", "marks": "92"}

# Practice 1: Use .pop() to remove and capture a value
removed_marks = student.pop("marks")
print("Removed marks:", removed_marks)                          # Removed marks: 92
print("Remaining dictionary:", student)                         # Remaining dictionary: {'name': 'Arjun', 'grade': 'A'}

# Practice 2: Use del to remove a key (no value returned)
del student["grade"]
print("After deletion:", student)                               # After deletion: {"name": "Arjun"}

# Practice 3: Safe .pop() with default
result = student.pop("marks", "Mot available")
print("Popped value:", result)                                  # Popped value: Not available

# Practice 4: KeyError using del

student = {"name": "Arjun"}

# Uncommenting the line below will cause an error
# del student["marks"]

# Instead, check first
if "marks" in student:
    del student["marks"]

else:
    print("Key not found")                                      # Key not found

"""
🧠 Challenge: Student Record Manager

You are given a dictionary representing a student: """

student = {
    "name": "Radha",
    "roll": "007",
    "math": 85,
    "science": 90,
    "english": 88
}
"""
🔸 Perform the following steps using dictionary methods:
        Use .pop() to remove the "english" marks and store it in a variable called removed_english.
        Use del to delete the "roll" key.
        Add a new subject "computer": 95 to the dictionary.
        Print the final dictionary and the value of removed_english.
"""

removed_english = student.pop("english")
del student["roll"]
student["computer"] = 95
print(student)                                                  # {'name': 'Radha', 'math': 85, 'science': 90, 'computer': '95'}
print("Removed English marks:", removed_english)                # Removed English marks: 88

"""
Now a 🔥 Mini-Challenge for you:
You have a dictionary of fruit prices.
Print all fruit names and their prices in this format:

Output Format:
apple costs ₹120 per kg  
banana costs ₹40 per kg  
"""
fruits = {
    "apple": 120,
    "banana": 40,
    "mango": 100,
    "grapes": 60
}

for key, value in fruits.items():
    print(f"{key} costs ₹{value} per kg")


"""
 Small Practice Challenge
"""
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7}

"""Print common elements
Print all unique elements from both sets
Print items in A but not in B"""  
print(set_a.intersection(set_b))
print(set_a.union(set_b))
print(set_a.difference(set_b))


"""
🧠 Challenge: Student Marks Analysis

Write a program that:
Takes a dictionary of student names and their marks.
Adds a new student to the dictionary.
Removes a student from the dictionary.

Prints:
All students and their marks using .items()
The names of students who scored more than 90 using a set.
"""
# Initial dictionary
students = {
    "Arjun": 96,
    "Bhavna": 88,
    "Chitra": 92,
    "Deepak": 85
}

# Add a new student
students["Esha"] = 98

# Removes a student from the dictionary
removed = students.pop("Bhavna")

# Students and their marks using .items()
for student, marks in students.items():
    print(f"{student} : {marks}")

# Name of the students who scored more than 90 using a set
high_scored_students = {name for name, marks in students.items() if marks > 90}
print("Removed Student:", removed)
print("\nStudents who scored more than 90 marks:", high_scored_students)


"""
🧠 Challenge: Inventory Tracker
You run a small fruit store. Do the following:

Create a dictionary where keys are fruit names and values are stock quantities.
A customer buys 2 kg of mangoes and 1 kg of grapes — update the stock.
Add a new fruit (e.g., "kiwi" with 15 kg) to the inventory.
Remove "banana" from the inventory (out of stock).
Print all fruit names and their updated quantities using .items().
Finally, use a set comprehension to get a set of fruits with more than 10 kg in stock.
"""

Inv_Tracker = {"Mango": 18, "Grapes": 5, "Banana": 2}
print("Stock in the inventory:")
for fruit, quantity_kgs in Inv_Tracker.items():
        print(f"{fruit} -> {quantity_kgs}kgs")
print()

Inv_Tracker["Mango"] = 16
Inv_Tracker["Grapes"] = 4
print("After a customer bought 2kg Mangoes and 1kg Grapes, stock is ")
for fruit, quantity_kgs in Inv_Tracker.items():
    print(f"{fruit} -> {quantity_kgs}kgs")
print()
# or
def updated_inventory(stock, fruit, quantity_kgs):
    if fruit in stock:
        stock[fruit] -= quantity_kgs
    else:
         print(stock)
    return stock

updated = updated_inventory(Inv_Tracker, "Mango", 2)
updated = updated_inventory(Inv_Tracker, "Grapes", 1)
print(updated)
print()
# or
updated = updated_inventory(updated_inventory(Inv_Tracker, "Mango", 2), "Grapes", 1)
print(updated)
print()

Inv_Tracker["Kiwi"] = 15
print("After adding 15kg Kiwi to the Inventory: ")
for fruit, quantity_kgs in Inv_Tracker.items():
    print(f"{fruit} -> {quantity_kgs}kgs")
print()

removed_fruit = Inv_Tracker.pop("Banana")
print("After removing Banana from the inventory:")
for fruit, quantity_kgs in Inv_Tracker.items():
    print(f"{fruit} -> {quantity_kgs}kgs")
print(f"{removed_fruit}kgs banana is removed.")
print()

more_fruits = {fruit for fruit, quantity_kgs in Inv_Tracker.items() if quantity_kgs > 10}
print("Fruits that are more than 10kgs:", more_fruits)