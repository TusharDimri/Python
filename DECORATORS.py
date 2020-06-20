# Decorators In Python modify the functionality of a function

def func():
    print("LETS ROCK")

func2 = func
del func #this deletes func Function
func2()

# a function returning another function
def funcret(num):
    if num == 0:
        return print #this return built in function print
    else:
        return sum   #this return built in function sum
a = funcret(0)
b = funcret(1)
print(a)
print(b)

#function as an argument of another function

def executor(func):
    func("this")

executor(print) #print function is passed as an argument to the function executor(this evaluates to = print("this") )

# DECORATORS

def dec1(func1):
    def nowexe():
        print("Executing Now")
        func1()
        print("Executed")
    return nowexe()
def task():#check output
    print("This Is The Task To Be Executed")
dec1(task)
# shortcut for line 38 using decorators
@dec1  #this is a decorator
def task():
     print("This is the task to be done") # Decorator above is equivalent dec1(task)


