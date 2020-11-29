# Instance & Class Variables in Python
class Rock:  # Conventionally we name a class with first character of its name in Upper Case
    pass
tushar = Rock()
satan = Rock()

tushar.name = "Tushar"
tushar.salary = 70000000
tushar.role = "Guitarist"

satan.name = "Lucifer"
satan.salary = 50000000
satan.role = "Violinist"

print(tushar.name, "&", satan.name)
# tushar.variable & satan.variable are the instance variables of respective objects and have nothing to do with class
# Defining class variables:-

class Rock:
    instruments_no = 1  # This is a class variable

tushar = Rock()
satan = Rock()
tushar.name = "Tushar"
tushar.salary = 70000000
tushar.role = "Guitarist"

satan.name = "Lucifer"
satan.salary = 50000000
satan.role = "Violinist"
print(Rock.instruments_no)
print(tushar.instruments_no)
print(satan.instruments_no)
# Above 3 print statements will gave same output(= 1) as  instruments_no is a class variable and is same for all objects
# We can change a class variable as:-
Rock.instruments_no = 2
print(Rock.instruments_no)  # It will print  the modified  value of the class variable
"""
But, we cannot change class variable using objects of that class:-
tushar.instruments_no = 2 & satan.instruments_no =2
will not change the class variable instead it will create instance variables "instrument_no" for  objects tushar and satan 
"""

# __dict__ returns a dictionary with variables and their values for class and its objects(check output)

print(Rock.__dict__)
print(tushar.__dict__)
print(satan.__dict__)

tushar.instruments_no = 2
satan.instruments_no = 2

print(Rock.__dict__)
print(tushar.__dict__)
print(satan.__dict__)

