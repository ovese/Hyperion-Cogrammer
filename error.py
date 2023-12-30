# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program")
print(">>>Fixed syntax error for line 5 by adding missing parentheses")

print ("\n")
print(">>>Fixed indentationError and Syntax error for missing parentheses on line 8")

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24 years old" 
print(">>>Fixed indentation error first on line 12,"
      "Secondly fixed variable declaration error as equality "
      "was used instead of an assignment for variable age_str")
age = age_Str # age = int(age_Str) 
print(">>>Fixed indentationError for line 16")
print(">>>Fixed ValueError for line 16 as var is a string")
    
print("I'm " + age + "years old.")
print(">>>Fixed another indentationError on line 20")

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
print(">>>Fixed another indentationError on line 24")
total_years = age + years_from_now
print(">>>Fixed another indentationError on line 26")

print ("The total number of years:" + "answer_years")
print(">>>Fixed syntax error for line 29 by adding missing parentheses")

# Variable to calculate the total amount of months from the total amount of years and printing the result
total = int(years_from_now)
total_months = total * 12
print(">>>fixed line 34 has a NameError as total is not defined anywhere inside code")
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old")
print(">>>Fixed syntax error for line 36 by adding missing parentheses, "
      " then converting total_months into string to avoid TypeError "
      " and to allow concatenation")

#HINT, 330 months is the correct answer