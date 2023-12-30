"""
This file dislays some logical error
examples.
"""

# example 1
number = input("Enter any number: ")
print(f"The number entered is {number}")
print(f"Double the number is {number*2}")  # trying to double number enetered as string literal
print(f"Triple of the number is {number*3}")  # trying to Triple number enetered as string literal

import random
system_guess = random.randint(1,10)
print(f"The randomly generated number is: {system_guess}")
for i in range(1,system_guess):
    if i > 5:
        print("Passed")
    elif i< system_guess:
        print("failed")
    elif i == system_guess:
        print("pronto")
    else:
        print("Nothing more to do here!!!")
        
        # the code never runs to display pronto as 1 is never equal to system guess