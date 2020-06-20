"""
Diamond shape problem arises in most programming languages due to multiple inheritance(languages like C++ but not Java as Java don't
support multiple inheritance.But, easy syntax in python makes it easier for us to avoid diamond shape problem to some extent.
This is due to the confusion caused by this problem that we are advised to avoid multiple inheritance so as to avoid confusion.
A simple example of such confusion is shown below.

"""



class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    var = 1
    def met(self):
        print("This is a method from class B")


class C(A):
    var = 2
    def met(self):
        print("This is a method from class C")


class D(B, C):
    pass

class E(C, B):
    pass

a = A()
b = B()
c = C()
d = D()
e = E()

print(d.var)
"""
 Confusion may arise due to multiple inheritance regarding which class variable to print(i.e. var of class B or var of class D) 
 But, python's syntax solves this problem and print class variable of class B first as it is called first during multiple inheritan
 -ce(check line 27:- class D(B, C)  ) as an argument

"""

print(e.met())
"""
Similar to previous problem this problem is solved by easy python syntax in 30 ( class D(C, B) ) where C is passed as an argument 
first during inheritance so method of class C is prioritised over that of class B and printed   

"""