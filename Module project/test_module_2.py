#Here in this file. We will import the first test_module into this one for use to use the
#greeting function that we defined in there
import test_module

#So now we just call on the file. Specifying which function of the file to use
#and inputing something into the "name" variable of the greeting function
test_module.greeting("Rodden")

name = "Jonah"
test_module.greeting(name)

from test_module import person1

print(person1["age"])