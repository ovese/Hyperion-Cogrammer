import math
from configparser import ConfigParser
import json
"""
This program is a financial services calculator
It is able to compute interest on two types of financial instruments
The first is an investment calculator
Second is a home loans repayment calculator
This program will make use of certain python constructs
object oriented programming will be used
functions are going to be employed
style checking for consistency is also employed
exception checking will also be done using
try-throw-finally statements or the more complete
try-except-else-finally block style
I have also experimented with config files.
Two types of config files were used here and
could be selected from to choose options
I used an ini and json config option to read the calculator
type needed
"""


class WrongSelectionError(Exception):
    pass


class FinanceCalculator:
    def __init__(self):  # the ctor of the class
        pass
        # self.principal = principal

    def read_config_json(self):
        with open("fin_calc_conf.json", "r") as jsonfile:
            jsondata = json.load(jsonfile)
            print("Read successful")
            jsonfile.close()  # is this necessary when suing with

        # print(data)
        inv_opt = jsondata["A"]
        bond_opt = jsondata["B"]

        return (inv_opt, bond_opt)

    def read_config_ini(self):
        # Read config.ini file
        config_object = ConfigParser()
        config_object.read("fin_calc_conf.ini")

        # Get the investment options from here
        calcinfo = config_object["CALCINFO"]
        # get the investment option
        investment_option = calcinfo["A"]
        # get the bond option
        bond_option = calcinfo["B"]

        return (investment_option, bond_option)

    # this function allows user to select the type of calculator they want
    def calculator_selector(self):
        try:
            # I am returning the calculator iption shere for ini file
            [inv_opt, bond_opt] = self.read_config_ini()

            print(f"{inv_opt}- to calculate the amount of interest "
                  "you'll earn on your investment")
            print(f"{bond_opt}-       to calculate the amount you'll have "
                  "to pay on a home loan")
            user_entry = input("Select the type of "
                               "calculation you want done: ").lower()
            if not (user_entry == "investment" or user_entry == "bond"):
                raise WrongSelectionError(f"Error: wrong entry made")
        except WrongSelectionError as selection_error:
            print(selection_error)
        else:
            if (user_entry == "investment"):
                user_entry = inv_opt
                print(f"user selected {user_entry}")
            elif (user_entry == "bond"):
                user_entry = bond_opt
                print(f"user selected {user_entry}")
        finally:
            print("Program is being executed")

        return user_entry.lower()  # had to format this as I am using the config file returned variables

    # function to compute simple interest
    def simple_interest(self, principal, rate, tenure):
        si_amount = principal*(1+(rate*tenure))

        return si_amount

    # function to compute compound interest
    def compound_interest(self, principal, rate, tenure):
        ci_amount = principal*math.pow((1+rate), tenure)

        return ci_amount

    def compute_bond(self, principal, rate, tenure):
        print(f"Principal: {principal}")
        print(f"Rate: {rate}")
        print(f"Tenure: {tenure}")
        repayment = (rate*principal)/(1-math.pow((1+rate), -tenure))
        print(f"Computed repayment is: {repayment}")

        bond_repayment = repayment

        return bond_repayment

    # fucntion to compute investments
    def investment_calculator(self):
        principal_amount = float(input("Enter the initial"
                                       " deposit or principal: "))
        interest_rate = float(input("Enter the prevailing interest rate: "))
        interest_rate = interest_rate/(100)
        tenure = int(input("Enter the number of years to invest: "))
        interest_type = int(input("Desired interest type:\n"
                                  "1.\t\tSimple interest \n"
                                  "2.\t\tCompound interest \n"
                                  "Select option: "))

        # take the selected interest type and compute the amount
        # fc = FinanceCalculator()
        print("Debug...<<<")
        if (interest_type == 1):
            print("Simple interest calculator selected with parameters: ")
            print(f"Principal:.........${principal_amount:,.2f}\n"
                  f"Interest rate.......{interest_rate}\n"
                  f"Tenure..............{tenure} year(s)\n")
            computed_simple_interest = self.simple_interest(principal_amount, interest_rate, tenure)
            print(f"Simple interest is: ${computed_simple_interest:,.2f}")
            print(f"Current total amount is: "
                  f"${principal_amount+computed_simple_interest:,.2f}")
        elif (interest_type == 2):
            print("Compound interest calculator selected with parameters: ")
            print(f"Principal:.........${principal_amount:,.2f}\n"
                  f"Interest rate.......{interest_rate}\n"
                  f"Tenure..............{tenure} year(s)\n")
            computed_comp_interest = self.compound_interest(principal_amount, interest_rate, tenure)
            print(f"Compound interest is: ${computed_comp_interest:,.2f}")
            print(f"Compounded total amount is: "
                  f"${principal_amount+computed_comp_interest:,.2f}")
        else:
            print("Not a known interest selection")

    # fucntion to compute investments
    def home_loans_repayment_calculator(self):
        # making the bond function functionality
        present_value = float(input("Enter the initial "
                                    "deposit or principal: "))
        interest_rate = float(input("Enter the "
                                    "prevailing interest rate: "))
        tenure = int(input("Enter the duration to invest in months "))
        # print(f" Repayment on loan is: ${repayment:,.2f}")
        print(f"Present value..........${present_value:,.2f}")
        print(f'Interest rate..........{interest_rate}')
        print(f"Repayment tenure.......{tenure} months")

        # fc = FinanceCalculator()
        bond_repayment = self.compute_bond(present_value, interest_rate/(1200), tenure)
        print(f"In {tenure} months, repayment on loan is: "
              f"${bond_repayment:,.2f}")
        print(f"Accrued compound interest on loan is: "
              f"${(present_value+bond_repayment):,.2f}")
