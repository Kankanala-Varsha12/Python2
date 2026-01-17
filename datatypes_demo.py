# datatypes_demo.py
# This program demonstrates Python data types, type casting,
# arithmetic operations, error handling, and dynamic typing.

# --------- Declaring variables of different data types ---------

# Integer type
num_int = 10

# Float type
num_float = 25.5

# String type
text = "Python"

# Boolean type
is_learning = True

# --------- Printing values and their data types ---------

print("Value:", num_int, "| Type:", type(num_int))
print("Value:", num_float, "| Type:", type(num_float))
print("Value:", text, "| Type:", type(text))
print("Value:", is_learning, "| Type:", type(is_learning))

# --------- Arithmetic operations using numeric variables ---------

sum_result = num_int + num_float
difference = num_float - num_int
product = num_int * 2
division = num_float / 5

print("\nArithmetic Operations:")
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)

# --------- Type casting with user input ---------

try:
    # Taking input as string
    user_input = input("\nEnter a number: ")

    # Converting string input to integer
    int_value = int(user_input)

    # Converting string input to float
    float_value = float(user_input)

    print("Integer value:", int_value)
    print("Float value:", float_value)

except ValueError:
    # This block executes if conversion fails
    print("Invalid input! Please enter a numeric value.")

# --------- Concatenating strings and numbers properly ---------

age = 21

# Convert number to string before concatenation
message = "My age is " + str(age)
print("\n" + message)

# --------- Demonstrating dynamic typing ---------

value = 100
print("\nValue:", value, "| Type:", type(value))

# Reassigning variable with a string
value = "Now I am a string"
print("Value:", value, "| Type:", type(value))
