import math
import datetime
import random

"""
Author: Rodden Bona
StudentID: w0461260
Course: PROG1700
Exercise: Python Exercise Reviewing Python Common Functions
Module: All Modules
Last Updated By: Boudreau,Davis
Language: Python 3
Last Update: November 2023
"""

#Create two string variables, str1 and str2, and concatenate them into a third variable result_str.
str1 = "forty "
str2 = "bucks"
str_con = str1 + " " + str2
print(str_con)

#Given a string sentence, extract and print the first five characters.
sub = "Hello world"
print(sub[0:5])

#Create a string that includes variables. Use string formatting to insert values into the string.
name = "Rodden"
form = "Sunday"
print(f"Hello. My name is {name}. and today is {form}")

#Using a for loop, print the numbers from 1 to 10.
results = ""
for i in range(1,11,1):
    results += str(i) + " "
print(results)

#Write a function to calculate the factorial of a number using a while loop.
def factorial(n):
    result = 2
    while n > 0:
        result *= n
        n = n - 1
    return result
print(factorial(4))

#Create two sets, set1 and set2, and find and print their intersection.
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1)
print(set2)

#Here's the more manual way of finding the intersection
for i1 in set1:
    for i2 in set2:
        if i1 == i2:
            print(i1)

#Here a version of it using & in the algorithim
inter_set = set1 & set2
print(inter_set)

#This also works as well and of course, it's the most simplest way of it
inter = set1.intersection(set2)
print(inter)

#and here's the dfference between the 2 sets
diff = set1 - set2
print(diff)

#Create a list of numbers. Perform the following operations and print the result:
#Average of all elements.
#Maximum and minimum values.

l = [6,7,8,9,10]

sum_of =  sum(l)
num_of = len(l)
avg = sum_of/num_of
print(avg)

#or
print(sum(l)/len(l))

maxi = max(l)
mini = min(l)
print(maxi)
print(mini)

#or

print(max(l))
print(min(l))

#Generate a list of squares of numbers from 1 to 10 using list comprehension.

squares1 = [x**2 for x in range(1,11)]
print(squares1)

#OR

squares2 = []
for x in range(1,11):
    squares2 = [x**2]
print(squares2)

#Create a tuple with three values. Unpack the tuple into three variables and print them.
tup = ("Yugi", "Kaiba", "Marik")

a, b, c = tup
print(a)
print(b)
print(c)

#Create a dictionary representing a person with keys like 'name', 'age', and 'city'. Print each key-value pair.
dictionary = {"Name":"Rodden",
              "Age":20,
              "City":"Port Hawksbury"}

for item,value in dictionary.items():
    print(f"{item}:{value}")

#Create a nested dictionary representing information about students and their grades. Print the average grade for each student.
student_record = {"Kris":{"Math":70, "English":75},
            "Noelle":{"Math":90, "English":85},
            "Susie":{"Math":60, "English":68}
            }

for student,grade in student_record.items():
    avg_grade = sum(grade.values())/len(grade)
    print(f"Student average for {student} is {avg_grade}")


#Write a function that takes two arguments and returns their sum.
def int_sum(int1,int2):
    print(int1+int2)

def int_input():
    int1 = input("Enter the first number: ")
    if int1.isdigit():
        int1 = int(int1)
        int2 = input("Enter the second number: ")
        if int2.isdigit():
            int2 = int(int2)
            int_sum(int1,int2)

int_input()

#Modify the previous function to have default values for the arguments.
int_sum(68,12)
#I may have done this in reverse order on accident

#Reading/Writing External Files:
#File Reading:
#Read a text file named 'sample.txt' and print its contents line by line.
t = open("sample.txt", "r")
print(t.read())

#File Writing:
#Write a list of strings to a new text file named 'output.txt'.

test = input("Enter something to add to an output text file: ")

w = open("output.txt", "a")
w.write(str(test))
w.close()

#Now to open it and read it again
w = open("output.txt", "r")
print(w.read())