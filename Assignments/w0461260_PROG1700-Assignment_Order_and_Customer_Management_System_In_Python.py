"""
Author: Rodden Bona
ID: W0461260
Course: PROG1700
Assignment: Order and Customer Management System
Module: Data Structures
Approach: Procedural Programming with Functions
Language: Python 3
Created: Nov 22 2023
Last edited Nov 29 2023
"""

#Defining the main customer table as a variable
customers = {1: {"name": "Alice", "contact": "123-456-7890", "orders": []},
            2: {"name": "Bob", "contact": "987-654-3210", "orders": []},
            }

#The count of customers in the customers variable
#Mainly used in adding a new customer and nothing else
number_of_entries = len(customers)

#First defined function: Adding a customer into the database
def customer_addition():
    while True: #For loop for the menu
        add_option = input("""Do you wish to add a new customer?
                        1)Yes
                        2)No
                        Enter option here: """) #User asked whether or not they want to add a customer or not?
        if add_option.isdigit(): 
            add_option = int(add_option)
            if add_option == 1: #If the option is 1(yes)
                add_fname = input("Enter new customer first name: ") #Enter the customers name
                add_contact = input("Enter new cusomter contact number: ") #Enter their phone number
                new_id = number_of_entries + 1 #using the number_of-entries variable to give the customer a unique ID by adding one to the number of current unique entries
                customers[new_id] = {"name":add_fname, "contact":add_contact, "orders":[]} #Add the entered inforation and add it to the new id which will become a new entry in the set
                print("New entry has been added")
                break #Conformation of entry and breaking the loop which brings us back to the main menu
            else:
                if add_option == 2:
                    print("Exiting to main menu") #If the option is 2(no) the loop breaks bringing user to main menu
                    break
                else:
                    print("invalid entry. Option not available") #Error if the inputed option isn't isn't available
        else:
            print("Invalid entry. Please enter a number") #Error if option is not a digit

#Function 2: placing an order
def order_placement(customerID, product_name, quantity, unit_price):
    number_of_orders = len(customers[customerID]["orders"]) #Variable for counting now many orders user already has if any
    while True:
        order_choice = input("""Would you like to place a new order for this customer?
                             1)Yes
                             2)No
                             Enter option here: """) #Same selectio menu. every function has this menu
        if order_choice.isdigit():
            order_choice = int(order_choice)
            if order_choice == 1: #If option is yes
                new_id = number_of_orders + 1 #Assign order to number of orders plus one
                new_order = {"OrderID":new_id, "product":product_name, "quantity":quantity, "price":unit_price} #The provided variable are in the main menu where the user will be prompted to add in the details there before moving on
                customers[customerID]["orders"].append(new_order)
                print("Order has been added")      #Append enterd dictionary of items into the end list of orders in customers
                break
            else:
                if order_choice == 2:
                    print("Exiting to main menu") #Exit to main menu
                    break
                else:
                    print("Invalid entry. Option not available") #Option not vailable message
        else:
            print("Invalid entry. Please enter a number") #Invalid entry message

#Function 3: Reporting the order of a single customer
def report_one(customerID):
    #Now I admit this was the hardest one to program in. Simply because of the total spending part of the code
    #Along with the difficulty of accesing the orders list of dictionaries in the customer set
    #I know there's an easier way fo doing this, probably. And that this is the caveman's solution to it.
    #But I legit could not get it to work in any other way of doing it.

    customer = customers[customerID]["orders"] #Set variable to the orders section of the customers info
    name = customers[customerID]["name"] #The a variable to the customers name. Both of these are done for simplicity's sake
    x = 0 #Set a variable as 0 for the below total spending calculator code
    total = 0 #Total varibale for the total spending calculator
    for items in (customers[customerID]["orders"]): #For the amount of orders in the customer's order list
        quant = float(customers[customerID]["orders"][x]["quantity"]) #Grab the item quantity of x in the list
        price = float(customers[customerID]["orders"][x]["price"])  #grab the price of x in the list
        current = (quant * price) #Current price of x in the list is quantity of items times the price of said items 
        total = total + current #Add the current price to the total price variable
        x = x + 1 #Increase x by 1 to run through the next item in the list of orders
    total = round(total,3) #After creating the total price in the for loop. Round total price to 3 (Which is actually the second decimal)
    """Intrestingly w3schools has this wrong in their round() page. Unless something in python or vscode as changed.
    But in w3schools it says that round(x , 2) will give the variable rounded to 2 decimals. Which flat out doesn't work here.
    Instead to get 2 decimals. i had to do round(x , 3) Which did lead to printing a variable of 3 decimal places.
    I don't know why this is how it works. But somethings not right here, whatever it is."""

