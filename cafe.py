import numpy as np
import pandas as pd
import math

"""The program works with a cafe menu
    It contains different menu items
    each menu item possesses value and
    within each value are prices
    
"""

class MissingInputError(Exception):
    pass

class UnknownMenuEntryError(Exception):
    pass

class Warehouse():
    def __init__(self, stock_name ):
        self.stock_name = stock_name

        
    def get_menu_list(self):
        menu_list = ["bread","olive oil","rice","sugar","water"]
        print(f"The menu items to choose from are:\n"
              f"1. {menu_list[0].capitalize()} \n"
              f"2. {menu_list[1].capitalize()}\n"
              f"3. {menu_list[2].capitalize()}\n"
              f"4. {menu_list[3].capitalize()}\n"
              f"5. {menu_list[4].capitalize()}\n")
        
        return menu_list


    """ menu todo
    """
    def get_menu(self, current_menu):
        # current_menu = self.get_menu_list()
        try:
            my_menu_item = input("Enter preferred menu: ").lower()
            if my_menu_item == "" or len(my_menu_item) == 0:
                raise MissingInputError(f"Error: Missing input detected")
            elif my_menu_item not in current_menu:
                raise UnknownMenuEntryError(f"Error: Unknown menu entry detected as {my_menu_item}")
        except MissingInputError as input_error:
            print(input_error)
        except UnknownMenuEntryError as entry_error:
            print(entry_error)
        else:
            if my_menu_item == "bread":
                self.stock_name = my_menu_item
            elif my_menu_item == "oil":
                self.stock_name = my_menu_item
            elif my_menu_item == "rice":
                self.stock_name = my_menu_item
            elif my_menu_item == "sugar":
                self.stock_name = my_menu_item
            elif my_menu_item == "water":
                self.stock_name = my_menu_item
            else:
                print("Not a known menu item") # does this do anything
        finally:
            print("Finished selecting the menu items")
        
        return self.stock_name
    
    def stock_value(self, current_menu):
        # current_menu = self.get_menu_list()
        # vcreate a tuple of key-value pairs
        list_stock_value = [(current_menu[0],13),(current_menu[1],24),
                     (current_menu[2],9), (current_menu[3],17),
                     (current_menu[4],33)]
        
        # print(type(list_stock_value))
        # print(list_stock_value)
        
        dict_stock = dict(list_stock_value)
        # print(type(dict_stock))
        # print(dict_stock)
        
        return dict_stock
    
    
    def stock_price(self, current_menu):
        # current_menu = self.get_menu_list()
        # vcreate a tuple of key-value pairs
        list_stock_price = [(current_menu[0],100.45),(current_menu[1],325.96),
                     (current_menu[2],90.12), (current_menu[3],170.67),
                     (current_menu[4],100.33)]
        
        # print(type(list_stock_price))
        # print(list_stock_price)
        
        dict_stock_price = dict(list_stock_price)
        # print(type(dict_stock_price))
        # print(dict_stock_price)
        
        return dict_stock_price
    
    
    def total_stock(self, current_stock):
        ret_stock_value = self.stock_value(current_stock)
        ret_stock_price = self.stock_price(current_stock)
        
        print("Stock\t\t\tQuantity\t\tPrice\t\t\tTotal-stock")
        print("--------------------------------------------------------------------------------------")
        for key,value in ret_stock_value.items():
            print(f"{key.capitalize()}\t\t\t{ret_stock_value[key]}\t\t\t"
                  f"${ret_stock_price[key]:,.2f}\t\t\t${ret_stock_value[key]*ret_stock_price[key]:,.2f}")
        
        print("\n")
        total_stock_worth = 0.0
        for key,value in ret_stock_value.items():
            total_stock_worth += (ret_stock_value[key]*ret_stock_price[key])
        
        print(f"Total stock capacity is:............................................... ${total_stock_worth:,.2f}")
        
        
    

    def get_menu_listv2(self):
        menu_list = ["bread","olive oil","rice","sugar","water"]
        print("The menu items to choose from are:")
        for i in range(len(menu_list)):
            print(f"{i+1}. {menu_list[i].capitalize()}")
        
        return menu_list
    
    
    def populate_stock_quantity(self, stock_list):
        pass
        
    