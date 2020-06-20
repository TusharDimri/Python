class Blues:
    instrument_no = 1
    def details(self):  # this function is called a meathod because of being in a class(self refers to the object of the class)
         return f"Name is {self.name},role is {self.role} & net worth is {self.net} million$"
jimmy = Blues()
john = Blues()

jimmy.name = "Jimmy Henderix"
jimmy.role = "Guitarist"
jimmy.net = 50

john.name = "John Mayer"
john.role = "Guitarist"
john.net = 40

#calling class ,meathod using object of the class (self is passed as object that is called)

print(jimmy.details())
print(john.details())
"""
NOTE:-self(name of parameter) is just a convention for a method but if we are calling a method using an object then
there should be a variable in the method's parameter (self in this case) to take object as an argument
"""
# all tasks covered up till now prove the usefulness of OOPS on the basis of code reusability(TRY) and in saving a lot of our time

# CONSTRUCTORS
# Giving arguments to a class(will be clear after checking an example)
class Fender:
    def __init__(self, argument_name , argument_role, argument_net):# this is a constructor
        self.name = argument_name
        self.role = argument_role
        self.net = argument_net
    # here self is used for object to be taken as an argument
    def help(self):
         return f"Name is {self.name},role is {self.role} & net worth is {self.net} million$"

kurt = Fender("Kurt Cobain", "Singer & Guitarist", 200)
clap = Fender("Eric Clapton", "Singer & Guitarist", 300)
print(kurt.help())
print(clap.help())
# Above example shoes how a constructor make object creation easier and time saving and very easy to declare instance variables
# Note that a contructor's name is always init and always take self(for object) as an argument with  other arguments