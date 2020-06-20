#Dictionary is nothing but a key value pair
d1 ={}
print(type(d1))
d1={"Tushar":"Guitar","Winsmoke":"Drums","Lucifer":"Vocals","Medusa":"Bass"}
print(d1)
print(d1["Tushar"])
d2={"Tushar":"Guitar","Winsmoke":"Drums","Lucifer":"Vocals","Medusa":"Bass","Kurdt":{"M":"violin","N":"Fiddle"}}#Nested Dictionary
print(d2)
d2["Satan"]="Piano"
print(d2)
del d2["Satan"]
print(d2)
d3=d2.copy()
print(d3)
d1=d3
del d1["Tushar"]
print(d1,d3)# Both Are Affected
print(d2.get("Kurdt"))#to get value of given key
d1={"Guitar":"An Instrument","Rock":"Genre","Mutable":"Changeable","Immutable":"Not-Changeable"}
import os
os.rename("Using else with for loops in Pyhton.py","Using else with for loops in Python.py")

choice = input("Enter a word")
print(d1.get(choice))
