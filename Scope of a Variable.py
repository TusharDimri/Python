l = 10  # This is a Global variable i.e. the scope of this variable is Global
def func1(n):
    l = 5  # This is a Local variable
    # We cannot change the value of a local variable inside a function.
    # l is first checked for in local scope and then in global scope.If the variable is not in global scope then error
    # is thrown
    # print(x) will throw an error
    print(l, "is a local variable")
    print(n, "Keep Rocking")

func1("Let\'s Rock")
print(l, "is a global variable")

m = 10  # This is a Global Variable
def func1(n):
    global m  # This keyword allows global variable to be altered inside the function
    m = m + 40
    print(m, "the edited local variable")
    print(n, "Keep Rocking")

func1("This is")
print(m, "Is the global variable (printed outside the function)")

x = 23
def tushar():
    x = 20
    def J():
        global x # Using the global keyword we change a global variable locally
        x = 69
    print("Before Calling J() = ", x)
    J()
    print("After Calling J() = ", x)
# The value of x does not change after calling J() because global keyword change the value of only the global variable

# When we use global keyword the variable is allocated outside the block.

print(x)
tushar()
print(x)
