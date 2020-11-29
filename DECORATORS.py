# Decorators in Python are used  modify the functionality of a function

def func():
    print("LETS ROCK")

func2 = func  # Assigning func to func2
del func  # This deletes function 'func'
func2()

# A function returning another function
def funcret(num):  # The name funcret implies function returner
    if num == 0:
        return print  # This return built in function print
    else:
        return int   # This return built in function sum
a = funcret(0)
print(a)
a("Hii")

b = funcret(1)
print(b)
c = b("21")
c = c + 1
print(c)


# Function as an argument of another function

def executor(func):
    func("this")

executor(print)  # print function is passed as an argument to the function executor(this evaluates to = print("this") )

# DECORATORS

def dec1(func1):
    def nowexe():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexe()

def task(): # Check Output
    print("This Is The Task To Be Executed")
task = dec1(task) # Here, function task is passed as a argument to function dec1
task()
# Shortcut for line 46 and 46 using decorators
@dec1  # This is a decorator
def task():
     print("This is the task to be done")  # Decorator above is equivalent dec1(task)


