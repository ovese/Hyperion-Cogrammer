"""This task is as described
This task takes a file with pairs of texts
this text can be arranged in key value pairs
the order of the text is not relevant at first
but the text needs to be put into a dictionary.
the dictionary will then have to be ordered such that the values are
unique numbers that can be sorted into ascending or descending
we must then arrange the values into a pyramid or triangle
or floyd pyramid

the last digits in each row of the traingle must be read and 
used to form a sentence using the key value pairs
"""

from collections import OrderedDict

# file_to_read = "textfile.txt"  # 
file_to_read = "coding_qual_input.txt"  #


with open(file_to_read, "r") as myfile:
    file_content = myfile.readlines()
    
print(type(file_content))
len_list = len(file_content)
print(len_list)
print(file_content)

striped_list = []
for i in range(len_list):
    striped_list.append(file_content[i].rstrip('\n'))
    
print(striped_list)

# split the current list about space
split_list = []
for i in range(len_list):
    split_list.append(striped_list[i].split(' '))
print(split_list)

num_part = []
word_part =[]

for i in range(len_list):
    num_part.append(int(split_list[i][0]))
    word_part.append(split_list[i][1])
print(num_part)
print(word_part)

keys = num_part
values = word_part
    

text_dict = dict()
for i in range(len_list):
    text_dict[keys[i]]=values[i]
print(text_dict)

print("New swapped dictionary........")
new_dict = dict([(value, key) for key, value in text_dict.items()])
print(new_dict)

print("Sorted and ordered dictionary.........")
# sorted_text_dict = sorted(text_dict.items(), key=lambda x:x[1])
sorted_text_dict = OrderedDict(sorted(new_dict.items(), key=lambda item: item[1]))
print(sorted_text_dict)

print("Retrieving dcitionary from tupled dictionary...........")
resorted_text_dict =dict(sorted_text_dict)
print(resorted_text_dict)

sorted_keys = sorted(keys)
print(f"Sorted numbers:........\n {sorted_keys}")

print("Printing pyramid.........")
count = 0
pyramid_list_end = []
for i in range(1,24+1): # Hardcoding here is not smart coding in my opinion
    for j in range(1,i+1):
        print(sorted_keys[count], end= " ")
        count += 1
        #pyramid_list_end.append(sorted_keys[count])
    print()

skip_index = 0
skip_increase = 2
valid_index = []

for i in range(23):
    # skip_index = i
    skip_index = skip_index + skip_increase
    # print(f"{skip_index} : {skip_increase}")
    valid_index.append(skip_index)
    skip_increase += 1
print(valid_index)


for i in valid_index:
    print(f"{i} : {list(resorted_text_dict)[i]}")

