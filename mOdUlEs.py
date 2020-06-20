# import matplotlib ,this statement impots a module and its functions in your program(press ctrl and click on module to open its code and its doc string)
import random

random_integer=random.randint(1,4)#this generates a random integer 1<=random no.<=4
print(random_integer)

rand=random.random()#this generates a random floating point no. between 0 & 1
print(rand)

rand=random.random() * 100 #this generates a random floating point no. between 0 & 100
print(rand)

l=["Rock","Blues","Jazz","Country","Disco"]
choice=random.choice(l)
print(choice)

