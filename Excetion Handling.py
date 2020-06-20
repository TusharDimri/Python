num1=input("enter a number")
num2=input("enter a number")
try:
    print("sum is",int(num1)+int(num2)) #for this to work user input should be a number or error will be shown
except: #this part of program executes even if try part shows an error due to string input by user
    print("this line is very important")   #let this be a very important line
