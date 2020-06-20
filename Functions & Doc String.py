def func(a,b):
    """This Function calculates the sun of two given numbers"""
    s=a+b
    return s
    print (s)

sum=func(2,5)
print (sum)

print( func.__doc__ )  #this prints the doc string of a function,remember to add 2 underscores before and after doc keyword
