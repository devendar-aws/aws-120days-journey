# Ì∞ç Python Day 4 ‚Äî Lists & Tuples

**Date:** July 25, 2025  
**Focus:** Indexing, slicing, methods, iteration, list comprehensions

---

## ‚úÖ Topics Covered

### Ì¥π Lists
- **Definition**: Ordered, mutable sequences of items.
- **Common Operations**:
  - Indexing: `my_list[0]`
  - Slicing: `my_list[1:4]`
  - Iteration: `for item in my_list:`
  - List Comprehension: `[x for x in list if condition]`
  - Methods: `.append()`, `.pop()`, `.remove()`, `.sort()`, `.reverse()`

### Ì¥π Tuples
- **Definition**: Ordered, immutable sequences of items.
- **Why Use Tuples**:
  - Safer than lists (immutable)
  - Slightly faster
  - Good for fixed data (e.g., coordinates, config)
- **Unpacking**:
```
  name, age = ("Alice", 28)
  print(f"{name} is {age} years old")
```
## Ì∑† Practice Patterns
|  # | Problem         | Description                                               |
| -- | --------------- | --------------------------------------------------------- |
|  1 | Even Numbers    | Printed even numbers from a list using list comprehension |
|  2 | Tuple Access    | Accessed items using indexing                             |
|  3 | Tuple Unpacking | Unpacked tuple values and used in a loop                  |
|  4 | Inventory Loop  | Looping through tuple-list to show items and counts       |

## ‚úçÔ∏è Example Snippet
```
### List Comprehension Example
even_nums = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", even_nums)

### Tuple Unpacking Example
inventory = [("apple", 10), ("banana", 5), ("orange", 8)]
for fruit, qty in inventory:
    print(f"We have {qty} {fruit}s")
```
## Ì¥ö Summary
- Lists are mutable, while tuples are immutable.
- List comprehension makes filtering easy.
- Tuple unpacking improves readability when looping over structured data.
