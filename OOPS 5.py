# Static Methods In Python

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
        return cls(*string.split(","))  # *string returns an arg(checks args and qwargs)

    @staticmethod
    def print_str():
        # This method is class specific(the speciality of this method is that it takes neither cls or self as argumnet
        print("Welcome to Guitar Community ")

kurt = Fender("Kurt Cobain", "Singer & Guitarist", 200)
clap = Fender("Eric Clapton", "Singer & Guitarist", 300)
frus = Fender.from_str("John Frusciante,Guitarist,8")
kurt.print_str()
clap.print_str()
# Although static function print_str is called using different objects or class but it gives same output.
print(frus.print_str())  # None is in output because the method print_str returns nothing
"""
NOTE:- Static method can be called by using either the class name or any of its objects.
But in this case,argument passed is of more importance.
"""