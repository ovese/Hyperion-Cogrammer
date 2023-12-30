# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# animal = Lion
# animal_type = "cub"
# number_of_teeth = 16

# full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

# print full_spec

print(">>>First error was on line 11: SyntaxError due to missing parentheses")
print(">>>Second error was NameError as Lion is not defined and\n"
      " is being passed as a RHval to the variable animal. Adding\n"
      " quotes to make Lion a string literal solved this")
print(">>>The Third error was a Logical error as he program runs but\n "
      " the output is not as it should be, since the variable\n"
      "placeholder names are being displayed as against the values\n"
      " in those variables. Fixed this by appending f at begining of string")
print(">>>Finally on getting the code to run the sentence \n"
      " seemed wrong as two variables needed to be switched \n"
      " to get the correct sense from the sentence\n"
      ",this also was a logical error")

print("\n\n ************Final form of the code is below this line**********")
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

print(full_spec)