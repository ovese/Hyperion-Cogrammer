""" 
this challenge tests 
2 compilation errors
1 runtime error
1 logical error
"""
# print(f"Welcome {my_name} to this challenge")
# on line 7 I try to print a variable that was not defined prior

# the list below has contents firstname, last name, age, street, postcoe and city
my_list = ["Ese", "ovie", "40", "Concord", "NE33 9QB", "Newcastle"]

for item in my_list:
    print(item)
    
list_size = len(my_list)
print(f"The size of the list is: {list_size}")
print(f"Twice my curent age is: {my_list[3]*2}")
# tried to get twice the age but indexed the wrong position
print(f"Twice my current age is: {my_list[2]*2}")
# finally indexed the correct position but the variable is a string

# print(f"Getting last item in the list with {my_list[6]}")
new_list = []
new_list = my_list.append("email")
print(new_list)
# i have tried creating new list and assigning an expanded original list to it wrongly

new_list1 = []
my_list.append("email")
new_list1 = my_list
print(new_list1)

another_list = []
another_list.append("email")
for i in another_list:
    print(item) # another logical error printing the wrong variable item instead of i


