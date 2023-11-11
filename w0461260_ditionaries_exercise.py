"""
Author: Rodden Bona
Student ID: W0461260
Course: PROG1700
Respository: https://github.com/RoddenBona/PROG1700
Project: 
Programming language: Python 3
Version
"""

#Create a script that how to work with dictionaries using several various operations 
#using at least 5 student names

#1 and 2. Create a table named student_score and add some names with their scores
student_score = {
    "Kris":70,
    "Bobby":90,
    "Noelle":95,
    "Ralph": 80,
    "Susie":50
}

#3.Print the student names
for key, value in student_score.items(): 
    print(f'{key}: {value}')

#4.Print the average scores

#create a sum of the values in the dictionary
sum_scores = sum(student_score.values())
print(sum_scores)

#then a value for how many key items there are (in this context. how many students)
number_students = len(student_score)
print(number_students)

#Now average them out
average = sum_scores/number_students
print(average)

highest = max(student_score.values())
print(highest)

#5. Promp to type in a student's name. display their score
#6. prompt the user of they wish to update their score
#7.Remove a student and prompt to add a new entry
#Calculate an d print the highest score
while True:
    choice = input("""(1)Select an existing student
    (2)Add a new student
    (3)Print all current scores
    (4)Exit
    Enter option here: """)
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            option = input("Enter a student name: ")
            option = str(option)
            if option in student_score:
                print("You have selected " + option + " and their score is: " )
                print(student_score[str(option)])
                print()
                deletion = input("""Would you like to:
                (1)Update score
                (2)Delete Entry
                (3)Exit
                Enter option here""")
                if deletion.isdigit():
                    deletion = int(deletion)
                    if deletion == 1:
                        updated = input("Enter updated score: ")
                        if updated.isdigit():
                            updated = int(updated)
                            student_score[str(option)] = updated
                    else:
                        if deletion == 2:
                            del student_score[str(option)]
                        else:
                            if deletion == 3:
                                print("exit")
                            else:
                                print("Invalid entry")
                else:
                    print("Invalid entry")
            else:
                print("Student not found please try again")
        else:
            if choice == 2:
                addition = input("Enter a new student name: ")
                addition = str(addition)
                new_score = input("Enter a score for the student: ")
                if new_score.isdigit():
                    new_score = int(new_score)
                    student_score[str(addition)] = new_score
                    print("Student has been added")
                else:
                    print("Invalid entry")
            else:
                if choice == 3:
                    for key, value in student_score.items(): 
                        print(f'{key}: {value}')
                        print("Average: " + str(average))
                        print("The highest score in the class is " + str(highest))
                else:
                    if choice == 4:
                        break
                    else:
                        print("invalid entry")
    else:
        print("invalid entry")

