""" 
The program 
● Create a file called while.py.
● Write a program that continually asks the user to enter a number.
● When the user enters “-1”, the program should stop requesting the user
to enter a number,
● The program must then calculate the average of the numbers entered,
excluding the -1.
● Make use of the while loop repetition structure to implement the
program.
"""

user_prompt = 0 
total_sum = 0
count = 0
final_count = 0
mean = 0

# a first implementation
while user_prompt != -1:
    user_prompt = int(input("Enter an interger: "))
    total_sum += user_prompt
    count+=1
    if user_prompt == -1:
        final_count = count - 1
        total_sum = total_sum + 1
    
mean = total_sum/final_count
print(f"The mean of the {final_count} numbers entered with sum {total_sum} is: {mean}")


# a second implementation
my_prompt = 0 
my_total = 0
my_count = 0
new_final = 0
my_mean = 0
while my_prompt != -1:
    my_prompt = int(input("Enter an interger: "))
    if my_prompt == -1:
       break
    my_total += my_prompt
    my_count += 1
    
my_mean = my_total/my_count
print(f"The mean of the {my_count} numbers entered with sum {my_total} is: {my_mean}")

    