# Object Introspection In Python
# The process of obtaining information about an object(its type, its class, etc.) is called as object introspection

class Employee():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{self.fname}.{self.lname}@email.com"

    def  explain(self):
        return f"Employee's full name is{self.fname} {self.lname}"

    @property
    def gmail(self):
        return f"{self.fname}.{self.lname}@gmail.com"

t = Employee("Tushar", "Dimri")

#Different ways to do object introspection are:-

# 1. Object introspection using type function which tells us the class of an object.

print(type(t))
print(type("XYZ"))  # output of this statement proves that str is a class.Similarly,int is also a class.
print(type(4), "\n")

# We can also find ID of an object using Function id.Also,different objects have different id.
a = 1
b = 1
print(id(a))
print(id(b), "\n")
# a & b have the same id because they point to the same memory location as they have the same value

c=1
d=2
print(id(c))
print(id(d), "\n")
# Output shows that c & d have different id.This is because they hold different values.

# 2. Object introspection using function 'dir'.

print("dir(object) returns:-")
print(dir(t), "\n")
# left click 'dir' above with ctrl key to know what this function returns about an object.

# 3. Object introspection using inspect module

import inspect
print("inspect.getmembers(object) returns:-")
print(inspect.getmembers(t))