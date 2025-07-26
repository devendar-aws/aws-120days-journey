# ✅ Day 05 – Dictionaries & Sets

## 📅 Date: July 26, 2025  
## 🧠 Topics Covered:
- Dictionary basics: key-value pairs
- Accessing values using `[]` and `.get()`
- Adding, updating, and deleting dictionary entries (`dict[key] = val`, `.pop()`, `del`)
- `.items()` method for looping through key-value pairs
- Basic Set concepts: uniqueness, no indexing
- Set operations: `union()`, `intersection()`, `difference()`

---

## 🔸 Practice Highlights:

### 📘 Dictionary Usage
```
student = {
    "name": "Arjun",
    "roll": "001",
    "marks": "96"
}
print(student["name"])         # Access via key
print(student.get("marks"))    # Safe access with .get()
```
## ❌ Difference between `del` vs `.pop()`
- `del dict[key]` deletes key without returning it.
- `dict.pop(key)` deletes key and returns the value.

## 🧪 Final Challenge – Inventory Tracker  
Simulated inventory operations:
- Show current stock
- Reduce stock after a sale
- Add new fruit
- Remove a fruit
- Use set comprehension to filter fruits >10kg

## Function to update inventory:
```
def updated_inventory(stock, fruit, quantity_kgs):
    if fruit in stock:
        stock[fruit] -= quantity_kgs
    return stock
```
## Combined updates in one line:
```
updated = updated_inventory(updated_inventory(Inv_Tracker, "Mango", 2), "Grapes", 1)
```

## ✅ Summary:  
- Mastered dictionary basics and common operations
- Practiced `.items()` and `.get()` safely
- Understood how sets work and applied key operations
- Built a mini inventory management simulation.
