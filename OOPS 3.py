class Blues:
    instrument_no = 1
    def details(self):  # This function is called a method because of being in a class(self refers to the object of the class)
         return f"Name is {self.name},role is {self.role} & net worth is {self.net} million $"
jimmy = Blues()
john = Blues()

jimmy.name = "Jimmy Hendrix"
jimmy.role = "Guitarist"
jimmy.net = 50

john.name = "John Mayer"
john.role = "Guitarist"
john.net = 40

# Calling Class Method using object of the class (self is passed as object that is called)

print(jimmy.details())
print(john.details())
"""
NOTE:-self(name of parameter) is just a convention for a method by default but if we are calling a method using an object
then there should be a variable in the method's parameter (i.e. other variable in place of self) to take object as an 
argument
"""
# All tasks covered up till now prove the usefulness of OOPS on the basis of code reusability.(TRY) and
# in saving a lot of our time

# CONSTRUCTORS
# Giving arguments to a class(will be clear after checking an example)
class Fender:
    def __init__(self, argument_name, argument_role, argument_net):  # This is a Constructor
        self.name = argument_name
        self.role = argument_role
        self.net = argument_net
    # Here self is used for object that is  taken as an argument.(For example:- in guitar.Fender(), self is fender)
    def help(self):
         return f"Name is {self.name},role is {self.role} & net worth is {self.net} million$"

kurt = Fender("Kurt Cobain", "Singer & Guitarist", 200)
clap = Fender("Eric Clapton", "Singer & Guitarist", 300)
print(kurt.help())
print(clap.help())
# Above example shows how a constructor make object creation easier and time saving and very easy to declare instance variables
# Note that a contructor's name is always init and always take self(for object) as an argument with other arguments