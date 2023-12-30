choice1=input("enter choice ").lower # only tells you what the lower is
print(choice1)
choice2=input("enter choice ").lower() # executes here
print(choice2)

# built-in method...means look for missing round brackets

# string manip in practice

# external file opening
print("********First way to open an external file********")
f=open("data.txt","r")
print(f.read())
f.close()

print("******Second way to open an external file**********")
with open("data.txt","r") as file:
    data=file.read()

print(data)

for credential in data:
	# print(credential.strip()) # rstrip, lstrip
	data_strip = credential.strip()

for crednetial in data:
	# print(credential.strip().split())
	data_strspl = credential.strip().split()

for crednetial in data:
	# print(credential.strip().split(","))
	data_strspl2 = credential.strip().split(",")

for crednetial in data:
	cleaned_data = credential.strip().split(",")
 
file.close()

# watch youtube for how to debug without printing

# is the code dynamic: if string size is changed, 
# would it cause the code to break

# How i format my string

name="john"
age=34

print(f"{name} and {age}")

# format string is good in fiancial data formatting

deposit=5000000.25645
print(deposit)
print(round(deposit,2))
print(round(deposit,3))
deposit=5000000.2000000035645
print(round(deposit,2))
deposit=5000000000.2000000035645
print(f" your deposit is: ${deposit:,.2f}")
# Capstone task 5 wil use this knowledge above

# how to use Join

# split is almots a cast from string to list

stringvar="a b c e t y u"
string_list=stringvar.split()
print(string_list)
print(stringvar.split())
print("".join(string_list))
print("%".join(string_list))

# stripping,splitting, indexing
print("stripping,splitting, indexing are the 3 main ops to be had with string text")
# task 17

# task 5..basic requirements...do as much as you want, dont limit myself

# try to stretch myself with the capstones and use as much knowledge as i can


# Resource to use
# 1. pythoninstitute.org

# https://pythoninstitute.org/

# 2. Django

# operator should have space befoe and after
# comments might not have to be spread but no
# line in between and comment directly above

# inline comment should be used only for reserved cases 
# whree long lines of code are used on certain variables 
# are declared at an earlier point and used much later

# open linter and check spellings
# especially spelling around comments
# correct spellings is part of professional code

# chriss@hyperiondev.com






