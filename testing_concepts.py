import numpy as np
import time

def test_vectorization(n):
    start = time.time()
    sum = np.sum(np.arange(n))
    print(f"The sum of the range of numbers from 0 to {n} is {sum}")
    end = time.time()
    print(end - start)
    
def test_fstring():
    name = 'tom'
    age = 5
    height = 1.44

    s = f'{name=} {age=} {height=}'
    # name='tom' age=5 height=1.44
    print(s)

    pi = 3.14159265
    print(f"{pi}")
    s2 = f'pi is {pi:.2f}'
    print(f"{s2}")
    s3 = f'pi is {pi:.3f}'
    print(f"{s3}") 
    s4 = f'pi is {pi:.5f}'
    print(f"{s4}")
    
def test_tupleunpacking():
    print("Without tuple unpacking")
    person = ['tom', 5, 'male']

    name, age, gender = person
    # name='tom', age=5, gender='male'
    print(f"name:{name}, age:{age}, gender: {gender}")
    
    print("With tuple unpacking")
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    print(letters)

    first, second, *others = letters
    # first='A', second='B'
    # letters = ['C', 'D', 'E', 'F', 'G']
    print(f"first:{first}, second:{second}, others: {others} or I can do")
    print(f"{first}, {second}, {others}")
    
def read_file():
    contents_list = []
    contents_dict = {}
    with open("user.txt","r") as my_file:
        contents = my_file.readlines()
    print(len(contents))
    print(contents)
    for item in contents:
        contents_list.append(item.strip().split(';'))
    print(len(contents_list))
    print(contents_list)
    
    contents_dict = dict(contents_list)
    user_key = []
    password_value = ''
    for item in contents_dict.keys():
        user_key.append(item)
    print(user_key)
    print("Form dictionary from the contents list")
    # contents_dict = dict(contents_list)
    # print(len(contents_dict))
    # print(contents_dict)
    
def iterable_index():
    colors = ['red', 'green', 'blue']

# Loop over the elements in the list and print their index and value
for i, color in enumerate(colors):
    print(f'{i}: {color}') 

def main():
    # test_vectorization(1500000)
    # print()
    # test_fstring()
    # print()
    # test_tupleunpacking()
    print()
    read_file()
    

if __name__ == "__main__":
    main()