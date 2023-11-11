"""
Author: Rodden Bona
Student ID: W0461260
Course: PROG1700
Respository: https://github.com/RoddenBona/PROG1700
Project: Dictionary Excercies
Programming language: Python 3
Version 2
"""

#Create a script that how to work with dictionaries using several various operations 
#using at least 5 student names

#1. and 2. Create a table named student_score and add some names with their scores
student_score = {
    "Kris":70,
    "Bobby":90,
    "Noelle":95,
    "Ralph": 80,
    "Susie":50
}

#create a sum of the values in the dictionary
sum_scores = sum(student_score.values())
#then a value for how many key items there are (in this context. how many students)
number_students = len(student_score)
#Now average them out
average = sum_scores/number_students
#Grab the highest value
highest = max(student_score.values())


#Since the last few exerices required user inputs. I decided to just combine just about everything
#into one big program. Where you can just access the student scores, edit scores, delete or add entries
#Just about the whole works of the whole assignment is down below in one big program

#3.Print all the student names and their scores
#4.Print the average scores
#5.Prompt to type in a student's name. display their score
#6.Prompt the user of they wish to update their score
#7.Remove a student and prompt to add a new entry
#8.Calculate and print the highest score in the dictionary

#Everything will be contained in a while loop. Bringing you back to the first select screen upon completing
#One of the options
while True:
    #User input to select whether to mess with existing entries, add a new one, print all current entries
    #or exit the program and break the while loop
    choice = input("""Please select an option
    (1)View an existing student
    (2)Add a new student
    (3)Print all current scores
    (4)Exit
    Enter option here: """)
    #Turn users choice into intiger to determine which option to go to and execute
    if choice.isdigit():
        choice = int(choice)
        #Excercise 5 is the view a pre-existing entry
        if choice == 1:
            #Search for exing entries in the dictionary and convert input into a string
            option = input("Enter a student name: ")
            option = str(option)
            #Search the dictionary to see if the inputed student exist within it
            if option in student_score:
                #print conformation and student's current score
                print("You have selected " + option + " and their score is: " )
                print(student_score[str(option)])
                #New input for updating the score deleting it, or exiting back to main menu
                deletion = input("""Would you like to:
                (1)Update score
                (2)Delete Entry
                (3)Exit
                Enter option here: """)
                #Convert option to int
                if deletion.isdigit():
                    deletion = int(deletion)
                    #option 1 and exercise 6. update the score
                    if deletion == 1:
                        updated = input("Enter updated score: ")
                        #Convert score to int and update student's score to input
                        if updated.isdigit():
                            updated = int(updated)
                            student_score[str(option)] = updated
                            print("Score has been updated")
                            print('\n',)
                    #option 2. deletion
                    else:
                        if deletion == 2:
                            #simply remove student entry from dictionary and return to main menu
                            del student_score[str(option)]
                            print("Student entry has been deleted")
                            print('\n',)
                        #option 3 and exercise 7(part one) just exits back to main menu
                        else:
                            if deletion == 3:
                                print("exit")
                                print('\n',)
                            else: # error message if choice is 4 or higher
                                print("Invalid entry")
                else: #error message if choice is not an int
                    print("Invalid entry")
            else: #Error if input does not match with an existing student
                print("Student not found please try again")
        #Excercise 7(part two) Adding a new entry to the dictionary
        else:
            if choice == 2:
                #Prompt user to input name for the new entry
                addition = input("Enter a new student name: ")
                addition = str(addition)
                #followed by their score for them
                new_score = input("Enter a score for the student: ")
                #check if entered score is an int
                if new_score.isdigit():
                    #convert to int if correct
                    new_score = int(new_score)
                    #Add the new student entry to the dictionary and boot back to main menu
                    student_score[str(addition)] = new_score
                    print("Student has been added")
                    print('\n',)
                #error if new score is not int
                else:
                    print("Invalid entry")
            #Excerise 3, 4 and 8 Viewing all current students and their scores with the average and highest score
            else:
                if choice == 3:
                    #Using f strings and for loops. This will print all students with their scores in a neat fashion
                    for key, value in student_score.items(): 
                        print(f'{key}: {value}')
                     #followed by the class average
                    print("Average: " + str(average))
                    #and what the highest score in the dictionary is
                    print("The highest score in the class is " + str(highest))
                #The final option of the main menu is just to break the loop. ending the program
                    print('\n',)
                else:
                    if choice == 4:
                        break
                    #error if inputed option is 5 or higher
                    else:
                        print("invalid entry")
    #error message for options that aren't int
    else:
        print("invalid entry")