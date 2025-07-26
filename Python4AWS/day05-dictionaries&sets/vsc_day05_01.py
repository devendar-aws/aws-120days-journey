# Creating a Dictionary

person = {
    "name": "Alice",
    "age": 30,
    "city": "Hyderabad"
}
""" "name" is the key, "Alice" is the value
Keys, strings, numbers and tuples must be unique and are immutable"""

# Accessing Values

print(person["name"])
print(person.get("age"))

""" [] will throw an error if key doesn’t exist
.get() will return None or a default value if not found """

""" Create a dictionary called student with keys: "name", "roll", "marks"
Then print:
    Name using []
    Marks using .get()"""

student = {
"name": "Arjun",
"roll": "001",
"marks": "96"
}
print(student["name"])
print(student.get("marks"))
print(student.get("grade", "Not Assigned"))

# Adding a new Key-Value pair
student["grade"] = "A+"
print(student)

# Updating an Existing Value
student["marks"] = "98"
print(student)

# Deleting a Key-value Pair
del student["roll"]
print(student)

# Using .pop() method
student.pop("name")
print(student)

# 3 Key differences between del and .pop() method
# 1. Return value                                  
""" del doesn't return the value whereas, .pop() returns the value of the removed key """
student = {"name": "Arjun", "marks": "95"}
val = student.pop("marks")                     # val = 95
print(val)                                     # You can store or use the value

del student["name"]                            # No value returned
print(student.get("name"))

# 2. Error Handling (Safer Option)
""" del will raise Keyerror if the key doesn't exist. .pop() can avoid that with a default fallback. """
student = {"name": "Arjun"}

# del student["grade"]      # Keyerror
# Safe with pop
print(student.pop("grade", "Key not found"))      # Key not found

# 3. Usage in Logic or Assignments
""" Since .pop() returns the value, it can be used directly. """
marks = student.pop("marks", 0) + 5             # Add 5 marks if key exists, else start from 0.
                                                # del cannot be used this way.

print(student.get("marks", "not found"))
print(student)

""" 
| Feature              | `del`           | `.pop()`             |
| -------------------- | --------------- | -------------------- |
| Returns value?       | ❌ No            | ✅ Yes                |
| Safe if key missing? | ❌ No (KeyError) | ✅ Yes (with default) |
| Use in expressions?  | ❌ No            | ✅ Yes                |

"""

# .items() in dictionary
# .items() is a method that returns each key–value pair from the dictionary as a tuple — in a list-like object.

student = {"name": "Arjun", "roll": "001", "marks": 96}

for key, value in student.items():
    print(key, "->", value)

# Sets in Python
# What is a Set? Unordered, No duplicates, Mutable(can add/remove items)

fruits = {"apple", "banana", "mango"}
print(fruits)                                           # order not guaranteed

# Set Methods & Operations
# 1. add() - Adds an item
fruits.add("orange")
print(fruits)                                           # {"apple", "banana", "mango", "orange"}

# 2. remove() - Removes an item (error if not found)
fruits.remove("banana")
print(fruits)                                           # {"apple", "orange", "mango"}

# 3. discard() - Removes an item (no error if not found)
fruits.discard("papaya")                                # no error
print(fruits)                                           # {"apple", "mango", "orange"}

# 4. union() - Combines two sets
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))                                       # {1, 2, 3, 4, 5}

# 5. intersection() - Common elements
print(a.intersection(b))                                # {3}

# 6. difference() - items only in a, not in b
print(a.difference(b))                                  # {1, 2}
