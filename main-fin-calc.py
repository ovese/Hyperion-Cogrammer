from financial_calculator import FinanceCalculator

# creating an instance of the FinancialCalculator class
fc = FinanceCalculator()


# this function is the main function that starts program execution
def main():
    # [inv_js, bond_js] = fc.read_config_json()
    # print(f"From json {inv_js}")
    # print(f"From json {bond_js}")

    # [inv_ini, bond_ini] = fc.read_config_ini()
    # print(f"From ini {inv_ini}")
    # print(f"From ini {bond_ini}")

    sel = fc.calculator_selector()

    if (sel == "investment"):
        fc.investment_calculator()
    elif (sel == "bond"):
        fc.home_loans_repayment_calculator()
    else:
        print("Do nothing")


# here the main method is called
if __name__ == '__main__':
    main()
