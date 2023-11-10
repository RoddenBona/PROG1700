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

#5. Promp to type in a student's name. display their score

while True:
    option = input("Select a student")
    if option in student_score:
        print('test')

#6. prompt the user of they wish to update their score

#7.Remove a student and prompt to add a new entry

