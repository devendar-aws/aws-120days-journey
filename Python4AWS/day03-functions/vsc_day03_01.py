# Defining Functions (def)

""" Syntax
def function_name(parameters):
     Function Body
    return result
"""
# Example:
def greet(name):
    return f"Hello {name}!"

print (greet("Devendar"))                   # Hello Devendar!

# Parameters and Arguments

def add(a, b):
    return a + b

print (add(5, 3))                           # 8

# Returning Values

def multiply(a, b):
    return a * b

result = multiply(4, 3)
print(result)                               # 12

# Default Arguments

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())                              # Hello, Guest!
print(greet("Devendar"))                    # Hello, Devendar!

# Scope

global_var = 10

def test_scope():
    local_var = 5
    print("Local variable:", local_var)
    print("Global variable:", global_var)
                                            
test_scope()                                # Local variable: 5
                                            # Global variable: 10

                  