#Ok now we can go onto creating the report itself. All that before was just to get a total value variable
    while True:
        report_option = input("""Do you wish to generate a report of the selected customer?
                              1)Yes
                              2)No
                              Enter option here: """)#Same option menu
        if report_option.isdigit():
            report_option = int(report_option)
            if report_option == 1: #Choice 1 is the print the report
                print(f"Customer report for {name}") #Little message of who's report this is
                for order in customer:
                    print(order) #Simply print the orders. Which were set onto the order variable used here
                print(f"Total spending for this customer is: {total}") #Now tell the total spending of the selected customer
                break #Break while loop and return to main menu
            else:
                if report_option == 2:
                    print("Exiting to main menu") #return to main menu
                    break
                else:
                    print("Invalid entry. Option not in list")#Invalid option
        else:
            print("invalid entry. Please input a number")#Invalid entry

#Function 4: report all entries in the customer table
def report_all():
    while True:
        report_choice = input("""Do you wish to generate a report of all customers
                            1)Yes
                            2)No
                            Enter option here: """) #Same yes or no choice
        if report_choice.isdigit:
            report_choice = int(report_choice)# If option is yes
            if report_choice == 1:
                    print(customers) #Simply print the customer table as is
                    break
            else:
                if report_choice == 2:
                    print("Exiting to main menu") #If no. Exit to menu
                    break
                else:
                    print("invalid entry. Option not in list") 
        else: #Same two error messages. This is easily the simplest part of the program
            print("Invalid entry. Please enter a number")


#Here is the main menu for the program
while True:
    menu_choice = input("""Please select an option
                        1)Add New customer
                        2)Place order
                        3)Generate report
                        4)Generate all reports
                        5)Exit
                        Enter option here: """) #List of all available functions to access
    if menu_choice.isdigit():
        menu_choice = int(menu_choice)
        if menu_choice == 1:
            customer_addition() #If option 1 is selected perform customer addition function
        else:
            if menu_choice == 2:
                customer_search = input("Enter Customer ID: ") #Now option 2 is a bit more complicated
                if customer_search.isdigit: #First the program asks for a customer ID to search in the set
                    customer_search = int(customer_search)
                    if customer_search in customers: #If the customer is found in the table
                        customerID = customer_search #Set the desired ID for the program to the searched ID
                        product_name = input("Enter product name: ") #Now input the name of the product which the customer is ordering
                        quantity = input("Enter quantity of product: ") #Quantity of the desired product is then asked for
                        if quantity.isdigit():
                            quantity = int(quantity) #Check if the quantity is a whole decimal number
                            unit_price = input("Enter price of the product in whole ollars: ")
                            unit_price = float(unit_price) #Now enter the price of the product
                            order_placement(customerID,product_name,quantity,unit_price)
                        else:
                            print("Invalid entry") #Error if quantity is not a whole number
                    else:
                        print("Invalid entry. Customer not found") #If searched id doesn't appear in the customers set
                else:
                    print("Invalid entry. Please enter a number") #Error if digit is not entered
            else:
                if menu_choice == 3: #Option 3. report one customer
                    customer_search = input("Enter Customer ID: ") #Enter ID of customer
                    if customer_search.isdigit():
                        customer_search = int(customer_search) #If customer ID is found in the customers set
                    if customer_search in customers:
                        customerID = customer_search
                        report_one(customerID) #Start report one function with customer ID as the inputed variable
                else:
                    if menu_choice == 4:
                        report_all() #Option 4 simply starts the report all function. Nothing else is needed
                    else:
                        if menu_choice == 5:  #Option 5 breaks the while loop of the menu. Ending the program
                            print("Exiting program. Thank you for your time")
                            break
                        else:
                            print("Invalid entry. Option not in list")#Same invalid option error as always
    else:
        print("Invalid entry. Please enter a number")#Same invalid entry error as all of them