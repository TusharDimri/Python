# Exceptions are raised in python using 'raise' keyword.Exceptions are user defined exception

a = input("Enter your name")

if a.isnumeric():
    raise Exception("Name cannot be numeric")

# Assume that the task following above code is bulky.It will save a lot of time if we raise excetpion it will prevent us
# from ding things the wrong way.

print("Important Task")

# There are many built in exceptions in Python,Do check it out online.

# Another Example

a = int(input("Enter a number"))
b = int(input("Enter a number"))

if b == 0:
    raise Exception("0 division Error")
else:
    print(int(a/b))

# Another Example

c = input("Enter  your name")
try:
    print(c)

except Exception as e:
    if c == "Tushar":
        raise ValueError("Access Denied")
    print("Exception Handled")
