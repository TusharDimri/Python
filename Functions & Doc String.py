a = 1
b = 32

c = sum([a, b]) # sum function takes only an iterable as an argument.
# sum is a built in function
print(c)


def func(a,b):
    """This Function calculates the sun of two given numbers"""
    s = a+b
    print(s)
    return s

sum=func(2,5)
print (sum)

print( func.__doc__ )
# Above statement prints the doc string of a function,remember to add 2 underscores before and after doc keyword
# If function has no doc string then it prints None