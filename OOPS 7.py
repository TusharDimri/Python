# Multiple Inheritance In Python

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

class Guitarist:
    instruments_no = 2
    def __init__(self,arname,arbrand):
        self.name = arname
        self.brand = arbrand

    def brand_details(self):
        return f"Name is {self.name} & Guitar Brand used  is {self.band} "

    @staticmethod
    def music(str):
        return f"Welcome Mr.{str}"

slash = Guitarist("Slash","Gibson Les Paul")

class Band(Fender, Guitarist): #This is a multiple inheritance(note that Fender is first argument and Guitarist is second)
    noofband = 1

jimmi = Band("Jimmi Hendrix", "Singer & Guitarist", 50)
# NOTE that as class Fender is mentioned first we have to use its constructor rather than that of class Guitarist
# This shows that the order in which class is called in a multiple inheritnce(see line 41) decides which class will be prioritized
# Also, we can't use methods which have instances specific to the second class inherited from(Guitarist in this case)
# the code:- print(jimmi.brand_details) will show error as explained

print(jimmi.help())
print(jimmi.instruments_no)# See that 1 will be printed rather than 2 because class Fender is prioritised over class Guitarist(dur to it being the first argument during inheritance)
print(jimmi.music("Hendrix"))

