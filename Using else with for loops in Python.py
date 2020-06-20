list = ["guitar", "violin", "mandolin", "ukelele"]
for ins in list:
    print(ins)
else:
    print("This for loop ended properly")

"""
NOTE that else will work after for loop will execute only if for loop ends normally i.e. without any break statements
One application of else with for loop is during linear search    
"""

n = input("Enter the name of the instrument to be searched")
n = n.lower()
list = ["guitar", "violin", "mandolin", "ukelele"]
for i in list:
    if i == n:
        print("Instrument Available")
        break
else:
    print("Instrument not available")
# You can see that else part is ignored when loop breaks i.e. when search is successful.