#Import random functionality
import random

print("Lets play Rock, Paper, Sisscors!")
invalid_attempts = 3

#Program control
while invalid_attempts > 0:
    #local variable input
    userchoice = input("Press 1 for Rock, 2 for Paper3, and 3 for Sisscors:")
    #validate the input to make sure the program doesn't have an invalid input
    #Loop input if input in incorrect
    if userchoice.isdigit():
        #convert input to integer 
        userchoice = int(userchoice)
        #Checks if user int input is not beyond 3
        # if len(userchoice) == 1: also wokrs in this situation for inputs iver single digits but not for ints over 3
        if userchoice <= 3 and userchoice > 0:
            #computer plsyer choice
            cpuchoice = random.randrange(1,4)
            print("CPU chooses " + str(cpuchoice) +"!")
            #Win condition check
            if userchoice == cpuchoice:
                print("It's a tie")
            else:
                if userchoice == 1 and cpuchoice == 3 or userchoice == 2 and cpuchoice == 1 or userchoice == 3 and cpuchoice == 2:
                    print("You win!")
                else:
                    print("CPU wins!")
        #Resets back to input selection if input is beyond 3
        else:
            print("You can't do that! You have to chose one of the three!")
            invalid_attempts = invalid_attempts - 1
            print("You have " + str(invalid_attempts) + " attempts left")
    #If input is not a integer digit. bring back to selection
    else:
        print("Invalid Entry. You gotta enter a number")
        invalid_attempts = invalid_attempts - 1
        print("You have " + str(invalid_attempts) + " attempts left")
else:
    print("If you're not gonna play fair. Then we're done here")