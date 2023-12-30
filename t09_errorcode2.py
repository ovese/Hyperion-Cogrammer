# declare the user defined exceptions 
# to be used in this file, which 
# inherit from parent exceptions class
class NotStringInputError(Exception):
    pass

class NotIntegerError(Exception):
    pass

# declare user variables here
my_name = ""
my_age = ""

# define a function where the exceptios will be raised
def get_details():
    
    my_name = input(" Enter your name: ").upper()
    my_age = input(" Enter your age: ")
    if not my_name.isalpha():
        raise NotStringInputError(f"Name {my_name}, cannot contain a number")
    if not my_age.isdigit():
        raise NotIntegerError(f"Your age {my_age}, must be an integer or number")
    
    return (my_name,my_age)

# call the function here and check for correct input
# it also uses an else block
try:
    [name, age] = get_details()
    # print(f"Welcome {name}, you are {age} years old")
except NotStringInputError as error1:
    print("There was an error: ",error1)
except NotIntegerError as error2:
    print("There was another error: ",error2)
else:
    print(f"Welcome {name}, you are {age} years old")
