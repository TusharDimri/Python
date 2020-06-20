# Deleter, Setter & Property Decorators In Python

class Employee():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{self.fname}.{self.lname} @ email.com"

    def  explain(self):
        return f"Employee's full name is{self.fname} {self.lname}"

    @property
    def gmail(self):
        return f"{self.fname}.{self.lname} @ gmail.com"

t = Employee("Tushar", "Dimri")
s = Employee("Lucifer", "Morningstar")

print(t.email)
t.lname = "Mayer"
print(t.email) #Even after changing lname,email remained same because email was created during onject creation.

print(t.gmail)
"""
If  property decorator had not been used then we would have to call gmail as a method rather than as a instance variable i.e. 
print(t.gmail()) 
the ' () ' would have been there because gmail is a method
We apply ENCAPSULATION by doing so as user won't know whether gmail is an instance variable or method,so basically we are hiding
some working details from user.
"""


# Setter Decorator  & Deleter Decorator In Python

"""
TO understand @setter we will imagine a scenario where we can change first ane and last name of an object if we change its gmail
To achieve this we will use @setter 
"""

"""
We cannot delete an object's attribute using del.For example:-
del t.gmail will throw us an error ,so for the purpose of deleting an attribute deleter is used.
"""

class Employee():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{self.fname}.{self.lname}@email.com"

    def  explain(self):
        return f"Employee's full name is{self.fname} {self.lname}"

    @property
    def gmail(self):
        if self.fname == None or self.lname == None: # This is in case if we delete gmail & don't want 'None.None@gmail.com' as gmail
            return "Gmail is not set"

        return f"{self.fname}.{self.lname} @ gmail.com"

    @gmail.setter
    def gmail(self, str):#Gmail will be argumented here as a string
        print("Setting Now")
        name = str.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @gmail.deleter
    def gmail(self):
        self.fname = None
        self.lname = None


t = Employee("Tushar", "Dimri")
s = Employee("Lucifer", "Morningstar")


print(t.fname)
print(t.lname)
print("\n")

t.gmail= "Tus.Dim@gmail.com"
print(t.fname)
print(t.lname)
print(t.gmail)

del s.gmail
print(s.gmail)
