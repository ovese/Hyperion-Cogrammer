# practicing the use of variables from example 1

name = "John"
print(name)
print("the variable stored in name is: ", name)
print("Wrong way to do this...The variable stored in name is {}", format(name))
print("Correct way to do this...The variable "
      "stored in name is {}".format(name))

"""
This is a comment block where i start the task
solutions from the first example
I have also used pycodestyle to check the consistency
of the code written
"""
print("hello world")
print()
print("another hello world after blank line")

print("Python variables use snake casing")
greeting_phrase="hello le monde"
print("testing input")

var_name=input("Please enter your name ")
print("Hello "+var_name+"!")

print('Adding comments to all the code')
print(' Two comment styles..single and block comments')

# The rest of the code is only additional work by myself
# printing a string variable
var_string = "Vladimir"
print(var_string)
print("{} is a string type".format(var_string))
print("data type of {} is ".format(var_string), type(var_string))

# printing a float variable
var_float = 3.142
print(var_float)
print("{} is a float type".format(var_float))
var_float=float(input("Enter a float value "))
print("The float value entered is {}".format(var_float))

# printing a integer variable
var_int = 19
print(var_int)
print("{} is of integer type".format(var_int))
print("data type of {} is ".format(var_int), type(var_int))
var_int=int(input("Enter a float value "))
print("The integer value entered is {}".format(var_int))

# printing a boolean variable
var_bool = True
print(var_bool)
print("{} is of boolean type".format(var_bool))
print("data type of {} is ".format(var_bool), type(var_bool))
