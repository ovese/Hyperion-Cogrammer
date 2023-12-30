""" 
flow control practice 
booleans
if
else
elif
"""

num = 10
if num < 12:
    print(f"Number {num}, is less than 12 ")
    

num = int(input("Enter a number between 1 and 30 "))
if num < 12:
    print(f"Number {num}, is less than 12 ")
    
umbrella = "leave me at home"
rain = False
if rain:
    print("bring me along")
    
# using if-else statements
if rain:
    print("bring me along") # this line only runs if condition is True
else:
    print(umbrella)
    

num = int(input("Enter a number between 1 and 30 "))
if num < 12:
    print(f"Number {num}, is less than 12 ")
else:
    print(f"Number {num} is larger than 12")
    
# using elif statements
num = int(input("Please input a number between 1 and 100 "))
if num < 12:
    print("The value you entered is lower than 12")
elif num > 13:
    print("The value you entered is higher than 13")
elif num < 13:
    print("The value you entered is lower than 13")
else:
    print("The value you entered is 13")
    

# othr conditionals
current_time = 12
if current_time < 11:
    print("Time for a short jog - let's go!")
else:
    print("It's after 11 - it's lunch time.")
    
current_time = 11
if current_time < 11:
    print("Time for a short jog - let's go!")
elif current_time ==11:
    print("Tome to pack up and prep for lunch")
else:
    print("It's after 11 - it's lunch time.")
    
# my sinple example
speed = float(input("Enter a speed value from 300 to 1000: "))
if speed < 343:
    print("Sub-sonic speed!")
elif speed ==343:
    print("Sonic speeds achieved")
elif speed > 343:
    print("Speed is supersonic.")
elif speed > 450:
    print("speed is Hypersonic...Kinzhai")
else:
    print("Defies speed in air")
