"""
Year of Birth Calculator
By Rodden Bona
Last edited Sept 27 2023
GitHub: 
"""
#importing current date and setting it to a variable
import datetime
date = datetime.datetime.now()

print("Hello I can calculate the year of your birth based on your age. Let me show you")

#This will be the input function for the user to input thier age
def user_input():
    global age
    while True:
        age = (input("Please enter your age: ")) # User inputs their age here
        if age.isdigit(): #Checks if input is digit
            age = int(age) 
            age_calc() # Then moves to the function for year of birth calculating
            break
        else:
            print("Please input a simple number as your age. I cannot use letters or decimals")
            #Error message for unintended variables

#This function will take the inputed age of the user and subtract it from the current year
def age_calc():
    if age <= 4:    #Checking if the age inputed if less than 4. I doub a 4 year old could understand this
        print("I don't believe that you are that young")
        user_input() #Boots user back to the input function
    else: 
        yob = (date.year) - (age)
        print("You were born in the year: " + str(yob))

user_input() #Fires up the input program after defining everything before it