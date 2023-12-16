#putting all item, price and its stock in a list 
menu_items={
    "Snacks":{
        "A01":{"name":"Piatos","price": 1.50, "stock": 10},
        "A02":{"name":"Cheetos","price": 3.75, "stock": 1},
        "A03":{"name":"Pringles","price": 5.00, "stock": 4},
        "A04":{"name":"V-cut","price": 3.50, "stock": 10},
    },
    "Drinks": {
         "B01":{"name":"Coca-Cola","price": 6.00, "stock": 3},
         "B02":{"name":"Water","price": 1.00, "stock": 10},
         "B03":{"name":"Sprite","price": 4.75, "stock": 2},
         "B04":{"name":"Fanta","price": 3.75, "stock": 5},
},
    "Sweets": {
         "C01":{"name":"Snickers","price": 4.00, "stock": 6},
         "C02":{"name":"Mars","price": 5.25, "stock": 7},
         "C03":{"name":"Cookie4U","price": 6.75, "stock": 2},
         "C04":{"name":"Jelly Beans","price": 7.75, "stock": 1},
},
}
#to print the menu for the user to see 

def print_menu(menu_items):
    print ("\n-----HELLO!!! WELCOME TO JJs VENDING MACHINE!!!-----\n")
    print("Menu:\n")
    for category, category_items in menu_items.items():
        print(category+":")
        for code,item in category_items.items():
            print(f'{code}: {item["name"]} (${item["price"]:.2f})')
        print()

#getting the input from the user on what they want to purchase

def get_code(menu_items):
    while True:
        code=input("Enter the Code of your item:")
        for category ,category_items in menu_items.items():
            if code in category_items:
                return code
            #print("INVALID CODE--Please try again:)")

# it ask how many money you inserted, if it is not a float it will say invalid code and have to insert a number

def get_money(menu_items,code):
    for category,category_items in menu_items.items():
        if code in category_items:
            item = category_items[code]
            break

    else:
         print(f'INVALID CODE "{code}".')
         return
        
    while True:
          money=float(input("Enter money: "))

          if money >= item["price"]:
           return money          
          print ( f'NOT ENOUGH MONEY! ---Add more ${item["price"]- money:.2f} more.')

#with the item you have purchase, it will take your money and give you change 

def dispense_item(menu_items,code,money):
    for category,category_items in menu_items.items():
        if code in category_items:
            item=category_items[code]
            break
    else:
        print(f'INVALID CODE "{code}".')
        return
    
    if item["stock"]>0:
        print(f'\nDispensing {item["name"]}...')
        change=money- item["price"]
        item["stock"]-=1
        print (f"Returning ${change:.2f} change...\n")
    else:
        print(f'\nERROR:{item["name"]}is out of stock.')

#suggesting another item for the user to buy

def suggest_purchase(menu_items,code):
    if code in menu_items["Drinks"]:
        print("You might also like: ")
        for code,item in menu_items["Snacks"].items():
            print(f'{code}:{item["name"]}({item["price"]:.2f}$)')
    elif code in menu_items["Snacks"]:
        print("You might also like: ")
        for code, item in menu_items["Drinks"].items():
            print(f'{code}:{item["name"]} ({item["price"]:.2f}$)')

while True:
    print_menu(menu_items)
    code= get_code(menu_items)
    money=get_money(menu_items,code)
    dispense_item(menu_items,code,money)
    suggest_purchase(menu_items,code)

    while True:
        response=input("\nWould you like to purchase more from the menu? (yes/no:")
        if response.lower()== "yes":
            break
        elif response.lower()=="no":
            print("Thank you for buying at JJs Vending Machine!!!")
            exit()
        else:
            print("ERROR: INVALID RESPONSE!!!!-- Please try again :)")


