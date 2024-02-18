        
# from tabulate import tabulate

# workers = [worker1, worker2]
# headers = ['Employee', 'Department']
# worker_data = [[worker.name, worker.department] for worker in workers]

# headers = ['','Employee', 'Department']
# worker_data = [[i, worker.name, worker.department] for i, worker in enumerate(workers, 1)]
# proint(tabulate(worker_data, headers=headers))

# lambdas
# when we have to sort, filter, 
# lambadas can be used to 

# pip install -r .\requirements.txt
# submit the files for capstone and requirements.txt file

# class Contact:
#     def __init__(self, name, email,phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
        
#     def display_data(self):
#         print(f"{self.name}\n "
#               f"{self.email}\n"
#               f"{self.phone}")
        
        
# class ContactList:
#     def __init__(self):
#         self.contacts = []
        
#     def add_contact(self, contact):
#         self.contacts.append(contact)
        
#     def remove_contact(self, index):
#         self.contacts.append(index)
        

# my_contact = ContactList()
# my_contact.add_contact(Contact('ona','ona@unicorngroup.com','1233455'))
# my_contact.contacts[0].display_data()

# lesson 15-02-2024

# OOP
# local and class variables

class MyClass1:

    def __init__(self, name):
        print(f"self=> >{self}<")
        self.name = name
        print(f"self.name => {self.name}")
        # self always represents the curent instanc eof the class

    def greet_and_update(self, new_name):
        local_variable = "I am a local variable"
        print(f"Hello, {self.name}!")
        print(local_variable)

# chantge the name
self.name = new_name

his_name = "Ese"
my_instance = MyClass1(his_name)

# now we call greet and update method
my_instance.greet_and_update("Alice")

print(f"Updated name: {my_instance.name}")

# access modifiers OOP
class MyClass2:

    def __init__(self):
        self.public_variable = "accessible anywhere"
        self._protected_variable = "Limited scope" 
        self.__private_variable = "Very limited scope or secret"

# how you access the variables or call them outside the class

my_object = MyClass2()

my_object.public_variable
my_object._protected_variable
# for private members, we use name mangling where
# it is accesible from a name outside the class
# not a strict access control mecvhanism, more of a convention
my_object.__private_variable # raises an error as its private. only exists inside the object and not outside

# to access it we ned to use name mangling
my_object._MyClass2__private_variable

# getters and setters are used to access ptrotected and private variables
# used for variables that have _var and __var in their names
class MyClass3:
    def __init__(self):
        self._value = 42

    def get_value(self):
        return self._value # a protected var

    def set_value(self, new_value):
        if new_value > 0:
            self._value = new_value

# craete class instance
my_instance = MyClass3()

my_instance.set_value(50)
print(my_instance.get_value())

# list comprehension
# general list comprehension
# {key: value for (key, value) in iterable if condition(key, value)}
my_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = {key: value * 2 for (key, value) in my_dict.items()}
print(new_dict)