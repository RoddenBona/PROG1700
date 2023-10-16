import random

print("Guess which number I am thinking about")
print("You only have 10 tries to figure it out")
invalid_attempts = 0

cpunumb = random.randrange(1,11)

while invalid_attempts <= 5:
    userchoice = input("Enter Number: ")
    if userchoice.isdigit():
        userchoice = int(userchoice)
        if userchoice > 0:
            if userchoice == cpunumb:
                print ("Correct!")
                print("You guessed " + str(cpunumb) + " in" + str(invalid_attempts) + " attempts")
            else:
                if userchoice > cpunumb:
                    print("Too high!")
                    invalid_attempts = invalid_attempts + 1
                else:
                    if userchoice < cpunumb:
                        print("Too low")
                        invalid_attempts = invalid_attempts + 1
        else:
            print("You can't use zero")
    else:
        print("You gotta enter a number!")
else:
    print("You're out of guesses. Too bad!")
