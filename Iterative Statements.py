list1  =[ ["Tushar",1], ["Lucifer",2],["Hitler",3]]

for name,grade in list1:
    print(name,"Grade IS:",grade )

dict1 = dict(list1)
print(dict1)
for name,grade in dict1.items():
    print(name,"Grade IS:",grade )

items = [1, "td", 32 , 21, "a"]
for item in items:
    if str(item).isnumeric():
        if int(item) > 6:
            print("Item:", item)

"""
Infinite Loops :-

i = 0
while i<1:
    print(i)
    
while(True):
    print("infinity")
"""

"""
i=0
while(i<11):
    print(i=" ")
    i=i+1
"""

"""
i=0 #use of break statement
while(True):
    print(i, end=" ")
    i=i+1
    if i==50:
        break   #program stops here 
"""

"""
i=0 #use of continue statement
while(True):
    if i<5:
        i=i+1
        continue
    print(i, end=" ")
    if i==50:
        break
    i=i+1
"""