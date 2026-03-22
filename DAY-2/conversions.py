# --- 1. SINGLE INPUTS ---
# Simple conversion of string input to integer/float
age = int(input("Enter age: "))
price = float(input("Enter price: "))
name = input("Enter name: ")

print(f"Single values: {age}, {price}, {name}")

# --- 2. MULTIPLE INPUTS (Lists, Tuples, Sets) ---
# [int(x) for x in ...] is a List Comprehension. 
# It loops through the split string and converts each piece.

# List of integers
age_list = [int(x) for x in input("Enter ages (space separated): ").split()]

# List of floats
price_list = [float(x) for x in input("Enter prices (space separated): ").split()]

# Tuple of strings (no conversion needed, just split)
names_tuple = tuple(input("Enter names (space separated): ").split())

# Set of integers (uses curly braces {} to automatically remove duplicates)
numbers_set = {int(x) for x in input("Enter numbers for set (space separated): ").split()}

print(f"List of ages: {age_list}")
print(f"List of prices: {price_list}")
print(f"Tuple of names: {names_tuple}")
print(f"Set of numbers: {numbers_set}")

# --- 3. DICTIONARY INPUT ---
# Dictionary with names and numbers (using eval)
numbers_dict = eval(input("Enter a dictionary of numbers (e.g. {'a': 1, 'b': 2, 'c': 3}): "))
print(numbers_dict)
