"""
Following program demonstrates data conversion or casting
"""

num1 = 99.23  # this is a float data
print("{} is of datatype {}".format(num1, type(num1)))

num2 = 23  # this is integer data
print("{} is of datatype {}".format(num2, type(num2)))

num3 = 150  # this is anothr integer
print("{} is of datatype {}".format(num3, type(num3)))

string1 = "100"  # this is a string
print("{} is of datatype {}".format(string1, type(string1)))

print()
# starting the conversion or data cast in code that follows
print("casting float num1 to int")
int_num1 = int(num1)  # knocks off the decimal part of num1
print("{} is of datatype {}".format(int_num1, type(int_num1)))

print("casting integer num2 to float")
float_num2 = float(num2)  # converting num2 to float
print("{} is of datatype {}".format(float_num2, type(float_num2)))

print("casting integer num3 to string")
str_num3 = str(num3)  # converting num3to string
print("{} is of datatype {}".format(str_num3, type(str_num3)))

print("casting string string1 to integer")
int_string1 = int(string1)  # this is a string
print("{} is of datatype {}".format(int_string1, type(int_string1)))
