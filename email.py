### --- OOP Email Simulator --- ###
# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Emails():
    
    # classs variable with default value
    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    
    # --- Lists --- #
    # Initialise an empty list to store the email objects.
    inbox = []
    
    def __init__(self, email_address, subject_line, email_content):
        """Takes params:
           email address
           subject line
           email content
           """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
 
    # Initialise the instance variables for emails.

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        pass

    # --- Functions --- #
    # Build out the required functions for your program.

    def populate_inbox(self):
        
        # Create 3 sample emails and add it to the Inbox list. 
        mail1 = Emails('abc@doublenet.com','procurement','Requesting the procurement manager to make requisitionj for new rigs')
        mail2 = Emails('def@yahoo.com','sales','Meeting agenda for quarterly sales discussion and future scoping of clients')
        mail3 = Emails('xyz@gmail.com','program management','Team building sessions to inform all stakeholders of the program plan')
        self.inbox.append(mail1.email_address)
        self.inbox.append(mail1.subject_line)
        self.inbox.append(mail1.email_content)
        
        self.inbox.append(mail2.email_address)
        
        self.inbox.append(mail3.email_address)

    def list_emails(self):
        
        # Create a function which prints the email’s subject_line, along with a corresponding number.
        pass

    def read_email(self, index):

        # Create a function which displays a selected email. 
        # Once displayed, call the class method to set its 'has_been_read' variable to True.
        my_item = self.inbox
        print(my_item)

# --- Email Program --- #
email = Emails('','','')
# Call the function to populate the Inbox for further use in your program.
email.populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        email.read_email(1)
        
    elif user_choice == 2:
        # add logic here to view unread emails
        pass
            
    elif user_choice == 3:
        # add logic here to quit appplication
        exit()

    else:
        print("Oops - incorrect input.")
        
