# ABSTRACTION & ENCAPSUATION In Python(Also explained is text file "Abstraction & Encsapsulation")
"""
Breaking a task into small subtasks referred to as ABSTRACTION(these subtasks can then be integrated to complete that task).

In OOPS ENCAPSULATION is used to achieve ABSTRACTION.IN simple words ENCAPSULATION refers to the process of hiding implementation details
(Laptop for example) As the hindi saying goes,"aam khayen guthliya na gine" is the perfect way to to explain ENCAPSULATION i.e. rather than
going in depth in the working of an Abstracted task, we simply apply it for the purpose of its creation.
"""

# INHERITANCE In Python

# Example given below is an example of "single inheritance"(other types of inheritance are discussed in OOPS 7 & OOPS 8)
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
        return cls(*string.split(","))

    @classmethod
    def changeinstrno(cls,newno):
        cls.instruments_no = newno

    @staticmethod
    def print_str(str):
        print("Welcome to Guitar Community ",str)

kurt = Fender("Kurt Cobain", "Singer & Guitarist", 200)
clap = Fender("Eric Clapton", "Singer & Guitarist", 300)
frus = Fender.from_str("John Frusciante,Guitarist,8")

class Musician(Fender): # this is an example of single inheritance where Musician class inherited all the attributes of parent class Fender
    def __init__(self, argument_name, argument_role, argument_net,argument_band): #This constructor is specific to instances of class Musician
        self.name = argument_name
        self.role = argument_role
        self.net = argument_net
        self.band = argument_band

    def called(self): #this function is specific to class Musician only
        return f"Name is {self.name},role is {self.role}, band is {self.band} & net worth is {self.net} million$"

slash = Musician("Slash", "Guitarist", 100 , "Guns N Roses")
print(slash.called())
print(slash.band)
print(slash.print_str(slash.name)) # this shows how a class can use attributes of its base class
# NOTE that instanced of Base class cannot use attributes of inheritance class
# For Example:-
# print(frus.called()) will show error because frus is instance of base class
# Also, instances of inherent class can use attributes of its respective class and of base class.
