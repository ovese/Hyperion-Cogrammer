"""
If the user is 40 or over, output the message "You're over the hill."

Write code to take in a user's age and store it in an integer variable called
age.

Assume that the oldest someone can be is 100; if the user enters a
higher number, output the message "Sorry, you're dead.".

If the user is 65 or older, output the message "Enjoy your retirement!"

If the user is under 13, output the message "You qualify for the kiddie
discount."

If the user is 21, output the message "Congrats on your 21st!"

For any other age, output the message "Age is but a number."
"""


class AgeNotPositiveError(Exception):
    pass


try:
    age_input = input("Enter your age please: ")

    age = int(age_input)
    if age < 0:
        raise AgeNotPositiveError(f"Age {age} cant be negative")

except AgeNotPositiveError as age_error:
    print(f"Error raised: {age_error}")

else:
    if (age < 13):
        print("Your qualify for the kiddies discount")
    elif (age == 21):
        print("Enjoy your 21st!")
    elif (age >= 40 and age <= 65):
        print("You're over the hill.")
    elif (age > 65 and age < 100):  # age > 65 and age < 120
        print("Enjoy your retirement")
    elif (age > 100):
        print("Sorry you are dead")
    else:
        print("Age is but a number.")
finally:
    print("Exiting the age quiz program")
