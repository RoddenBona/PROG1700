#This is to demonstrate inhieritance in OOP

#Create the general animal class
class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        pass


#Then at least 1-2 more classes for some animals
class Dog(Animal):
    def speak(self):
        return(f"{self.name} says Woof")
    
class Cat(Animal):
    def speak(self):
        return(f"{self.name} says Meow")
    

#Create objects of a dog and cat
dog = Dog("Kobe")
cat = Cat("Finn")


#Use methods
print(dog.name)
print(cat.name)
print(F"{dog.speak()} and {cat.speak()}")