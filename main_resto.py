from resto import Restaurant

def main():
    my_resto = Restaurant(" "," "," ")
    # my_cafe.get_menu_locale_list()
    
    sel_locale = my_resto.get_locale()
    print(f"You have selected {sel_locale}, cuisine")
    
    ret_stock = my_resto.stock_value()
    keys = ret_stock.keys()
    values = ret_stock.values()
    print(f"{ret_stock.items()}")
    print("Menu\t\t Quantity")
    for key in ret_stock.keys():
        print(f"{key.capitalize()} \t {ret_stock[key]}")
    
    
    
    
if __name__ == "__main__":
    main()