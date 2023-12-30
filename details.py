"""
This tasks requests user information and prints out
in an agreed format
Some of  the requested infrmation are strings
other are alphanumeric and others numbers
"""

user_name = input("Enter your full name: ")  # name is a string
user_age = int(input("Enter your age: "))  # age is a number or interger
house_number = input("Enter your house number: ")  # house number can be alpha-numeric
street_name = input("Enter your street name: ")  # street name is a string

# printing output in requested format
print(f"This is {user_name}. He is {user_age} years old and "
      " lives at house number {house_number} on {street_name}")
