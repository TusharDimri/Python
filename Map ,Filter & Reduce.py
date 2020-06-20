# Map Function
# list=["0","2","69"]
# for i in range(len(list)):
#     list[i] = int(list[i])
#
# list[2] += 1
# print (list[2])

# Shortcut for above code using map function
list2=["69","34","45"]
obj= map(int, list2) #it is to note that map function returns an object (check output)
print(obj)
list3 = list(map(int, list2)) #type casting  the object returned by map function to a list
print(list3)
list3[0] = list3[0] + 1
print(list3[0])


#other uses of map function
def sq(a):
    return a*a
num=[1, 3, 2, 5, 6, 7, 9, 8]
square = list(map(sq, num))
print(square)
#above code using lambda function
sq = lambda a:a*a
num=[1, 3, 2, 5, 6, 7, 9, 8]
square = list(map(sq, num))
print(square)


def square(a):
    return a*a
def cube(a):
    return a*a*a
func = [square, cube]
for i in range(6):
    print(list(map(lambda x:x(i), func)), end=" ") # x takes a function and return i th value of the function

# Filter Function
lt=[1,2,3,4,5,6,7,8,9]
def greater_than_5(num):
    return num>5
great_than_5= list(filter(greater_than_5, lt)) #type casting is required like map function because filter returns an object
print((great_than_5))
# Reduce Function

from functools import  reduce
lisht=[1,2,3,4,5]
num=0
for i in lisht:
    num = num+i
print(num)

#pythonic(better & easier) way of doing above task

lit=[1,2,3,4,5]
num = reduce(lambda x,y:x+y,lit)#sum of elemets of lit is reduced
print(num)