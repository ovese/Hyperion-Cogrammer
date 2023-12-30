"""
PUZZLE
The Husbands' Names
Using the power of deduction to solve a logic grid puzzle

The next logic puzzle provides a series of clues, and requires you to analyse and synthesise the information in order to make deductions, much like the classical detective Sherlock Holmes solving a case. Part of what can be challenging about this sort of puzzle is working out how to represent the information so it is easy to keep track of, and so that it best supports intelligent deductions. This sort of puzzle is sometimes called a logic grid puzzle; we suggest you start by experimenting with creating a grid to capture the information and see what you can deduce!

Upon returning from a year long working holiday, Alberta, the youngest of 4 sisters, announced her whirlwind marriage. Her 3 sisters, Carla, Paula, and Roberta, were amazed by her husband’s name.
The 4 men are Albert, Carl, Paul, and Robert. Their last names are Albertson, Carlson, Paulson, and Robertson.
No woman’s husband has a first name that consists of her first name without the final “a”; no woman’s last name consists of her first name without the final “a” and with “son” on the end; and, no man’s last name consists of his first name with “son” added at the end.
Paul is not married to Roberta, and Robert is not married to Paula.
No husband and wife have “bert” in both their first names, but there is a man who has “bert” in his first and last names.
Carl’s last name is not Paulson.

Work out Alberta’s husband’s first and last name, as well as Carla’s, Paula’s, and Roberta’s husbands’ first and last names.
Enter your answer here
******************
Algorithm for how many letetsr occur in text

Create a variable to store the given string "You can have data without information, but you cannot have information without data."
Convert the given string to lowercase
Create a list containing every lowercase letter of the English alphabet 

for every letter in the alphabet list:
    Create a variable to store the frequency of each letter in the string and assign it an initial value of zero
    for every letter in the given string:
        if the letter in the string is the same as the letter in the alphabet list
            increase the value of the frequency variable by one.
    if the value of the frequency variable does not equal zero:
        print the letter in the alphabet list followed by a colon and the value of the frequency variable


**************************
"""
print("Hello World")
my_name=input("Enter your name: ")
print("Welcome "+my_name)

my_salary=1250
my_rent=650
my_utilities=175
my_expenditures=my_rent+my_utilities
print("My salary is: "+str(my_salary))
print("My rent is: "+str(my_utilities))
print("My total expenditure is: "+str(my_expenditures))
amount_left=my_salary-my_expenditures
print("Balance after expenbditures: "+str(amount_left))
christmas_savings=0.25*amount_left
print("Monthly christmas savings: "+str(christmas_savings))
savings_sept_nov=3*christmas_savings
print("Total christmas savings: "+str(round(savings_sept_nov)))

print("Calculating Body Mass Index BMI")
# BMI=mass*height*height
weight=float(input("Enter your weight: "))
height=float(input("Enter your height: "))
bmi=weight*height*height
print("Weight: "+str(weight))
print("Height: "+str(height))
print("BMI: "+str(round(bmi)))

print("Program to print 6 letter word backwords")
test_word=input("Enter a six letter word: ")
print("The six letter word is: "+test_word)
# check the length of the word
word_len=len(test_word)
print("The length of the entered word is: "+str(word_len))

if(word_len!=6):
  print("wrong word length entered: needs six characters long word")
else:
  print("Correct word length...")
  print("Word backward: ")
  print(test_word[-1])
  print(test_word[-2])
  print(test_word[-3])
  print(test_word[-4])
  print(test_word[-5])
  print(test_word[-6])
  
  print("second realization")
  
  for i in range(1,word_len+1):
    print(test_word[-i])
    
  print("third realization")
  print(test_word[-word_len:])
  
      
  print("fourth realization")
  print(test_word[:-word_len])
  
  print("Example 1: ")

veryLongWord = "supercalifragilisticexpialidocious"
print(veryLongWord[0:5])      

