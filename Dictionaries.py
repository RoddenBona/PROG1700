# Python Dictionaries

"""
Objective: In this lesson, we will dive into Python dictionaries, a versatile and fundamental data 
structure. By the end of this lesson, you should be able to understand what dictionaries are, create
and manipulate dictionaries, and apply them to real-world problems. 
"""

# how ot make a dictionary
student = {'name':'Alice',
           'age':20,
           'major':'Computer Science',
           }

#printing class + what is in the dictionary
print(type(student))
print(student)

#cool. now how do you access that information in peices?

#You can display or even modfy by puttinh the specific section in square brackets aafter the dictionary


#print just the name
print(student['name'])

#change the age and then print the modified value
student['age'] = 21
print(student['age'])

#unlike lists, Dictionaries can be altered (or at least altered without a roundabout solution)

