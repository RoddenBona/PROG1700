import textwrap
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
           'id':'W4132008'
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

"""
`dict.keys()`: Returns a list of all keys in the dictionary. 

`dict.values()`: Returns a list of all values in the dictionary. 

`dict.items()`: Returns a list of key-value pairs (tuples). 

`dict.get(key, default)`: Returns the value associated with the key, or a default value if the key doesn't 

"""

# Dictionary methods 

keys = student.keys() 

values = student.values() 

items = student.items() 

major = student.get('major', 'Undeclared') 

print(keys)

print(values)

print(items)

print(major)

#iterating through dictionaries
#You can loop through a dictionary to process keys and values

for key in student:
    #format print
    print(f'{key}:{student[key]}')
print('\n',)


for key in student:
    print(key,':',student[key])

#we could also use this
# Using a for loop with items() 

for key, value in student.items(): 
    print(f'{key}: {value}')





#irl example
# Creating a library catalog using dictionaries 
library_catalog = { 

    '978-0134863709': 'Python Crash Course', 

    '978-1491946008': 'Fluent Python', 

    '978-1449355739': 'Python Pocket Reference' 

} 

library_catalog['978-1449369415'] = 'Learning Python' 

del library_catalog['978-1491946008'] 

print("Library Catalog:") 

for isbn, title in library_catalog.items(): 

    print(f"ISBN: {isbn}, Title: {title}") 
 
#In this lesson, you've learned about Python dictionaries, how to create and manipulate them, 
# and some useful methods. Dictionaries are a powerful tool for organizing and accessing data in 
# Python. Practice working with dictionaries to become proficient in their use, as they are essential 
# for many real-world applications.  
