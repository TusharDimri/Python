# Do rewatch the video by codewithharry (video 65 from python tutorials for beginners & video has same name as this file)

class A:
    classvar1 = "I'm a Class Variable of Class A"
    def __init__(self):
        self.var1 = "I am inside class A's Constructor "
        self.classvar1 = "Instance Variable Of Class A"
        self.special = "I'm a special variable"

class B(A):
    classvar1 = "I'm a Class  Variable of Class B"
    def __init__(self):
        super().__init__() # Now instances of Class B can access all class variables of A that are not in B(like special)
        self.var1 = "I am inside class B's Constructor "
        self.classvar1 = "Instance Variable Of Class B"
        print("Called from __init__ of Class B :-",super().classvar1)


a = A()
b = B()
print(b.classvar1)
print(a.classvar1)
print(b.special)
