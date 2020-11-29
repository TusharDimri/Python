# import matplotlib ,this statement imports a module and its functions in your program(press ctrl and click on module to open its code and its doc string)
import random

random_integer = random.randint(1, 4) # This generates a random integer 1 <= random no. <= 4
print(random_integer)

rand = random.random() # This generates a random floating point no. between 0 & 1
print(rand)

rand = random.random() * 100 # This generates a random floating point no. between 0 & 100
print(rand)

l = ["Rock", "Blues", "Jazz", "Country", "Metal"]
choice = random.choice(l)
print(choice)

