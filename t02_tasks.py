# python recognises this as a string because of quotation marks
word = "heLlO Party pEople"
print("Printing out the string: "+word)
number_string = "10"  # cant be used in arithmetic without casting
print("printing out the number string: "+number_string)

print("Intergers can be positive or negative")
number = 5  # any whole number thats is positive or negative
print("positive interger ", number)
neg_number = -16
print("negative number ", neg_number)

print("Printing out decimal which can be +ve or -ve")
decimal = 3.4  # this is a float due to decimal
print("positive decimal ", decimal)
neg_decimal = -9.8
print("negative decimal ", neg_decimal)

print("Boolean values are discrete or take only two types of values")
fact = True  # this is boolean type
neg_fact = False
print("Data or expression can be {} or {}".format(fact, neg_fact))

"""
manipulating strings
"""

lower_word = word.lower()  # changing original word to lower case
print("changing {} to lower case: {}".format(word, lower_word))

upper_word = word.upper()  # changing original word to uppercase
print("changing {} to upper case: {}".format(word, upper_word))

cap_word = word.capitalize()  # capitalizes the original word
print("changing {} to capitals: {}".format(word, cap_word))

word_split = word.split(",")
print("splitting {} : {}".format(word, word_split))


word2 = "==hello== ==world===="
word2_strip = word2.strip("=")
print("stripping {} : {}".format(word2, word2_strip))
print("Any symbols between he two words wont be affected")

rep_word = word2.replace("=", " ")
print("replacing {} : {}".format(word2, rep_word))

"""
String indexing
"""
print("position of a charcater inside a string")
print(" python indexing starts from zero")

print("Get out charcater ib position 1 or index zero")
position = word[0]
print(position)

print("Get out charcater in position 4 or index three")
position = word[3]
print(position)

print("Get out charcaters within range")
position = word[0:2]
print(position)

print("Get out charcater in alternate position")
word[0::2]
print(position)

print("Negative indexing")
position = word[-1]
print(position)
position = word[-5]
print(position)

print("reversing string")
position = word[::-1]
print(position)

"""
The rest of the code is my extension to the taught material
"""


# ************ Example 1 ************
print("Hello, World!")


# ************ Example 2 ************
print("Printing a string.")
my_address = "30 Front Street"
print("My address is:{} ".format(my_address))
print("Practicing string indexing")
str_size = len(my_address)
print("Getting string size {} ".format(str_size))
print(my_address[0:2])
print(my_address[-1:0])
print(my_address.strip(" "))


# ************ Example 3 ************
# The following input commands will get the user's name and age.
name = input("Enter your name: ")
age = input("Enter your age: ")

print(name, age)
print("{} is {} years old!".format(name, age))
