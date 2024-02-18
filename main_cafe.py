from cafe import Warehouse

stock = Warehouse("")

stock_options_list = stock.get_menu_list()

def main():
    # todo     
    # my_stock = stock.get_menu(stock_options_list)
    
    stock_value_dict = stock.stock_value(stock_options_list) # returns dictionnary
    
    print("\n")
    print("Stock\t\tQuantity")
    print("---------------------------------")
    for key,val in stock_value_dict.items():
        print(f"{key.capitalize()}\t\t{val}")
    
    print("\n")
    stock_price_dict = stock.stock_price(stock_options_list)
    print("Stock\t\tPrice")
    print("---------------------------------")
    for key,val in stock_price_dict.items():
        print(f"{key.capitalize()}\t\t${val:,.2f}")
    
    print("\n")    
    # finally we conpute the stock balance
    stock.total_stock(stock_options_list)
    
    # print("\n")
    # print("*************Extending functionality of requested code**********")
    
    # stock.get_menu_listv2()
    
    # print("\n")
    
    # ret_stock_value_list = stock.populate_stock_quantity(stock_options_list)
    # print(ret_stock_value_list)
    
    # print("\n")
    # ret_stock_value_dict = stock.create_stock_balance(stock_options_list, ret_stock_value_list)
    # print(type(ret_stock_value_dict))
    # print(ret_stock_value_dict)
    
    # print("\n")
    # ret_updated_stock_list = stock.add_to_stock(stock_options_list)
    # print(ret_updated_stock_list)
    
    # print("\n")
    # new_stock_value_list = stock.populate_stock_quantity(ret_updated_stock_list)
    # print(new_stock_value_list)


if __name__ == "__main__":
    main()
