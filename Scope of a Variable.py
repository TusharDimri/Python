l=10 #Global variable

def func1(n):
    l=5 #Local variable
    print(l,"is a local variable")
    print(n,"Keep Rocking")

func1("Let\'s Rock")
print(l,"is a global variable")

l=10 #Global Variable
def func1(n):
    global l #this keyword allows global variable to be altered inside the function
    l=l+40
    print(l,"is a local variable")
    print(n,"Keep Rocking")

func1("Let\'s Rock")
print(l,"is a global variable")

def Td():
    x=20
    def J():
        global x
        x=69
        print("Before Calling j()",x)
        j()
        print("After Calling j()", x)
Td()
print(x)

