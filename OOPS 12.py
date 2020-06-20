# Abstract Base Class & @abstractmethod In Python

"""
Abstract Base Class is used for creating a base class with an abstract method
Abstract method of a base class imposes all child classes of the base class to have the abstract method of base class in them
If abstract method is not present in the child classes,then interpreter will throw an error
"""

from abc import ABC , abstractmethod
# NOTE that older Python version(<=3.4) users have to type :- from abc import ABCMeta, abstractmethod

class Shape(ABC):# older version python users should pass argument "metaclass = ABCMeta" in place of "ABC"
    @abstractmethod
    def area(self): #Now all child classes of class Shape must have a method named area
        return 0

class Square(Shape):
    def __init__(self,len):
        self.length = len

    def area(self):
        return f"Area of the given Square is {self.length * self.length} units"


s = Square(2)
print(s.area())
# If we remove area method from class Square,then Square will show error due to it being a subclass of class Shape
# We cannot Create Objects of Abstract Base Classes.
