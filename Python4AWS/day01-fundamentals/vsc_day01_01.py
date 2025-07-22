# Basic Variables and printing
name = "Devendar"
age = 32
is_ready = True

print (name)                                                                    #Devendar
print(age)                                                                      #32
print(is_ready)                                                                 #True

# Type check and casting
print(type(name))                                                               #<class 'str'>
print(type(age))                                                                #<class 'int'>
print(type(is_ready))                                                           #<class 'bool'>

age_str = str(age)
print("Age as String:", age_str)                                                #Age as String: 32
print(type(age_str))                                                            #<class 'str'>

# Simulate input (like lambda receives payload)
# This prepares you how Lambda handles API Gateway/event inputs
username = input("Enter your name: ")                                           #Enter your name: Devendar
print("Welcome",username)                                                       #Welcome Devendar (Comma adds space automatically)

# Practice
name_input=input("Enter your name: ")                                           #Enter your name: Devendar
age_input=input("Enter your age: ")                                             #Enter your age: 32
print("Hello,",name_input,"You are",age_input,"years old.")                     #Hello, Devendar You are 32 years old.
print("Hello,",name_input+"!","You are",age_input,"years old.")                 #Hello, Devendar! You are 32 years old.
print(f"Hello, {name_input}! You are {age_input} years old.")                   #Hello, Devendar! You are 32 years old.
print("Hello, {}! You are {} years old.".format(name_input,age_input))          #Hello, Devendar! You are 32 years old.


# Simple Calculator
a= int(input("Enter First Number: "))                                           #Enter First Number: 16
b= int(input("Enter Second Number: "))                                          #Enter Second Number: 4

print("Sum:",a+b)                                                               #Sum: 20
print("Difference:",a-b)                                                        #Difference: 12
print("Product:",a*b)                                                           #Product: 64
print("Quotient:",a/b)                                                          #Quotient: 4.0

# Using f-string
print(f"Sum: {a+b}")                                                            #Sum: 20
print(f"Difference: {a-b}")                                                     #Difference: 12
print(f"Product: {a*b}")                                                        #Product: 64
print(f"Quotient: {a/b}")                                                       #Quotient: 4.0
