# Map Function :-

# list=["0","2","69"]
# for i in range(len(list)):
#     list[i] = int(list[i])
# list[2] += 1
# print (list[2])

# Shortcut for above code using map function
list2 = ["69", "34", "45"]
obj = map(int, list2)  # Note that map function returns an object (check output)
print(obj)
list3 = list(map(int, list2))  # Type Casting the object returned by map function to a list
print(list3)
list3[0] = list3[0] + 1
print(list3[0])
print(list2[0])
# Above 2 print statement show that list2 and list 3 are different strings.
"""
NOTE:-
map executes int(list2) and then returns map object.
This map object is then type casted to list (list3)
"""


# Other uses of map function
def sq(a):
    return a*a
num = [1, 3, 2, 5, 6, 7, 9, 8]
square = list(map(sq, num))
print(square)
# Above code using lambda function
sq = lambda a: a*a
num = [1, 3, 2, 5, 6, 7, 9, 8]
square = list(map(sq, num))
print(square)

cube = list(map(lambda a: a*a*a, num))
print(cube)

def square(a):
    return a*a
def cube(a):
    return a*a*a
func = [square, cube]
for i in range(6):
    print(list(map(lambda x: x(i), func)), end=" ")  # x takes a function and return i th value of the function

print("\n")

# Filter Function:-

# This function creates a list for which the specified list elements return True

lt = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def greater_than_5(num):
    print(num > 5)
    return num > 5

great_than_5 = list(filter(greater_than_5, lt))
# Type casting is required like map function because filter returns an object
print(great_than_5)


# Reduce Function:-

# Reduce function returns a number which is reduced after the specified function is implemented on the specified list

from functools import reduce
lisht = [1, 2, 3, 4, 5]
num = 0
for i in lisht:
    num = num+i
print(num)

# Pythonic (better & easier) way of doing above task

lit = [1, 2, 3, 4, 5]
num = reduce(lambda x, y: x+y, lit)  # Sum of elements of lit is reduced
print(num)