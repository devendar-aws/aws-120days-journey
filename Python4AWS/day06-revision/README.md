# 📅 Day 06 - Python Inventory Tracker & Revision (Days 01–05)

## ✅ What I Learned Today

### 1. **Dictionaries Practice**
- Accessing values using `dict[key]` and checking existence with `if key in dict`.
- Updating and modifying dictionary values (e.g., reducing stock on sale).
- Using `.get()` method for safe access and `.items()` for looping through key-value pairs.

### 2. **Custom Functions**
- Created `add_fruit()` and `sell_fruit()` functions to manipulate inventory.
- Designed `update_inventory()` to reflect stock changes.
- Practiced writing clean, modular, reusable functions.

### 3. **Real-World Application: Inventory Tracker**
- Built a CLI (command-line interface) based fruit stock tracker:
  - `add` → Add new fruit or update quantity.
  - `sell` → Reduce fruit quantity with error checking.
  - `show` → Display all current stock.
  - `exit` → End the program.
- Applied dictionary logic, conditionals, loops, and `input()` to simulate a working system.

---

## 🧠 Python Concepts Revised (Days 01–05)

| Concept        | Practiced Examples                            |
|----------------|-----------------------------------------------|
| Print & Variables | `print()`, `x = 10`, basic arithmetic       |
| Conditionals   | `if`, `elif`, `else`                          |
| Loops          | `for`, `while`, `range()`                     |
| Lists          | Indexing, slicing, appending, list comps      |
| Dictionaries   | Accessing, modifying, `.get()`, `.items()`    |
| Functions      | `def func_name(params):` syntax               |

---

## 🧪 Revision Quiz (My Answers)

1. `print("10" * 5)` → `1010101010`
2. `x = 8`... → prints **"Medium"**
3. Loop with `range(1, 8, 2)` → runs **4 times**
4. `print(None, 0)` → **`None 0`**
5. Set operations → Intersection: `{3}`, Union: `{1,2,3,4,5}`, Difference: `{1,2}`

---

## 🔍 Real-World Task: Inventory Tracker

```python
Inv_Tracker = {}
```
# Actions: add, sell, show, exit  
# Handled via while loop and custom functions  
Sample Output:  
What do you want to do? (add/sell/show/exit): add  
Enter fruit name: Mango  
Enter quantity in kg: 5  
Mango added. Current stock: 5 kg  
