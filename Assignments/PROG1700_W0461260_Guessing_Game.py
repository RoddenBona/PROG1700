"""
Author: Rodden Bona
Student ID: W0461260
Course: PROG1700
Respository: https://github.com/RoddenBona/PROG1700
Project: Python random number guessing game
Programming Language: Python 3
Version: 1.5
"""
#Random function for the radnom number
import random

#Asks for the user's name and proceeds to explain what the game is
name = input("Good day there. What is your name?: ")
print("Hello " + str(name) + ". Let's play a game!")
print("Guess which number I am thinking about!")
print("You only have 10 tries to figure it out!")
#Variable for both the amount of guesses taken
invalid_attempts = 0
#Random number variable will choose a number between 1 and 10
cpunumb = random.randrange(1,11)

#While you are at attempt 5 or fewer. The program will proceed to loop until you run out of guesses
while invalid_attempts <= 5:
    #User input to guess the number
    userchoice = input("Enter Number: ")
    # if the users choice is a simple digit. convert input to intiger and continue
    if userchoice.isdigit():
        userchoice = int(userchoice)
        #If the users guess is not 0 or a number above 10. Check for win condition
        if userchoice > 0 or userchoice <=10:
            #If guess is correct. Print correct and tell the user how many guesses they took
            if userchoice == cpunumb:
                print ("Correct! Congratulations " + str(name))
                #Incease the variable by one so if they get it first try, it doesn't say they did it in 0 guesses
                invalid_attempts = invalid_attempts + 1
                print("You guessed " + str(cpunumb) + " in " + str(invalid_attempts) + " attempts")
                break
            else:
                #If guess is too high. Increase attempts by 1 and tell user just that
                if userchoice > cpunumb:
                    print("Too high!")
                    invalid_attempts = invalid_attempts + 1
                else:
                    #If code is too low. Increase  attempts by 1 and tell user 
                    if userchoice < cpunumb:
                        print("Too low")
                        invalid_attempts = invalid_attempts + 1
        else:
            #If user inputs 0 or above 10. Print this as a warning and continue loop
            print("You can't use those numbers")
    else:
        # Error message if input was not a simple digit or invalid variable type
        print("You gotta enter a simple number!")
else:
    #Game over message if user doesn't guess the number in 5 attempts
    print("You're out of guesses. Too bad!") 

    #Once user has used up their 5 guesses. The while loop will no longer loop. Ending the program
