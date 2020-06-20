#ENUMERATE Functions(a mna is ordered to buy below list or die but later order is changed to buy only odd things ordered)
l1 = ["Bhindi", "Aloo", "Chopsticks", "Chowmein"]
i=1
for item in l1:
    if i%2 != 0:
        print(item)
    i+=1

#shortcut for above code

for index,item in enumerate(l1):
    if index % 2 == 0:
        print(item)