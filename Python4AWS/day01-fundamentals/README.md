## ✅ Day 01 – Python Basics: Variables, Input, Printing  
📌 Topics Covered
| Concept              | Description                                                                 |
| -------------------- | --------------------------------------------------------------------------- |
| Variables            | Created variables for name, age, and boolean readiness                      |
| `print()`            | Displaying string, integers, and booleans                                   |
| `type()`             | Checking variable types (str, int, bool)                                    |
| Type casting         | Converted integer to string using `str()`                                   |
| `input()` simulation | Captured user input (e.g., name)                                            |
| String formatting    | Used `+`, `.format()`, and `f-string` for dynamic output                    |
| Simple calculator    | Addition, subtraction, multiplication, division of two numbers (with input) |

### 🧪 Practice Code Samples

#### 1. Variable Declaration

	name = "Devendar"
	age = 32
	is_ready = True

#### 2. Type Check & Casting

	print(type(name))       # <class 'str'>
	print(type(age))        # <class 'int'>
	print(type(is_ready))   # <class 'bool'>
	age_str = str(age)
	print(type(age_str))    # <class 'str'>

#### 3. Input Simulation & Welcome Message

	username = input("Enter your name: ")
	print("Welcome", username)

#### 4. String Formatting Styles

	# Using + operator
	print("Hello, " + name_input + "! You are " + age_input + " years old.")

	# Using format()
	print("Hello, {}! You are {} years old.".format(name_input, age_input))

	# Using f-string
	print(f"Hello, {name_input}! You are {age_input} years old.")

#### 5. Simple Calculator

	a = int(input("Enter First Number: "))
	b = int(input("Enter Second Number: "))
	print(f"Sum: {a + b}")
	print(f"Difference: {a - b}")
	print(f"Product: {a * b}")
	print(f"Quotient: {a / b}")


### 🐍 VS Code Setup Notes

| Tool/Extension    | Status                      |
| ----------------- | --------------------------- |
| Python Extension  | Installed (Microsoft)       |
| Linter: Pylint    | Working (Blue Zigzag Shown) |
| Formatter: Flake8 | Optional, not required now  |
| Python 3.13.5     | Interpreter selected        |
| [`vsc_day01_01.py`](./vsc_day01_01.py) | Code saved and tested       |


### 🚀 Output Example
	Hello, Devendar! You are 32 years old.
	Sum: 20
	Difference: 12
	Product: 64
	Quotient: 4.0
