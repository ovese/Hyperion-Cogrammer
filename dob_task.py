"""
Program to read and write to file
The file to be read is called dob.txt
"""

file_path = "./DOB.txt"


def check_file_exists():
    print("Reading text file using f = open()")
    contents = ""
    try:
        file2read = open(file_path, "r")  # read the textfile

        if not file2read:  # Check if the DataFrame is empty
            print('Text file is empty')
        else:
            # Proceed with data processing
            # print(file2read)
            print("File to read exists")
    # except pd.errors.EmptyDataError:
    #     print('CSV file is empty')
    except FileNotFoundError:
        print('Text file not found')
    else:
        contents = file2read.readlines()
        # print(contents)
    finally:
        file2read.close()
        print("Bye from the file reading program")

    return contents


def check_file_exists_v2():
    print("Reading text file using with open as ")
    contents_list = list()
    try:
        with open(file_path, "r") as fileread:  # read the textfile
            # using with, the file is automatically closed
            if not fileread:  # Check if the file read is empty
                print('Text file could NOT be opened')
            else:
                # Proceed with data processing
                print("File to read exists and is opened")
                for contents in fileread:
                    # print(contents)
                    contents_list.append(contents)
    except FileNotFoundError:
        print('Text file not found')
    else:
        # when I tried to read the contents of file here
        # using a for item in fileread and print statement,
        # it seems file was already closed an contents
        # could not be read as it gave a
        # ValueError: I/O operation on closed file
        # This is due to how the with statement works
        # You dont have to close file when using the with
        pass
    finally:
        # fileread.close()
        print("Bye from the file reading program using with-open")

    return contents_list


def process_file_contents(content_list):
    print(f"The length of the returned list is: {len(content_list)}")
    new_list = []
    for i in range(len(content_list)):
        new_list.append(content_list[i].rstrip('\n'))
    print(new_list)

    # take each string within the list and split at space
    names = []
    dob = []
    for i in range(len(content_list)):
        split_str = new_list[i].split(" ")
        name_section = split_str[0:2]
        names.append(name_section)
        dob_section = split_str[2:]
        dob.append(dob_section)

    return (names, dob)


def display_formatted_output(name_list, dob_list):
    print("Name")

    # for i in range(len(name_list)):
    #    print(f"{name_list[i][0]} {name_list[i][1]}")
    #  line above is hardcoded and not very intelligent
    for name in name_list:
        print(" ".join(name))

    print("\n")

    print("Birthdate")
    # for j in range(len(dob_list)):
    #     print(f"{dob_list[j][0]} {dob_list[j][1]} {dob_list[j][2]}")
    for dobby in dob_list:
        print(" ".join(dobby))


def main():
    # print("Processing results from the first file reading method")
    # ret_contents = check_file_exists()
    # process_file_contents(ret_contents)

    print("Processing results from the second file reading method")
    ret_contents2 = check_file_exists_v2()
    [Names, Dobs] = process_file_contents(ret_contents2)

    display_formatted_output(Names, Dobs)


if __name__ == "__main__":
    main()
