from financial_calculator import FinanceCalculator

# creating an instance of the FinancialCalculator class
fc = FinanceCalculator()


# this function is the main function that starts program execution
def main():
    sel = fc.calculator_selector()

    if(sel == "investment"):
        fc.investment_calculator()
    elif(sel == "bond"):
        fc.home_loans_repayment_calculator()
    else:
        print("Do nothing")


# here the main method is called
if __name__ == '__main__':
    main()
