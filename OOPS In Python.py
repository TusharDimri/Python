# Classes - Templates(pre made format ,say an official letter)
#Object - Instance of the Class (say,the letter written with help of a template)
# OOPS is based on the concept of D.R.Y - do not repeat yourself
#OOPS is applied to save time and effort,to resrict the access of a function
#Now here's my first OOPS code in python
class student:  #this class(for now) has no template
    pass
harry = student() # object\instance of class student
larry = student() #  another object\instance of class student
print(harry,larry) # output will show that both are different objects of class student(check output)
# instance variables of an object
harry.name = 'Harry' # instance variable of object harry of class student(don't cofunse keyword class with standard in school)
harry.standard  = 12 # another instance variable of object harry of class student
harry.section = 'A' #  another instance variable of object harry of class student
print(harry,larry)
print(harry.name," of ",harry.standard,harry.section)
larry.name = "Larry"
print(larry.name)
# But print(larry.std) will show error as we haven't yet declared such instance variable for object larry
# instance variable can contain lists,dictionary,integers, etc like any other variables
larry.subject = ["English", "Mathematics", "Computer"]
harry.gang = {1:"Tushar", 2:"Tanmay"}
print("List of Larry\'s Subjects:-",larry.subject)
print ("Members Of Harry\'s Gang",harry.gang)

