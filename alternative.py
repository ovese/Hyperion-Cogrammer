"""
String manipulation exercises
1. The first part of the program has all the
   exercises being given in the tutprial text

2. the second pat=r of the program works on
   the main tasks for this session
"""


def bonus():
    my_string = "hello"
    print(f"1. getting the length of the string: {len(my_string)}")

    print(f"2. printing the string using the index")
    print(my_string[0])
    print(my_string[1])
    print(my_string[2])
    print(my_string[3])
    print(my_string[4])

    original_string = "Hello world!"
    print(f"3. Slicing the string: {original_string[0:5]}")
    print(f"4. after slicing the original "
          f"string is unchanged: {original_string}")
    print(f"5. lower the original string: {original_string.lower()}")
    print(f"6. upper the original string: {original_string.upper()}")
    print(f"7. capitalize the original string: {original_string.capitalize()}")
    print(f"8. title case for the original string: {original_string.title()}")
    print(f"9. stripping the original string: {original_string.strip(' ')}")
    print(f"10. Replacing in the original "
          f"string: {original_string.replace(' ','-')}")
    print(f"11. Do we still have the original string?: {original_string}")
    print(f"12. Finding text position within the original "
          f"string: {original_string.find('Hello')}")
    print(f"13. Splitting the original string is "
          f"unchanged: {original_string.split()}")
    print(f"14. Replacing in the original string: "
          f"{original_string.replace('world','le monde')}")
    # print(f"15. Appending to the original string: {original_string.append('Mephistopheles')}")
    print("16. " + "@".join(["apples", "bananas", "carrots"]))
    print("17. The escape sequence \\n creates a "
          "new line in a print statement")
    print("18. Hello \n \t \"bob\"")

    number_builder = " "
    i = 0
    while i <= 50:
        if i % 2 == 0:
            number_builder += str(i) + " "
        i += 1

    print(f"19. Print concatenation: {number_builder}")

    number_builder2 = []
    i = 0
    while i <= 50:
        if i % 2 != 0:
            # number_builder2.append(str(i) + " ")
            number_builder2.append(str(i))
        i += 1

    print(f"20. Print concatenation: {number_builder2}")
    """
    This function just shows the
    various examples given within the
    reading material and used as examples
    to master string manipulation
    """


def alternateFor(text="hello world, whats new this year"):
    print("Program that switches the case of argument")
    for i in range(len(text)):
        if i % 2 == 0:
            print(text[i].upper(), end=" ")
        else:
            print(text[i].lower(), end=" ")
    print("\n")
    """
    This function demonsytrates the
    switching of case for each letter
    in the text presented as argument
    to the function using a for loop
    """


def alternateWhile(text="hello world, whats new this year"):
    print("Second program that switches the case of argument")
    i = 0
    while i != len(text):
        if i % 2 != 0:
            print(text[i].upper(), end=" ")
        else:
            print(text[i].lower(), end=" ")
        i += 1
    print("\n")
    """
    This function demonsytrates the
    switching of case for each letter
    in the text presented as argument
    to the function using a while loop
    """


def alternateWordSplit(text="hello world, whats new this year"):
    print("Program that switches the case of argument")
    i = 0
    split_text_list = text.split()
    print(f"The split text is {split_text_list}, "
          f"and has length {len(split_text_list)}")
    while i != len(split_text_list):
        if i % 2 != 0:
            print(split_text_list[i].upper(), end=" ")
        else:
            print(split_text_list[i].lower(), end=" ")
        i += 1
    print("\n")
    """
    This function demonsytrates the
    switching of case for each word
    in the text presented as argument
    to the function using a while loop
    """


def alternateWordJoin(text=""):
    text_list = text.split()
    print(text_list)
    for item in text_list:
        print(item, end=" ")
    temp_list = []
    for i in range(len(text_list)):
        if i % 2 == 0:
            temp_list.append(text_list[i].upper())
        else:
            temp_list.append(text_list[i].lower())
    print("\nChanging word case for list: ", temp_list)
    print(f"Stitching the sentence back with join \n ")
    stitched_text = " ".join(temp_list)
    print(stitched_text)
    """
    This function demonsytrates the
    switching of case for each word
    in the text presented as argument
    to the function using a for loop
    """


def main():
    bonus()
    alternateFor("hello world, bienvenue tous le monde")
    alternateWhile("hello world, bienvenue tous le monde")
    alternateWordSplit("I am learning to code")
    alternateWordJoin("I am learning to code")
    """
    This main function starts
    the program by calling the functions
    in order
    """


if __name__ == '__main__':
    main()
