# Object overloading and Special methods in Python
# Methods that begin & end with __ are called special/dunder methods.For Example:- __init__ is dunder init.
# Dunder methods are mostly used for operator overriding.

class Fender:
    instruments_no = 1
    _user = "Any Guitarist"
    __gtype = "Strat"

    def __init__(self, argument_name, argument_role, argument_net):
        self.name = argument_name
        self.role = argument_role
        self.net = argument_net

    def help(self):
        return f"Name is {self.name},role is {self.role} & net worth is {self.net} million$"

    def __add__(self, other):
        return self.net + other.net

kurt = Fender("Kurt Cobain", "Singer & Guitarist", 200)
john = Fender("John Mayer", "Singer & Guitarist", 40)
print(kurt + john)

# NOTE that if dunder method __add__ was not present the print statement would have shown error
# Do search online for more Dunder methods(Mapping Operator To Function)

# Do rewatch video to know about __rpr__ & __str__ methods





