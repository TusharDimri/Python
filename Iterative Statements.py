list=[ ["Tushar",1], ["Lucifer",2],["Hitler",3]]
for name,grade in list:
    print(name,"Grade IS:",grade )
dict1 = dict(list)
for name,grade in dict1.items():
    print(name,"Grade IS:",grade )

"""while i<1:
    print(i)"""  #Infinite Loop

"""i=0
while(i<11):
    print(i=" ")
    i=i+1"""

"""i=0 #use of break statement
while(True):
    print(i, end=" ")
    i=i+1
    if i==50:
        break """   #program stops here

"""i=0 #use of continue statement
while(True):
    if i<5:
        i=i+1
        continue
    print(i, end=" ")
    if i==50:
        break
    i=i+1"""