print("Example 2: ")
index = 6
print(veryLongWord[index:9])    

print("Example 3: ")
print(veryLongWord[0:])
print(veryLongWord[:])
print(veryLongWord[:9])


# trying out replace function
gross_string="I!am!a!coding!genius!"
net_string=gross_string.replace("!"," ")
print(net_string)

# code to determne even or odd number entry
my_num=int(input("Enter an number to test even or odd: "))
if my_num%2==0:
  print("fizz")
else:
  print("buzz")
  
num=1 # this is an invariant
while num<11:
  print(num)
  num+=1
  
print("testing out lists in python")
groceries = ["apples", "milk", "cheese", "bread"]
groceries. append("coffee") 	# ["apples", "milk", "cheese", "bread", "coffee"]
groceries.insert(0, "carrots") # ["carrots","apples", "milk", "cheese", "bread", "coffee"]
groceries.insert(1, "peas") # ["carrots","peas","apples", "milk", "cheese", "bread", "coffee"]
groceries.pop() # ["carrots", "peas", "apples", "milk", "cheese", "bread"]
groceries.pop(0) # ["peas","apples", "milk", "cheese", "bread"]
groceries.remove("cheese") # ["peas","apples", "milk", "bread"]

# creating list of four animals
animaux=["squirrel","komodo","rabbit","donnkey"]
print("printing list...")
print(animaux)
print("printing list...")
for i in range(0,len(animaux)):
  print(animaux[i])
  
# removing second animal fromm list
animaux.pop(1)
print("printing list...")
for i in range(len(animaux)):
  print(animaux[i])
  
# apending cheetah to list
animaux.append("cheetah")
print("printing list...")
print(animaux)
print("printing list...")
for i in range(len(animaux)):
  print(animaux[i])
  
# removing cheetah from list
animaux.remove("cheetah")
print("printing list...")
for i in range(len(animaux)):
  print(animaux[i])
  
# program to get user names and email and print output
user_name=input("Enter your first name: ")
user_email=input("Enter your email address: ")
print("Hello ",user_name,"!, we will be contacting you shortly at ",user_email)
       
# program that tests whileloop and computes average
entry=0
sum=0
numbank=[]
while entry>-1:
  entry=int(input("Enter an interger: "))
  if entry==-1:
    break
  else:
    numbank.append(entry)

# print the list of numbers
print(numbank)

list_sz=len(numbank)
for i in range(list_sz):
  sum+=numbank[i]
  
#print sum and average
print("The sum and average are: ",sum,sum/list_sz)



# the guard and entry problem
guard_present=False
print("Between  the hour from 7 to 17, you do not need the guard to be there as the gate is open")
print("If the hour is before 7 or after 17, the guard must be there to let you in")
hr=int(input("enter an hour value between 0 and 23: "))

if hr>0 and hr<23:
  print("correct timescale chosen...")
  if hr>=7 and hr<=23:
    print("Hour=",hr)
    print("No need for the guard as normal open times")
    print("Gate is open!!!")
  elif (hr<7 or hr>17):
    guard_present=True
    print("Gate locked")
    if guard_present:
      print("You are in!!! Guard is present")
else:
  print("Wrong timescale entered")

# *****************
print()
print("Identity matrix") 
size=int(input("Enter a size for identity matrix: "))
for row in range(0, size):
  for col in range(0, size):
    
    # Here end is used to stay in same line
    if (row == col):
      print("1 ", end=" ")
    else:
      print("0 ", end=" ")
  print()   
  
print("Printing the mirror image of the previous matrix")
# the logic I have used here is to understand the positions within the
# matricx that has the values of one is always those positions where
# te sum of row+col= size-1
  
for row in range(0, size):
  for col in range(0, size):
    
    # Here end is used to stay in same line
    if ((row + col) == size-1):
      print("1 ", end=" ")
    else:
      print("0 ", end=" ")
  print() 
    

