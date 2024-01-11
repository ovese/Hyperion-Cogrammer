import numpy as np
import pandas as pd
import math

"""The program works with a cafe menu
    It contains different wors regiuonal menus
    each regional menu psssesses categories and
    within each category are types of meals
    
"""

class MissingInputError(Exception):
    pass

class UnknownMenuEntryError(Exception):
    pass

class Restaurant():
    def __init__(self, menu_locale, menu_category, menu_type ):
        self.menu_locale = menu_locale
        self.menu_category = menu_category
        self.menu_type = menu_type
        
    def get_menu_locale_list(self):
        list_menu_locale = ["african","american","asiatic","european","mediterranean"]
        print(f"The world menus to choose from are:\n"
              f"1. {list_menu_locale[0].capitalize()} \n"
              f"2. {list_menu_locale[1].capitalize()}\n"
              f"3. {list_menu_locale[2].capitalize()}\n"
              f"4. {list_menu_locale[3].capitalize()}\n"
              f"5. {list_menu_locale[4].capitalize()}\n")
        
        return list_menu_locale
    
    def get_menu_category_list(self):
        list_menu_category = ["entree","main course","dessert"]
        print(f"The world menus to choose from are:\n"
              f"1. {list_menu_category[0].capitalize()} \n"
              f"2. {list_menu_category[1].capitalize()}\n"
              f"3. {list_menu_category[2].capitalize()}\n"
              f"4. {list_menu_category[3].capitalize()}\n")
        
        return list_menu_category

    """ menu locale can be 
        mediteranean
        asiatic
        european
        african
        american
    """
    def get_locale(self):
        current_menu_locale = self.get_menu_locale_list()
        try:
            menu_region = input("Preferred menu locale: ").lower()
            if menu_region == "" or len(menu_region) == 0:
                raise MissingInputError(f"Error: Missing input detected")
            elif menu_region not in current_menu_locale:
                raise UnknownMenuEntryError(f"Error: Unknown menu entry detected as {menu_region}")
        except MissingInputError as input_error:
            print(input_error)
        except UnknownMenuEntryError as entry_error:
            print(entry_error)
        else:
            if menu_region == "african":
                self.menu_locale = menu_region
            elif menu_region == "european":
                self.menu_locale = menu_region
            elif menu_region == "asiatic":
                self.menu_locale = menu_region
            elif menu_region == "mediterranean":
                self.menu_locale = menu_region
            elif menu_region == "american":
                self.menu_locale = menu_region
            else:
                print("Not a known world menu") # does this do anything
        finally:
            print("Finished selecting the menu locale")
        
        return self.menu_locale
    
    def stock_value(self):
        current_menu_locale = self.get_menu_locale_list()
        # vcreate a tuple of key-value pairs
        list_stock = [(current_menu_locale[0],13),(current_menu_locale[1],24),
                     (current_menu_locale[2],9), (current_menu_locale[3],17),
                     (current_menu_locale[4],33)]
        
        print(type(list_stock))
        print(list_stock)
        
        dict_stock = dict(list_stock)
        print(type(dict_stock))
        print(dict_stock)
        
        return dict_stock
    