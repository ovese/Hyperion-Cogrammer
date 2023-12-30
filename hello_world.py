"""
The code here is going to demonstrate the following
Variable declaration
Variable definition
data requests using built-in input function
print statements
"""

# declare a varable to hold user name
# the user name is a string or list of charcaters
user_name = input("Enter your name: ")

# print out the entered user name
print("The user name entered is: "+user_name)

# the above print statement uses string
# concatenation to output the user name
# other methods exist as shown below
print("User name is: ", user_name)
print(f"User name is {user_name}")
print("User name is {}".format(user_name))

# I am declaring another variable called age
# age should be a number of integer type
# However, I could also enter age as a string

int_age = int(input("Enter your age: "))
# previous data variable for age entered is a number so
# using string concatenatio for output wont work
# print("The user name entered is: "+int_age)

# printing out age
print("Your age is: ", int_age)
print(f"Your age is {int_age}")
print("Your age is {}".format(int_age))

# using the string for age
str_age = input("Enter your age: ")
# printing out age
print("The user age entered is: "+str_age)
print("User age is: ", str_age)
print(f"User age is {str_age}")
print("User age is {}".format(str_age))

# print hello world
welcome_text = "hello world!!!"
print(welcome_text)
print(f"{welcome_text}")
