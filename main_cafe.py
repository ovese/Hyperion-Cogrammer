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
        
        
if __name__ == "__main__":
    main()
