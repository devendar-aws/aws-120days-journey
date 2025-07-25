# List basics

fruits = ["cherry", "banana", "apple"]
print(fruits[0])            # Indexing                  # apple
print(fruits[-1])           # Negative indexing         # cherry
print(fruits[1:3])          # Slicing                   # ['banana', 'apple']

# List Methods

fruits.append("orange")     # Add to end                # ['cherry', 'banana', 'apple', 'orange']
fruits.remove("banana")     # Remove item               # ['cherry', 'apple', 'orange']
fruits.sort()               # Sort in-place             # ['apple', 'cherry', 'orange']
fruits.reverse()            # Reverse order             # ['orange', 'cherry', 'apple']
print(len(fruits))          # Length of list            # 3
print(fruits)                                           # ['orange', 'cherry', 'apple']

# Iteration

for fruit in fruits:
    print(fruit, end=" ")                               # orange cherry apple

# List Comprehension

squares = [x**2 for x in range(1, 6)]
print(squares)                                          # [1, 4, 9, 16, 25]


# Tuples

coordinates = (10, 20)
print(coordinates[0])
# coordinates[0] = 15                                  Error: tuples are immutable (can't be changed)

# Tuple unpacking

x = coordinates[0]
y = coordinates[1]
print(f"X:{x} Y:{y}")

X, Y = coordinates
print(f"X:{X} Y:{Y}")