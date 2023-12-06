#This is wht allows us to import other funccction into our own code
#When we import things like random and datetime. Those are just other python files
#That were made y other people being inported for us to just inject into our code


#As a simple example. we will define a greeting function to just say hello to us when something is inputed into "name"
def greeting(name):
    print(f"Hello there {name}")

#Now that the function is defined. We can import it into another one of our files
#Check the second test_module file for that in use

#You can also use this to store variables inside it aswell
#Meaning you can just grab variables from outside the main python file you are currenlty working on

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

#If you wanted to just import one thing from a file use the following import string
#       from mymodule import person1