"""The task manager program is a reconfiguration
task that requires my understanding existing code
and adding structure and logic to improve it.
I will be using all OOP priciples at my disposal 
for this task. This will include:
Classes and functions or methods.

Second, I am going to be implementing parts of code
using the advanced concepts taught during the bootcamp.
These concepts include:
Lambda functions
Decorators
Higher order fucntions HOFs

third, where possible , I will apply configuration files.
These files can be json or ini typoe files

fourth, I am going to be applying error checking
using try-except-else-finally logic

"""
# import module libraries
import os
from datetime import datetime, date
# Python version
import sys
# scipy
import scipy
# numpy
import numpy
# matplotlib
import matplotlib
# pandas
import pandas as pd
# json
import json
# tabulate
from tabulate import tabulate
# time
import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

global DATETIME_STRING_FORMAT
DATETIME_STRING_FORMAT = "%Y-%m-%d" # this should be global

# menu_options = []

class DuplicateNameError(Exception):
    pass

class WrongMenuSelectionError(Exception):
    pass

class AuthorisationDeniedError(Exception):
    pass

class TaskManager():            
    def __init__(self, curr_user, username_password, username_list, password_list):
        """The __init__ function takes the curr-user and
           the dictionary of username passwords"""
        # If no user.txt file, write one with a default account
        if not os.path.exists("user.txt"):
            with open("user.txt", "w") as default_file:
                default_file.write("admin;password")
                
        self.curr_user = curr_user
        self.username_password = username_password
        
        username_password_list = []
        # self.username_password = {}
        with open("user.txt","r") as my_file:
            contents = my_file.readlines()
        for item in contents:
            username_password_list.append(item.strip().split(';'))
            
        self.username_password = dict(username_password_list)
        
        # declare the global or class variables for user_keys and user_values
        self.username_list = username_list
        self.password_list = password_list
        # # lets get the current user from the dictionary passed as argument
        # saved_users = {k : k for (k,v) in username_password.items()} # dictionary comprehension
        # user_key = []
        # password_value = []
        # user_key = list(saved_users.keys()) # list of keys
            
    
    def validate_module_version(self):
        print("Module versions used in program")
        print(f'Python: {sys.version}')
        print(f'scipy: {scipy.__version__}')
        print(f'numpy: {numpy.__version__}')
        print(f'matplotlib: {matplotlib.__version__}')
        print(f'pandas: {pd.__version__}')
        # print(f'time: {datetime.__version__}')
    
    def my_timer_decorator(func): # func is param that receives the function
        def wrapper(*args, **kwargs):# wrapper can be any name really
            # storing time before function execution
            begin = time.time()
            print(f"Started here...{begin}")
            func(*args, **kwargs)
            # storing time after function execution
            end = time.time()
            print(f"Ended here...{end}")
            print("Total time taken in : ", func.__name__, end - begin)
        return wrapper
    
    # or use normal function that i want to decorate
    @my_timer_decorator
    def compute_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        # time.sleep(1)
        print(f"The current time: {current_time}")
        
    def create_task_detail(self):
        # DATETIME_STRING_FORMAT = "%Y-%m-%d"

        # Create tasks.txt if it doesn't exist
        # seed file with default task as format
        if not os.path.exists("tasks.txt"):
            with open("tasks.txt", "w") as default_file:
                # pass
                # default task.txt entry has the format
                # username;task title;task_description;date due;date generated;completion status
                default_file.write("admin;Task title;Task description.;2022-12-01;2022-11-22;No")

        with open("tasks.txt", 'r') as task_file:
            task_data = task_file.read().split("\n")
            task_data = [t for t in task_data if t != ""] # list comprehension used here
            
        print("------Debug output from list comprehension-----")
        print(type(task_data))
        print(task_data)

        task_list = [] # I have used this so much, I should make it global/ class variable
        for t_str in task_data:
            curr_t = {}

            # Split by semicolon and manually add each component
            ### I am adding the task ID data field here to allow the task.txt have a serial number entry
            task_components = t_str.split(";")
            #curr_t['task_id'] = task_components[0]
            curr_t['username'] = task_components[0]
            curr_t['title'] = task_components[1]
            curr_t['description'] = task_components[2]
            curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
            curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
            curr_t['completed'] = True if task_components[5] == "Yes" else False

            task_list.append(curr_t)
            
        return (curr_t, task_list) # returning both dict and list
    
    def display_task_detail(self, task_dict):
        
        print(task_dict)
        my_keys = task_dict.keys()
        my_values = task_dict.values()        
        
        my_keys_list = list(my_keys)
        my_values_list = list(my_values)
        
        return (my_keys_list, my_values_list)
    
    def is_logged_in(self, keys_list, values_list):
        #====Login Section====
        '''This code reads usernames and password from the user.txt file to 
            allow a user to login.
        '''
        # If no user.txt file, write one with a default account
        if not os.path.exists("user.txt"):
            with open("user.txt", "w") as default_file:
                default_file.write("admin;password")

        # Read in user_data
        with open("user.txt", 'r') as user_file:
            user_data = user_file.read().split("\n")
        print(f".....Debug.....what does user_data look like: {user_data}")

        # Convert to a dictionary
        for user in user_data:
            username, password = user.split(';')
            self.username_password[username] = password

        logged_in = False
        while not logged_in: 

            print("LOGIN")
            self.curr_user = input("Username: ")
            curr_pass = input("Password: ")
            if self.curr_user not in self.username_password.keys():
                print("User does not exist")
                continue
            elif self.username_password[self.curr_user] != curr_pass:
                print("Wrong password")
                continue
            else:
                for i in range(len(keys_list)):
                    if ((self.curr_user == keys_list[i]) and (curr_pass == values_list[i])): # use more compact statement in if
                        print(f"Logged in as user: {self.curr_user} \n"
                              f"with password {curr_pass}")
                print("Login Successful!")
                logged_in = True
                
        return (logged_in, self.username_password)
    
    def retrieve_saved_users(self):
        """Retrieve the saved users and separate the 
           User names into a list and the passwords into another list
           return the two lists so that they can be used elsewhere
           """
        username_password_list = []
        # username_password = {}
        
        with open("user.txt","r") as my_file:
            contents = my_file.readlines()
        for item in contents:
            username_password_list.append(item.strip().split(';'))
            
        # username_password = dict(username_password_list) #################
        # lets get the current user from the dictionary passed as argument
        saved_users = {k : v for (k,v) in self.username_password.items()} # dictionary comprehension
        user_key = []
        password_value = []
        user_key = list(saved_users.keys()) # list of keys
        password_value = list(saved_users.values()) # list of values
            
        return (user_key, password_value) # i might choose to also return saved passwords list
    
    def validate_user_entry(self,username, search_list):
        """this function will take the user entry and target username list
           as arguments. 
           Then ascertain if the user name is found in the target list.
           It return a true or false value
           True is username already exists
           False if user name is not in list 
           """
        counter = 0
        # checks if entered user name is found or not
        # ideal is to not have it already
        # true means the name already exists and is found in list
        found_user = True 
        try:
            # request user name from user here
            # - Request input of a new username
            # see if after 3 tries the user is logged out
            # move the while statement here to check for the new user name being entered       
            while found_user == True: # could i have just said while found_user
                re_username = input("Re-enter user name: ")
                if re_username in search_list:
                    counter += 1
                    print(f"You have made {counter} tries for user name")
                    # continue
                    if counter == 3:
                        break
                    continue
                elif re_username not in search_list:
                    username = re_username
                    print(f"Your selected user name is {username}")
                else:
                    raise DuplicateNameError(f"You cant use an already existing user name.\nSelect unique user name: \n")
                found_user = False
        except DuplicateNameError as dne:
            print(dne)
        else:
            pass
        finally:
            pass

        return username,found_user # this should be False, to make it work or to register new user
    
    # reg_user — a function that is called when the user selects ‘r’ to
    # register a user.
    def reg_user(self):
        '''Add a new user to the user.txt file
           by requesting for the username and password
           It also checks if the usename exists and either
           allows the name to be added or stops it from
           being added'''
        # declare a dictionary
        # i could pass this as a param or argument or global var
        # username_password = {}
        
        # - Request input of a new username
        new_username = input("New Username: ") # read this from function to validate username 
        # - Retrieve username list
        [ret_usernames, ret_passwords] = self.retrieve_saved_users()
        # check for duplicate user name here 
        [ret_new_username, entry_exists] = self.validate_user_entry(new_username, ret_usernames)
        if entry_exists == False:
            print(f"Registered username: {ret_new_username}")
            print("Next, select a suitable password.....")
            # - Request input of a new password
            new_password = input("New Password: ")

            # - Request input of password confirmation.
            confirm_password = input("Confirm Password: ")

            # - Check if the new password and confirmed password are the same.
            if new_password == confirm_password:
                # - If they are the same, add them to the user.txt file,
                print("New user added")
                self.username_password[ret_new_username] = new_password

                with open("user.txt", "w") as out_file:
                    user_data = []
                    for k in self.username_password:                        
                        user_data.append(f"{k};{self.username_password[k]}")
                    out_file.write("\n".join(user_data))

                    # - Otherwise you present a relevant message.
            else:
                print("Passwords do no match")
        else:
            print(f"user name entered {new_username} is not valid")
                    
    
    # add_task — a function that is called when a user selects ‘a’ to add a
    # new task.
    def add_task(self, auth_dict, task_list):
        '''Allow a user to add a new task to task.txt file
           Prompt a user for the following: 
           - A username of the person whom the task is assigned to,
           - A title of a task,
           - A description of the task and 
           - the due date of the task.'''
        # username_password = {} # or assign dict()
        username_password = auth_dict
        
        # lets get the current user from the dictionary passed as argument
        curr_user = {k : k for (k,v) in username_password.items()} # dictionary comprehension
        # print(curr_user)
        # print(curr_user.keys())
        # users_list = list(curr_user.keys())
        # print(users_list)
        
        # task_id = input("A unique task ID number e.g. 001")
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys(): # or not in users_list from line 318
            print("User does not exist. Please enter a valid username")
            # continue
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break
            except ValueError:
                print("Invalid datetime format. Please use the format specified")


        # Then get the current date.
        curr_date = date.today()
        ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.
            Also add task ID to update for each task added'''
        #for i in range(1,100): # this for leaves end range open as any number of tasks can be added          
        new_task = {
            # "Task ID": task_id,
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    # t['task_id'],
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")    
    
    # view_all — a function that is called when users type ‘va’ to view all
    # the tasks listed in ‘tasks.txt’.
    def view_all(self, auth_dict, task_list):
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''

        for i,t in enumerate(task_list, 1):
            # i += 1
            disp_str = f"Task S/N: \t {i}\n"
            # disp_str += f"Task code: \t {t['task_id']}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task complete?: \t {"Yes" if t['completed'] else "No"}\n"
            disp_str += f"Task Description: \t {t['description']}\n"
            print(disp_str)                
    
    # view_mine_unique — a function that is called when users type ‘vm’ to view
    # specific task item in the list
    def pick_unique_task(self, curr_user, task_list):
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling).
           But more importantly, be able to isolate specific tasks by number
        '''
        task_id = int(input(f"Welcome {curr_user}, do you want to: \n"
                             "1. To view specific task:.....enter task ID \n"
                             "2. To return to main menu :.....enter -1 \n")) # previously an int when i used Serial number

        # i should be able to use the counter to select specific task from list
        counter = 1
        for counter,t in enumerate(task_list): # i previously used an enumerator here
            if t['username'] == curr_user: # getting only tasks for particular user
                counter += 1
                if task_id == counter:
                    disp_str = f"Task S/N: \t {counter}\n"
                    # disp_str += f"Task ID: \t {t['task_id']}\n"
                    disp_str += f"Task: \t\t {t['title']}\n"
                    disp_str += f"Assigned to: \t {t['username']}\n"
                    disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                    disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                    disp_str += f"Task Description: \t {t['description']}\n"
                    print(disp_str)
                elif task_id == -1:
                    break
        
    # extends the view mine function allowing user to pick unique
    # task and edit same
    # edit specific task item in the list
    def pick_and_edit_task(self, curr_user, task_list):
        '''Allows selection of unique task and 
           editing of same 
        '''
        try:
            task_id = int(input(f"Welcome {curr_user}, do you want to: \n"
                        "1. To view a specific task and edit :.....enter task ID \n"
                        "2. To return to main menu :.....enter -1 \n"))
            # initialise display string
            disp_str = " "
            # task status variable
            task_status = ""
            # file to eventually write to
            file_path = os.path.basename('./modified_tasks.txt')
            # i should be able to use the counter to select specific task from list
            counter = 1
            for counter,t in enumerate(task_list):
                if t['username'] == curr_user: # getting only tasks for particular user
                    counter += 1
                    if task_id == counter and t['completed'] == False:
                        disp_str = f"Task S/N: \t {counter}\n"
                        #  disp_str += f"Task ID: \t {t['task_id']}\n"
                        disp_str += f"Task: \t\t {t['title']}\n"
                        # try to edit task assignee
                        _prompt = input(f"Current task owner is {t["username"]} \n"
                                        f"Would you want to re-assign task \n"
                                        f"Yes/No? \n").lower()                    
                        if _prompt == "yes":
                            _new_username = input("Enter new username for task owner")
                            t["username"] = _new_username
                            disp_str += f"Assigned to: \t {t['username']}\n"
                        elif _prompt == "no":
                            t["username"] = curr_user
                            disp_str += f"Assigned to: \t {t['username']}\n"
                        # disp_str += f"Assigned to: \t {t['username']}\n"
                        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                        disp_str += f"Task Description: \t {t['description']}\n"                    
                        task_status = input("Is task completed, (Yes/No)?: ").lower() # check task status ####### todo 
                        if task_status == "yes":
                            t['completed'] = True
                            disp_str += f"Task status: \t {"Yes" if t['completed'] else "No"}"
                        elif task_status == "no":
                            t['completed'] = False
                            disp_str += f"Task status: \t {"Yes" if t['completed'] else "No"}"
                        else:
                            print("Not a known request option")
                        print(disp_str) # instead of printing i will write to json file
                    elif task_id == -1:
                        break
        except ValueError as ve:
            print(ve)
        
        # the code below must be inside the scope of the for loop to work
        split_disp_str = disp_str.replace('\t','').split('\n')
        # ('').join(split_disp_str)
        updated_task_item_list = split_disp_str
        # updated_task_item_list.append(split_disp_str)
        # print(type(updated_task_item_list))
        # print(updated_task_item_list)
                
        # create a dictionary from this list and then write it to the tasks.txt file
        # Convert to a dictionary
        task_dict = {}
        str_to_write_list = []
        for item in updated_task_item_list:
            val1, val2 = item.split(':')
            task_dict[val1] = val2
        # print(task_dict)
        for key,value in task_dict.items():
            str_to_write_list.append(value)
        # print(str_to_write_list)
        # with open(file_path,'a') as modify_file:
        #     # converting all items of a list to a string using the generator expression.
        #     modify_file.write(";".join(str(item) for item in str_to_write_list)) # if this works, I will be shocked
        #     # modify_file.write(str_to_write_list) # i couldn't write list to file directly. Its not alowed
        
        # check the contents of task_status and status of t['completed'] here
        print(f"Task status:......... {task_status}")
        if task_status == 'yes':
            t['completed'] = True # therefore we can write to modified.txt file
            file = open(file_path, "a")
            file.write(";".join(str(item) for item in str_to_write_list)+'\n')
            print(f"File, {file_path}, was successfully written to")
            file.close()
        elif task_status == 'no':
            t['completed'] = False
            # dont write or do nothing
            print(f"Task completed status is {t['completed']} \n"
                  f"File, {file_path}, was NOT written to")

    # view_mine — a function that is called when users type ‘vm’ to view
    # all the tasks that have been assigned to them
    def view_mine(self, curr_user, task_list):
        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
        # counter = 1 # i should be able to use the counter to select specific task from list
        for counter,t in enumerate(task_list,1):
            if t['username'] == curr_user: # whats going on here
                # counter+=i
                disp_str = f"Task S/N: \t {counter}\n"
                # disp_str = f"Task ID: \t {t['task_id']}\n"
                disp_str += f"Task: \t\t {t['title']}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \t {t['description']}\n"
                print(disp_str) # instead of printing i will write to json file
                
        # self.pick_unique_task(curr_user, task_list)
        # self.pick_and_edit_task(curr_user, task_list)
                
                
        # here we select between just picking a unique task or
        # picking and editing a specific task
        select_action = int(input("From the displayed tasks, do you want to\n"
                                  "1. View a specific task\n"
                                  "2. View and edit specific task\n"
                                  "x. Go back to main menu\n"))
        if select_action == 1:
            # Try to select a unique task by id here
            self.pick_unique_task(curr_user, task_list)
        elif select_action == 2:
            # Try to edit a task here
            self.pick_and_edit_task(curr_user, task_list)
            
    def generate_report(self):
        """This function reads the tasks.txt file and modified_tasks.txt
           to draw statistics from files"""
        task_report_str = ""
        num_of_tasks_total = 0
        num_of_completed_tasks = 0
        num_incomplete_tasks = 0
        percentage_completed = 0.0
        percentage_incomplete = 0.0
        incomplete_overdue = 0
        overdue_tasks = 0.0
        # read the file conmtents in tasks.txt
        with open('tasks.txt', 'r') as first_file:
            # print("Debug...how many lines in tasks.txt")
            first_file_out = first_file.readlines()
            # print(f"Type of data in first file: {type(first_file_out)}")
            num_of_tasks_total = len(first_file_out)
            # print(f"Length of tasks.txt contents: {num_of_tasks_total}")
            
        # open the modified_tasks.txt file to read contents
        with open('modified_tasks.txt', 'r') as second_file:
            # print("Debug...how many lines in modified_tasks.txt")
            second_file_out = second_file.readlines()
            # print(f"Type of data in second file: {type(second_file_out)}")
            num_of_completed_tasks = len(second_file_out)
            # print(f"Length of modified_tasks.txt contents: {num_of_completed_tasks}")
            
        # report generation to be written to the file task_overview.txt
        task_report_str = f"Item\t\t\t\t Statistics \n"
        task_report_str += f"=================================== \n"
        task_report_str += f"Total tasks: \t\t\t {num_of_tasks_total} \n"
        task_report_str += f"Completed tasks: \t\t {num_of_completed_tasks} \n"
        num_incomplete_tasks = num_of_tasks_total - num_of_completed_tasks
        task_report_str += f"Incomplete tasks: \t\t {num_incomplete_tasks} \n"
        percentage_completed = float((num_of_completed_tasks/num_of_tasks_total)*100)
        task_report_str += f"Completed tasks(%): \t {percentage_completed:.3f} \n"
        task_report_str += f"Incomplete overdue: \t {incomplete_overdue} \n"
        percentage_incomplete = float((num_incomplete_tasks/num_of_tasks_total)*100)
        task_report_str += f"Incomplete tasks(%): \t {percentage_incomplete:.3f} \n"
        task_report_str += f"Overdue(%): \t\t {overdue_tasks:.3f} \n"
        
        # print report
        print(task_report_str)
        # write report to task_overview.txt
        # I can choose to use the print directly to report or
        # I can use tabulate 
        if not os.path.exists("task_overview.txt"):
            with open('task_overview.txt','w') as task_report_file:
                pass
        
        # now I would do the actual writing to file task_overview.txt
        with open('task_overview.txt', 'w') as task_report:
            task_report.write(task_report_str)
            
        
        # Read from the user.txt file and generate the relevant reports for the file called
        # user_overview.txt
        # the 
        user_report_str = ""
        self.username_list = list(self.username_password.keys())
        self.password_list = list(self.username_password.values())
        total_users = 0
        # open the user.txt file to read contents
        task_contents_lists = []
        # task_contents_str = ''.join(first_file_out).strip()
        # Method 1: using append in a for loop
        # with open('tasks.txt', 'r') as second_file:
        #     for line in second_file:
        #         task_contents_lists.append(line.strip().split(','))
                
        # Method 2: Using list comprehension
        with open('tasks.txt', 'r') as f:
            task_contents_lists = [line.strip().split(',') for line in f]
        
        # get first item from each list in the
        task_owner_list = []
        for i in range(len(task_contents_lists)):
            task_owner_list.append(''.join(task_contents_lists[i]).split(';')[0])
            #print(task_owner_list) # not here as it just iterates. use outside for loop
        # print(task_owner_list)
        count = 0
        print(f"The current user is: {self.curr_user}")
        for i, item in enumerate(task_owner_list):
            if self.curr_user == item:
                count += 1
        # print(f"{self.curr_user} occurs {count} times")

        user_report_str = f"Item\t\t\t Statistics \n"
        user_report_str += f"=================================== \n"
        user_report_str += f"Current user: \t\t {self.curr_user} \n"
        total_users = len(self.username_list)
        user_report_str += f"Total users: \t\t {total_users} \n"
        total_tasks = len(task_owner_list)
        user_report_str += f"Total tasks: \t\t {total_tasks} \n"
        user_report_str += f"Assigned tasks: \t {count} \n"
        curr_user_task_percentage = (count/total_tasks)*100
        user_report_str += f"Total allocation(%): \t {curr_user_task_percentage:.3f} \n"
        

        print(user_report_str)
        # write the contents of the user_report to the user_overview.txt
        # if the file has not been created then creat it first
        if not os.path.exists("user_overview.txt"):
            with open('user_overview.txt','w') as user_report_file:
                pass
        # now I would do the actual writing to file user_overview.txt
        with open('user_overview.txt', 'w') as user_report:
            user_report.write(user_report_str)
        
        
    def display_statistics(self):
        """Only the admin has access to this function
           If the curr_user is not admin then accesss is denied.
           If the user is an admin they can display statistics about number of users
           and tasks.
           I sense this last part is to allow me display my knowledtge of
           list and string manipulation with as many different techniques I have learnt
           """
        # num_users = len(self.username_password.keys())
        # num_tasks = len(task_list)

        # print("-----------------------------------")
        # print(f"Number of users: \t\t {num_users}")
        # print(f"Number of tasks: \t\t {num_tasks}")
        # print("-----------------------------------")          
        try:
            if not self.curr_user == "admin":
                raise AuthorisationDeniedError(f"You dont have permission to view statistics as {self.curr_user}")
            else:
                print(f"Welcome {self.curr_user}!!!")
                if not os.path.exists("tasks.txt"):
                    with open('tasks.txt', 'r') as file_to_read:
                        pass

                with open('tasks.txt', 'r') as f:
                    # this is a list of lists and suitable for tabulate rendering
                    task_contents_lists = [line.strip().split(',') for line in f]
                
                # print(task_contents_lists)

                # get first item from each list in the
                task_owner_list = []
                for i in range(len(task_contents_lists)):
                    # task_owner_list.append(''.join(task_contents_lists[i]).split(';')[0])
                    task_owner_list.append(''.join(task_contents_lists[i]).split(';'))
                
                # print(task_owner_list) 
                  
                # using tabulate to display task data
                print(f"Task details before modification as read from {os.path.basename("./tasks.txt")}!!!")
                # data to display is task_content_lists
                # tablefmt can be plain, fancy_grid, jira, html, textile
                task_table = tabulate(task_owner_list, headers= ['User', 'Task title', 'Task description','Date due','Date','Status'], showindex='always') # , tablefmt='plain'
                print(task_table)

                # read from modified_tasks.txt
                with open('modified_tasks.txt', 'r') as mt:
                    # this is a list of lists and suitable for tabulate rendering
                    modified_task_contents_lists = [line.strip().split(',') for line in mt]
                
                # get first item from each list in the
                modified_task_list = []
                for i in range(len(modified_task_contents_lists)):
                    modified_task_list.append(''.join(modified_task_contents_lists[i]).split(';'))
                    
                print()
                print(f"Task details after modification as read from {os.path.basename("./modified_tasks.txt")}!!!")
                modified_task_table = tabulate(modified_task_list, headers= ['Task id', 'User', 'Task title', 'Task description','Date due','Date','Status'], showindex='always') # , tablefmt='plain'
                print(modified_task_table)
                # end of analysis for tasks.txt here

                # analysing user.txt file here
                [ret_usernames, ret_passwords] = self.retrieve_saved_users()
                # print(ret_usernames)
                # print(ret_passwords)
                print(f"S/N \t Username \t Password")
                print("====================================")
                for i in range(len(ret_usernames)):
                    print(f"{i+1}\t{ret_usernames[i]}\t\t{ret_passwords[i]}\n")
                # ends analysis of user.txt
        except AuthorisationDeniedError as ade:
            print(ade)
        else:
            pass
        finally:
            pass

    def main_menu(self): # should i pass a list of available menu options as argument
        # readeing from json dest_info file
        with open("mainmenu_info.json") as m_menu:
            m_menu_contents = m_menu.read()
        
        parsed_menu  = json.loads(m_menu_contents)
        # print(type(parsed_destinations)) # this is a dictionary
        # print(parsed_menu)

        my_menu_keys = []
        my_menu_values = []
        for key, value in parsed_menu.items():
            my_menu_keys.append(key)
            my_menu_values.append(value)
            
        # print(my_menu_keys)
        # print(my_menu_values)
        
        ret_menu_selection = ''    
        # while True:
        # presenting the menu to the user and 
        # making sure that the user input is converted to lower case.
        try:
            menu_selection = input('''Select one of the following Options below:
                r - Registering a user
                a - Adding a task
                va - View all tasks
                vm - View my task
                gr - Generate reports
                ds - Display statistics
                e - Exit
                : ''').lower()
            if not menu_selection in my_menu_keys:
                raise WrongMenuSelectionError(f"{menu_selection} is not a known menu option!!!")
        except WrongMenuSelectionError as wmse:
            print(wmse)
        else:
            ret_menu_selection = menu_selection
        finally:
            pass
        
        return ret_menu_selection
        

    def logged_in_task_selector(self, auth_dict, task_list):
        #===== display menu section =======
        #===== maybe a separate function to display menu======        
        while True:
            # presenting the menu to the user and 
            # making sure that the user input is converted to lower case.
            print()
            # menu = input('''Select one of the following Options below:
            #                 r - Registering a user
            #                 a - Adding a task
            #                 va - View all tasks
            #                 vm - View my task
            #                 gr - Generate reports
            #                 ds - Display statistics
            #                 e - Exit
            #                 : ''').lower()
            menu = self.main_menu()

            if menu == 'r':
                # add user to text file by calling the relevant function
                # above
                self.reg_user()
            elif menu == 'a':
                # add the rfelevant function here to implement add logic
                self.add_task(auth_dict, task_list)
            elif menu == 'va':
                self.view_all(auth_dict,task_list)
            elif menu == 'vm':
                self.view_mine(self.curr_user,task_list)
            elif menu == 'gr':
                self.generate_report()
            elif menu == 'ds' and self.curr_user == 'admin': 
                self.display_statistics()
            elif menu == 'e':
                print('Goodbye!!!')
                exit()
            else:
                print("You have made a wrong choice, Please Try again")
    
    def main(self):
        self.validate_module_version()
        [ret_task_dict, ret_task_list] = self.create_task_detail()
        [ret_keys_list, ret_values_list] = self.display_task_detail(ret_task_dict)        

        # compute_time = self.my_timer_decorator()
        self.compute_time()
        for i in range(len(ret_values_list)):
            print(f"{ret_keys_list[i]}:.......................{ret_values_list[i]}")
            
        [ret_logged_in, ret_auth] = self.is_logged_in(ret_keys_list, ret_values_list)
        print(f"Log in status: {ret_logged_in}")
        
        self.logged_in_task_selector(ret_auth, ret_task_list)
        
        

        #self.compute_time()
        # duration = ended-started
        # print(f"Block of code ran for {duration} seconds")
        
                
        # out = {}
        # for d in ret_task_list:
        #     out.setdefault(d["plat"], []).append(d["os_name"])
        # print(out)