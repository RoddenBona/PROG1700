"""
Author: Rodden Bona
ID: W0461260
Course: PROG1700
Assignment: Order and Customer Management System
Module: Data Structures
Approach: Procedural Programming with Functions
Language: Python 3
Created: Nov 22 2023
Last edited Nov 22 2023
"""

customers = {1: {"name": "Alice", "contact": "123-456-7890", "orders": []},
            2: {"name": "Bob", "contact": "987-654-3210", "orders": []},
            }

number_of_entries = len(customers)

def customer_addition():
    while True:
        add_option = input("""Do you wish to add a new customer?
                        1)Yes
                        2)No
                        Enter option here: """)
        if add_option.isdigit():
            add_option = int(add_option)
            if add_option == 1:
                add_fname = input("Enter new customer first name: ")
                add_contact = input("Enter new cusomter contact number: ")
                new_id = number_of_entries + 1
                customers[new_id] = {"name":add_fname, "contact":add_contact, "orders":[]}
                print("New entry has been added")
                break
            else:
                if add_option == 2:
                    print("Exiting to main menu")
                    break
                else:
                    print("invalid entry. Please enter option as a number")
        else:
            print("Invalid entry. Please enter a number")

def order_placement(customerID, product_name, quantity, unit_price):
    number_of_orders = len(customers[customerID]["orders"])
    while True:
        order_choice = input("""Would you like to place a new order for this customer?
                             1)Yes
                             2)No
                             Enter option here: """)
        if order_choice.isdigit():
            order_choice = int(order_choice)
            if order_choice == 1:
                new_id = number_of_orders + 1
                new_order = {"OrderID":new_id, "product":product_name, "quantity":quantity, "price":unit_price}
                customers[customerID]["orders"].append(new_order)
                print("Order has been added")
                break
            else:
                if order_choice == 2:
                    print("Exiting to main menu")
                    break
                else:
                    print("Invalid entry. Option not in list")
        else:
            print("Invalid entry. Please enter a number")

def report_one(customerID):

    customer = customers[customerID]["orders"]
    name = customers[customerID]["name"]
    x = 0
    total = 0
    for items in (customers[customerID]["orders"]):
        quant = int(customers[customerID]["orders"][x]["quantity"])
        price = int(customers[customerID]["orders"][x]["price"])
        current = (quant * price)
        total = total + current
        x = x + 1




    while True:
        report_option = input("""Do you wish to generate a report of the selected customer?
                              1)Yes
                              2)No
                              Enter option here: """)
        if report_option.isdigit():
            report_option = int(report_option)
            if report_option == 1:
                print(f"Customer report for {name}")
                for order in customer:
                    print(order)
                print(f"Total spending is: {total}")
                break
            else:
                if report_option == 2:
                    print("Exiting to main menu")
                    break
                else:
                    print("Invalid entry. Option not in list")
        else:
            print("invalid entry. Please input a number")

def report_all():
    while True:
        report_choice = input("""Do you wish to generate a report of all customers
                            1)Yes
                            2)No
                            Enter option here: """)
        if report_choice.isdigit:
            report_choice = int(report_choice)
            if report_choice == 1:
                    print(customers)
                    break
            else:
                if report_choice == 2:
                    print("Exiting to main menu")
                    break
                else:
                    print("invalid entry. Option not in list")
        else:
            print("Invalid entry. Please enter a number")

while True:
    menu_choice = input("""Please select an option
                        1)Add New customer
                        2)Place order
                        3)Generate report
                        4)Generate all reports
                        5)Exit
                        Enter option here: """)
    if menu_choice.isdigit():
        menu_choice = int(menu_choice)
        if menu_choice == 1:
            customer_addition()
        else:
            if menu_choice == 2:
                customer_search = input("Enter Customer ID: ")
                if customer_search.isdigit:
                    customer_search = int(customer_search)
                    if customer_search in customers:
                        customerID = customer_search
                        product_name = input("Enter product name: ")
                        quantity = input("Enter quantity of product: ")
                        if quantity.isdigit():
                            quantity = int(quantity)
                            unit_price = input("Enter price of the product in whole ollars: ")
                            if unit_price.isdigit():
                                unit_price = int(unit_price)
                                order_placement(customerID,product_name,quantity,unit_price)
                            else:
                                print("Invalid entry")
                        else:
                            print("Invalid entry")
                    else:
                        print("Invalid entry")
                else:
                    print("Invalid entry")
            else:
                if menu_choice == 3:
                    customer_search = input("Enter Customer ID")
                    if customer_search.isdigit():
                        customer_search = int(customer_search)
                    if customer_search in customers:
                        customerID = customer_search
                        report_one(customerID)
                else:
                    if menu_choice == 4:
                        report_all()
                    else:
                        if menu_choice == 5:  
                            print("Exiting program. Thank you for your time")
                            break
                        else:
                            print("Invalid entry. Option not in list")
    else:
        print("Invalid entry. Please enter a number")

# This is how to print/access the list inside of the dictionary
# Which is in another dictionary itself 
# print(customers[1]["orders"])

#Current goal
#get report one working with total spending included