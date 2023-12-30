# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
 
name = "Tim"
    # surname = " Jones"
print(" On line 6 there was an "
      "IndentationError: unexpected indent")
print(" After correcting the IndentationError: ")
surname = " Jones "

age = 21
 
# full_message = name + surname +  is  + age + " years old"
print(" On line 14, there was a SytaxError: invalid "
      "syntax for wrong formating of output")
print(" Finally the age variable is integer type and cant "
      "be concatenated like string except on cast or "
      "if requested as a string from input")
print("After correction of the various errors on line 14, "
      "the final string is")
full_message = name + surname + " is " + str(age) + " years old"
 
print (full_message)

print("Further defensive programming using try-except-else")
print("This part of the program requests input and checks same for "
      "correctness. It uses custom exceptions")

class NotStringInputError(Exception):
    pass

class NotIntegerError(Exception):
    pass


my_name = ""
my_age = ""
def get_details():
    
    my_name = input(" Enter your name: ").upper()
    my_age = input(" Enter your age: ")
    if not my_name.isalpha():
        raise NotStringInputError(f"Name {my_name}, cannot contain a number")
    if not my_age.isdigit():
        raise NotIntegerError(f"Your age {my_age}, must be an integer or number")
    
    return (my_name,my_age)

# this does not use an else
try:
    [name, age] = get_details()
    print(f"Welcome {name}, you are {age} years old")
except NotStringInputError as error1:
    print("There was an error: ",error1)
except NotIntegerError as error2:
    print("There was another error: ",error2)
        
