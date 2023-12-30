import math
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
"""


class FinanceCalculator:
    def __init__(self):  # the ctor of the class
        pass
        # self.investment = investment
        # self.bond = bond

    # this function allows user sselect the type of calculator they want
    def calculator_selector(self):
        print("investment- to calculate the amount of interest "
              "you'll earn on your investment")
        print("bond-       to calculate the amount you'll have "
              "to pay on a home loan")
        user_entry = input("Select the type of "
                           "calculation you want done: ").lower()

        # use a try-catch-block here
        if(user_entry == "investment"):
            print(f"user selected {user_entry}")
        elif(user_entry == "bond"):
            print(f"user selected {user_entry}")
        else:
            print("Wrong selection...please try again")

        return user_entry

    # function to compute simple interest
    def simple_interest(self, principal, rate, tenure):
        si_amount = principal*(1+rate*tenure)

        return si_amount

    # function to compute compound interest
    def compound_interest(self, principal, rate, tenure):
        ci_amount = principal*math.pow((1+rate), tenure)

        return ci_amount

    # fucntion to compute investments
    def investment_calculator(self):
        principal_amount = float(input("Enter the initial"
                                       " deposit or principal: "))
        interest_rate = float(input("Enter the prevailing interest rate: "))
        interest_rate = interest_rate/100
        tenure = int(input("Enter the number of years to invest: "))
        interest_type = int(input("Desired interest "
                                  "type: simple(1) or compound(2): "))

        # take the selected interest type and compute the amount
        fc = FinanceCalculator()
        print("Debud...<<<")
        if(interest_type == 1):
            print("Simple interest calculator selected")
            computed_simple_interest = fc.simple_interest(principal_amount, interest_rate, tenure)
            print(f"Simple interest is: ${computed_simple_interest:,.2f}")
            print(f"Current total amount is: ${principal_amount+computed_simple_interest:,.2f}")
        elif(interest_type == 2):
            print("Compound interest calculator selected")
            computed_comp_interest = fc.compound_interest(principal_amount, interest_rate, tenure)
            print(f"Compound interest is: ${computed_comp_interest:,.2f}")
            print(f"Compounded total amount is: ${principal_amount+computed_comp_interest:,.2f}")
        else:
            print("Not a known interest selection")

    # fucntion to compute investments
    def home_loans_repayment_calculator(self):
        # making the bond function functionality
        present_value = float(input("Enter the initial"
                                    "deposit or principal: "))
        interest_rate = float(input("Enter the "
                                    "prevailing interest rate: "))
        # interest_rate = interest_rate/100
        tenure = int(input("Enter the duration to invest: "))
        # print(f" Repayment on loan is: ${repayment:,.2f}")
        print(f"Present value: ${present_value:,.2f}")
        print(f'interest rate: {interest_rate}')
        print(f"The repayment tenure: {tenure}")

        # repayment = (interest_rate*present_value)/(1-(1-interest_rate)**(-tenure))
        beta = (1-interest_rate)**(tenure)
        repayment = ((interest_rate*present_value)*beta)/(beta-1)
        # print(f"Repayment on loan is: ${repayment}")
        print(f"Repayment on loan is: ${repayment:,.2f}")

    # this function is the main function that starts program execution
    def main(self):
        fc = FinanceCalculator()
        sel = fc.calculator_selector()

        if(sel == "investment"):
            fc.investment_calculator()
        elif(sel == "bond"):
            fc.home_loans_repayment_calculator()
        else:
            print("Do nothing")


# here the main method is called
if __name__ == '__main__':
    fc_init = FinanceCalculator()
    fc_init.main()
