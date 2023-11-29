""" 
Author: Rodden Bona
Student ID: W0461260
Course: PROG1700
Respository: https://github.com/RoddenBona/Assignments
Project: Create a simple algorithm using the flowchart and psuedocode
Programming Language: Python 3
Version 3.0
"""

#importing date and time and setting it to a variable
import datetime
date = datetime.datetime.now()

#This function will print the year of birth for someone born before today
def bef_calc():
    yob = (date.year-age)
    print("You were born in " + str(yob))

#This is the input program for someone born before today
def before():
    global age
    while True:
        age = int(input("Input your age as a simple number: "))
        if age <= 4: #Telling the user that it's npt likely they'd be using the program under 4 years old
            print("I do not belive you")
        if age > 4: #If the user is above 4. It will proceed to calcualte year of birth and end this wile loop
            bef_calc()
            break
        else:
            print("Invalid Entry") #Invalid entry prompt for users less than 4 or if an unintended value is entered

# This will calculate year of birth for one born after the current day
def af_calc():
    yob = (date.year - age) -1 #Likely born a yeat prior
    print("You were born in " + str(yob))

#A similar function as for the before function but is prompted if user is born after today
def after():
    global age
    while True:
        age = int(input("Input your age as a simple number: "))
        if age <= 4: #Same error messages will occur if user is under 5
            print("I do not belive you")
        if age > 4:
            af_calc()
            break # As well as the breaking of the loop to begin the year of birth calculation
        else:
            print("Invalid Entry")

# This function will as the user if their day of birth is before the current date or after the current date
def beoraf():
    opt = int(input("Was your brithday. (1)Before today? Or (2)After today?")) #User is prompted to either input 1 or 2 as their options
    while opt != 1 or opt != 2: #This while loop checks if the option entered is either option provided
        if opt == 1:            #If not then the while loop will repeat back to the input selection prompt
            before()
            break #Break and proceed to before calculation
        if opt == 2:
            after()
            break #Break and proceed to after calculation
        else:
            print("please enter a 1 or 2")

beoraf()
#After everything is defined and working. This will start up the input selection for if their date of birth
#is eitber before today or after today

"""The program is split up into multiple fucntions for both ease of troubleshooting on my end. As well as
having issues with putting the before or after function into the pre-existing year of birth calclator"""