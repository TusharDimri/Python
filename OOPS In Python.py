# Classes - Templates(pre made format ,say an official letter)
# Object - Instance of the Class (say,the letter written with help of a template)
# OOPS is based on the concept of D.R.Y - Do not Repeat Yourself
# OOPS is a programming paradigm applied to save time and effort,to restrict the access of a function
# Now here's my first OOPS code in python
class Student:  # This class(for now) has no template
    # Conventionally, class name always start with a Capital Letter
    pass
harry = Student()  # object\instance of class Student
larry = Student()  #  Another object\instance of class Student
print(harry, larry)
# Output will show that both are different objects of class student(check output)
# Instance variables of an object:-
harry.name = 'Harry'
# Instance variable of object harry of class student(don't confuse keyword class with standard in school)
harry.standard = 12  # Another instance variable of object harry of class student
harry.section = 'A'  # Another instance variable of object harry of class student
print(harry, larry)
print(harry.name, " of ", harry.standard, harry.section)
larry.name = "Larry"
print(larry.name)
# But print(larry.std) will show error as we haven't yet declared such instance variable for object larry
# instance variable can contain lists,dictionary,integers, etc like any other variables
larry.subject = ["English", "Mathematics", "Computer"]
harry.gang = {1: "Tushar", 2: "Tanmay"}
print("List of Larry\'s Subjects:-", larry.subject)
print("Members Of Harry\'s Gang", harry.gang)
