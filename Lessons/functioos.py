#functions are code that exist in their own little bubble

def func():
    a = 2
    b = 3
    print("Hello")
    print(a + b)

func()

#functions can take inputs

def greet(username):
    print(f"Hello {username} How are you today")

greet("John")

#They can be used to return results

def calc(a,b):
    combo = a + b
    print(combo)

calc(1,8)

#default values

def greet_message(username, message = "Good morning"):
    print(f"{message} {username}")

greet_message("Joeseph")

#best practice is to keeep as much of your function as self containted as you possibly while still doing it's purpose

