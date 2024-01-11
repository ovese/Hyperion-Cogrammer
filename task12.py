"""
Lessons in the task 12 file
This file will demonstrate some list and
dictionary examples which will be used
later in the main task
"""

# Creating a list
string_list = ["John", "Mary", "Harry"]
print(type(string_list))
print(string_list)

# indexing a list
pet_list = ["cat", "dog", "hamster", "goldfish", "parrot"]
print (pet_list[0])

# slicing a list
num_list = [1, 4, 2, 7, 5, 9]
print (num_list[1:2])

# changing an element in a list
name_list = ["James", "Molly", "Chris", "Peter", "Kim"]
print(f"Before: {name_list}")
name_list[2] = "Tom"
print(f"After: {name_list}")

# deleting an element from the list
char_list = ['P', 'y', 't', 'h', 'o', 'n']
print(f"Before deleting: {char_list}")
del char_list[3]
print(f"After deleting: {char_list}")


# here I am going try out some common 
# list functions. These are 
# ● extend() - Adds all elements of a list to another list
# ● insert() - Inserts an item at the defined index
# ● remove() - Removes an item from the list
# ● pop() - Removes and returns an element at the given index
# ● index() - Returns the index of the first matched item
# ● count() - Returns the count of the items passed as an argument
# ● sort() - Sorts items in a list in ascending order
# ● reverse() - Reverses the order of items in the list

language_list = ["Natural", "Formal"]
natural_languages = ["japanese","urhobo","english","swahili","bantu","arabic","hebrew"]
formal_languages = ["c++","c#","python","ruby","javascript","pearl","sql"]

print(natural_languages)
print(formal_languages)

all_languages = []
all_languages.append(natural_languages.extend(formal_languages))
print(all_languages)

natural_languages.insert(4,"french")
print(natural_languages)

natural_languages.remove("arabic")
print(natural_languages)

all_languages = formal_languages
print(all_languages)

print(all_languages.pop(3))
print(all_languages)





