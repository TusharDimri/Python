age=int(input("Enter Your Age"))
if age<18:
    print("You cannot dirive legally")
elif age>18:
    print("You can drive")
elif age==18:
    print("You need to come for examination")

# Shorthand if and else statements in python

num1 = int(input("Enter a number"))
num2 = int(input("Enter another number"))
# if num1>num2: print("The number you entered first is bigger")
# else: print("The number you entered second is bigger")

# One liner
print("The number you entered first is bigger") if num1>num2 else print("The number you entered second is bigger")