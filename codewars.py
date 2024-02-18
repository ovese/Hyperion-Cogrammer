def to_camel_case(text):
    """Complete the method/function so that it converts
dash/underscore delimited words into camel casing. The
first word within the output should be capitalized only
if the original word was capitalized (known as Upper Camel
Case, also often referred to as Pascal case). The next
words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""

    new_text = ""
    len_text = len(text)
    print(f"length of text is {len_text}")
    for i in range(len_text):
        if text[i] == '-':
            new_text = text.replace(text[i],' ')
    for i in range(len(new_text)):
        if new_text[i]=='_':
            new_text = new_text.replace(new_text[i],' ')

    text_list = list(new_text.split(" "))
    mod_list = []
    for i in range(len(text_list)):
        mod_list.append(text_list[i].capitalize())

    s=''

    return s.join(mod_list)

def alphabet_position(text):
    """Map all letters in text to correspondiing
        numeric value. Using a dictionary to
        match letters to numbers
    """
    alpha_list = ['a','b','c','d','e','f','g','h','i','j',
                  'k','l','m','n','o','p','q','r','s','t',
                  'u','v','w','x','y','z']
    print(type(alpha_list))
    print(len(alpha_list))
    print(alpha_list)

    # assign each letter to a number in ascending order
    num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
                17,18,19,20,21,22,23,24,25,26]
    print(num_list)
    
    # res_dct = map(lambda i: (alpha_list[i], num_list[i+1]), range(len(alpha_list)-1)[::2])
    res_dct = map(lambda i: (alpha_list[i], num_list[i]), range(len(alpha_list))[::1])
    alpha_num_dict = dict(res_dct)
    print(alpha_num_dict)

    print()
    
    # zip the two lists together to create a list of key-value pairs
    key_value_pairs = zip(alpha_list, num_list)

    # convert the list of key-value pairs to a dictionary
    my_dict = dict(key_value_pairs)
    print(my_dict)

    retrieved_num_list = []
    for i in range(len(text)):
        if text[i] != ' ':
            value = my_dict[text[i]]
            retrieved_num_list.append(value)

    #print(retrieved_num_list)
    #equiv_num_str = ",".join(retrieved_num_list)
    my_str = " ".join(str(element) for element in retrieved_num_list)
    # equiv_num_str = my_str

    # or using list comprehension
    string_list = [str(element) for element in retrieved_num_list]# my_list
    equiv_num_str = string_list
    
    return equiv_num_str

def bubblesort_desc(l):
    """Perform a single pass of the input list
       using bubblesort algorithm"""
    print("Before first pass: ")
    print(l)
    # temp
    for i,itemi in enumerate(l):
        j=i+1
        for j,itemj in enumerate(l):
            if l[i] < l[j]:
                pass
            elif l[i] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    print("After bubble sort")
    print(l)

def bubblesort_asc(l):
    """Perform a single pass of the input list
       using bubblesort algorithm"""
    print("Before first pass: ")
    print(l)
    # temp
    for i,itemi in enumerate(l):
        j=i+1
        for j,itemj in enumerate(l):
            if l[i] > l[j]:
                pass
            elif l[i] < l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    print("After bubble sort")
    print(l)

def bubblesort_once(l):
    """Perform a single pass of the input list
       using bubblesort algorithm"""
    print("Before first pass: ")
    len_l = len(l)
    print(len_l)
    print(l)
    # temp
    for i,itemi in enumerate(l):
        j=i+1
        if j < len_l:            
            if l[i] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    print("After bubble sort")
    print(l)

def solution(text, ending):
    """Program for string ends with works
       by having the logic check if the second
       string forms the ending of the first:
       use the following logic:
       1. get length of text to match
       2. extract similar length from end of text
       3. match to decide true or false"""
    print(f"Text: {text}")
    print(f"ending: {ending}")
    matches = False
    len_end = len(ending)
    print(len_end)
    extract_end = ""
    extract_end = text[-len_end:]
    print(f"Extracted text end: {extract_end}")
    if extract_end == ending:
        matches = True
    else:
        matches = False

    return matches

def find_it(seq):
    """loops through a sequence and identify
       the only number that occurs odd number
       of times"""
    return None
                                   
def main():
    ret_text = to_camel_case("come-up-hither_oh_ye-saints")
    print(f"Formatted text is: \n{ret_text}")

    print()

    ret_num_str = alphabet_position("hello to gen z world")
    print(f"Formatted text is: \n{ret_num_str}")

    print()
    l = [9,7,5,3,1,2,4,6,8]
    bubblesort_desc(l)

    print()
    l2 = [9,7,5,3,1,2,4,6,8]
    bubblesort_asc(l2)

    print()
    l3 = [9,7,5,3,1,2,4,6,8]
    bubblesort_once(l3)

    print()
##    "hello world"
##    "orld"
##    "samurai", "ai" 
##    "ninja",   "ja"
##    "sensei",  "i"
##    "abc",     "abc"
##    "abcabc",  "bc"
    # "fails",   "ails
    text = "samurai"
    ending = 'ai'
    # solution(text, ending)
    ret_bool = solution(text, ending)
    print(ret_bool)


if __name__ == "__main__":
    main()
