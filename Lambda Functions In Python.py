# Lambda or Anonymous Functions in Python
"""
def add(a,b):
    return a+b
this function calculates sum of two numbers as arguments
this function's shortcut form is
"""
a=int(input("Enter A Number"))
b=int(input("Enter A Number"))
sum= lambda a,b: a+b #this is a lambda function(a function sum is created which take two arguments (a & b) and return a+b
print("Sum =",sum(a,b))

a=[[1,14],[8,12],[0,5]] #this is a list of lists i.e. a list inside a list
def a_1stindex(a):
    return a[1]
a.sort(key=a_1stindex)
print("List of list sorted in order of its first element is",a)

# Above code using lambda function is
a=[[1,14],[8,12],[0,5]]
a.sort(key=lambda n:n[0]) # Refer first lambda function to understand working of lambda functions
print("List of list sorted in order of its first element is",a)




# Now we will study sort function(an inbuilt python function)
l = [13,2,8,101,32,11,75,23,69]
l.sort()
print(l)

# To print list inn descending order (using reverse argument of sort method)
l1 = [13,2,8,101,32,11,75,23,69]
l.sort(reverse=True)
print(l1)

# sort() has another parameter called key which takes a function and sorts the values that the function returns
# For example:-
sl = ['aaa','bb','cccc','dd']
sl.sort(key=len)
# In the above code len is passed as a function so the list will be sorted on the basic of lenght rather than ASCII values
print(sl)




