
for i in range(1,4):
    print(i)
    i=10
    # print(i)
print(i)

my_string="the brown fox jumped over the dog"
my_new_string=my_string[0:len(my_string):+1]
print(my_new_string)

my_new_string=my_string[0:len(my_string):+2]
print(my_new_string)

my_new_string=my_string[0:len(my_string):-1]
print(my_new_string)

my_new_string=my_string[len(my_string)::-1]
print(my_new_string)