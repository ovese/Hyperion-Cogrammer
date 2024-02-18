import configparser
import os

config = configparser.ConfigParser()
config.read('roles_config.ini')

"""
Code to register students for an exam venue
1. ask user how many students are registering
2. create for loop that runs that number of students
3. each time for loop runs, program should ask
   user for next student id number
4. write each id number to a text file called
   reg_form.txt
5. include a dotted line after each student id
   because this file will be used as an attendance
   register which students will sign when they arrive
   exam venue
6. This program uses the folowing files
7. create_config.py which is used to populate
   the config file that will be read from
8. student_register.py which contains the program logic
9. main_register.py that launches the program
"""


class NegativeValueError(Exception):
    pass


class StudentRegister:
    def __init__(self, role):
        self.role = role  # the roles can be admin or visitor

    def read_configfile_sections(self):
        print(config.sections())
        # Output: ['Section 1', 'Section 2']

    def get_num_students(self):
        try:
            # should i try a while here to force right input
            # or to ensure if wrong input is used a number of times
            # the program exits
            student_number = int(input("Enter number of students: "))
            if student_number < 0:
                raise NegativeValueError(f"Cant have negative "
                                         f"value as this value")
            elif student_number == 0:
                print(f"You cant register {student_number} "
                      f"number of students")
            else:
                print(f"You entered {student_number} as number"
                      f"of students to register")
        except NegativeValueError as nve:
            print(nve)
        except ValueError as ve:
            print(ve)
        except UnboundLocalError as ule:
            print(ule)
        else:
            print("Valid entry made for number of students")
        finally:
            print(f"You have {student_number} students "
                  f"scheduled for registration")

        return student_number

    def read_user_names_roles(self):
        users = []
        roles = []
        for key in config['AppUsers']:
            # users.append(config['AppUsers'][item]) # ***interesting how I got this to work***
            users.append(key)
            # roles.append(value)
        for item in users:
            roles.append(config['AppUsers'][item])

        return users, roles

    def validate_user(self):
        current_user = input("Enter your UserID: ")
        validated_role = " "
        found = False

        [my_users, my_roles] = self.read_user_names_roles()
        # confirm current user is on list of registered users
        for i in range(len(my_users)):
            # test for upper case or capitalize also
            if current_user == my_users[i]:
                found = True
                validated_role = my_roles[i]
                break
            else:
                found = False

        if found:
            print(f"User {current_user} FOUND, with "
                  f"role {validated_role}")
        elif not found:
            print(f"User {current_user} NOT FOUND")
            exit()

        return current_user, validated_role

    def execute_registration(self, n):
        [my_username, my_role] = self.validate_user()
        print(f"Welcome {my_username}, you are logged "
              f"in with {my_role} priviledges")
        student_id = " "
        file_path = " "
        try:
            with open("reg_form.txt", "w") as rf:
                if not rf:
                    raise FileExistsError(f"File {rf.name()} "
                                          f"could not be opened")
                else:
                    print("File is opened and can be written to")
                    rf.write("#\t\t studentID\t\t User\t\t Role\t\t Signature\n")
                    rf.write("==================================="
                             "=========================\n")
                    for i in range(n):
                        student_id = input(f"Student {i+1}: ")
                        rf.write(str(i+1)+"\t\t"+student_id+"\t\t\t"+my_username+"\t\t"+my_role+"\n")
                        rf.write("-------------------------------"
                                 "--------------------------------\n")
        except FileExistsError as fe:
            print(fe)
        except TypeError as te:  # if I wrongly reference a non-callable entity or method
            print(te)
        except IOError as ioe:  # if i try to access a file that is already closed
            print(ioe)
        else:
            file_path = "./reg_form.txt"
            print(f"File {os.path.basename(file_path)}, written"
                  f" to Successfully")
        finally:
            print(f"You have successfully registered {n} students")

    def display_utility(self, list2print):
        list_size = len(list2print)
        for i in range(list_size):
            print(list2print[i], end=" ")
