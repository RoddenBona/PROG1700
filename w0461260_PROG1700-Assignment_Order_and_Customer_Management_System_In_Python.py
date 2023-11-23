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

customers = {1: {"name": "Alice", "contact": "123-456-7890", "orders": ["hey","this is","a test"]},
            2: {"name": "Bob", "contact": "987-654-3210", "orders": []},
            }

number_of_entries = len(customers)

def customer_addition():
    while True:
        add_option = input("""Do you wish to add a ne customer?
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
                main_menu()
            else:
                if add_option == 2:
                    print("Exiting to main menu")
                    main_menu()
                else:
                    print("invalid entry. Please enter option as a number")

def order_placement(customerID, product_name, quantity, unit_price):
    print("test")
    main_menu()

def report_one(customerID):
    while True:
        report_option = input("""Do you wish to generate a report of the selected customer?
                              1)Yes
                              2)No
                              Enter option here: """)
        if report_option.isdigit():
            report_option = int(report_option)
            if report_option == 1:
                print("test. You inputed", report_option)
                main_menu()
            else:
                if report_option == 2:
                    print("Exiting to main menu")
                    main_menu()
                else:
                    print("Invalid entry. Please enter option as a number")

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
            else:
                if report_choice == 2:
                    print("Exiting to main menu")
                    main_menu()
                else:
                    print("invalid entry. Please enter option as a number")

def main_menu():
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
                    order_placement()
                else:
                    if menu_choice == 3:
                        customer_search = input("Enter CustomerID")
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
                                print("Invalid entry. Please enter option as a number")

main_menu()

# This is how to print/access the list inside of the dictionary
# Which is in another dictionary itself 
# print(customers[1]["orders"])