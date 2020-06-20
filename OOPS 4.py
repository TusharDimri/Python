#Class Methods
class Fender:
    instruments_no = 1
    def __init__(self, argument_name , argument_role, argument_net):
        self.name = argument_name
        self.role = argument_role
        self.net = argument_net
    def help(self):
         return f"Name is {self.name},role is {self.role} & net worth is {self.net} million$"
    @classmethod # this is a Decorator
    def changeinstrno(cls,newno): # the purpose of this class method is to change value of class variable but it can be used for many other tasks
        cls.instruments_no = newno #the argument cls takes class as an argument (like self,whuch takes an object)

kurt = Fender("Kurt Cobain", "Singer & Guitarist", 200)
clap = Fender("Eric Clapton", "Singer & Guitarist", 300)
print(kurt.instruments_no)
kurt.changeinstrno(2)
print(kurt.instruments_no) # the thing to note here is that we can change a class variable using an object with the help of a class method

# Class Methods as alternative Constructors:-

class Fender:
    instruments_no = 1

    def __init__(self, argument_name, argument_role, argument_net):
        self.name = argument_name
        self.role = argument_role
        self.net = argument_net

    def help(self):
        return f"Name is {self.name},role is {self.role} & net worth is {self.net} million$"

    @classmethod
    def from_str(cls,string):
        # fruscinte = string.split(",")
        # return cls(fruscinte[0],(fruscinte[1]),(fruscinte[2])) [this returns te line:- Fender(frusciante[0], frusciante[1], frusciante[2]) ]
        # shortcut for above 2 lines of code
        return cls(*string.split(",")) # *string returns an arg(checks args and qwargs)

kurt = Fender("Kurt Cobain", "Singer & Guitarist", 200)
clap = Fender("Eric Clapton", "Singer & Guitarist", 300)
frus = Fender.from_str("John Frusciante,Guitarist,8")
"""
previous three lines of code create three different instances(kurt, clap and frus).Respectively,first two instances are 
created using method __init__ but the instance "frus" is created using classsmethod from "_str" 
"""
print(Fender.help(frus))


"""
NOTE:-
1. Normal methods in Python OOPS like 'help' and '__init__' method are methods which have self(instance of the class) as
the default argument. They are mostly used in cases where we need to modify or use the objects of the class 

2. Class methods in Python  OOPS like from_str are methods which use cls(class) as the default argument.They are used when
we directly want to use our class inside the class. GThey can be used as alternative constructors where they are named
conventionally as 'from_---' where '---' is the format from which they are parsed.

3. Static methods in Python OOPS like print_str (OOPS 5) are methods which take neither self(instances of class) and cls
(class itself) as an argument but are logically related to the class

Now it is up to us to use these 3 different methods of class when needed and appropriately. 
"""