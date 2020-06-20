def func_print(a,b,c): #simple function to print arguments passed
    print(a,b,c)
func_print(1,2,3)

# *args

def arg_func(normal,*args): #writing args is just a covntion,the argument can have an name but * is mandatory
   print(type(args))  #this tells as that args are stored in the form of a tuple inside the function even after being passed as a list
   print(normal)
   for name in args:
        print(name)
nm="Team Blacklist:-"
l=["Tushar","Yash","Tanmay","Aditya","Akhil"]
arg_func(nm,*l)

# **kwargs

def kwrg_func(nor,*args,**kwargs):
    for item in args:
        print(item)
    print("TEAM BLACKLIST:-")
    for key,value in kwargs.items():#.items allow us to unpack dictionary(**kwargs)
        print(f"{key} is {value} in the team") #f string

nor="Class:-"
pos=[1,2,3,4,5]
# dict={"Tushar":"Leader","Tanmay":"Co-Leader","Aditya":"Elder","Yash":"Elder","Akhil":"Member"}
# kwrg_func(nor,*pos,**dict)
dict={}
for i in range(5):
   nm=input("Enter Name to be added in Team Blacklist")
   position=input("Enter position of member to be added")
   dict[nm]=position
kwrg_func(nor,*pos,**dict)
#like args kwargs is alos just a convention to the argumnet dictionary passed but ** is what make i a kwarg

"""
NOTE:- if we write *args and **kwargs as arguments in a function but pass no value of both the function will still show 
no error and work with simle argument(i.e. neither arg or kwarg),but variables argumented in a function should be in 
asending order as:_
simple argument<followed by>,*args<followed by>,**kwargs
or else the sytem will show error
"""
def func(nm,*args,**kwargs):
    print (nm)
func("Tushar Dimri")

"""
But, code given below will generate error
def func(**kwargs,nm,*args):
    print (nm)
func("Tushar Dimri")
"""

