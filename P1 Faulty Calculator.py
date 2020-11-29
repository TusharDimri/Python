""" a calculator that solves all the problems except
45*3=555
56+9=77
56/6=4"""
num1 = int(input("Enter a Number"))
num2 = int(input("Enter a Number"))
ch = int (input("PRESS 1 for addition,2 for division ,3 for multiplication & 4 for subtraction"))
if ch == 1:
    if num1 == 56 and num2 == 9:
        print("77")
    else:
        print(num1+num2)
elif ch == 2:
    if num1 == 56 and num2 == 6:
        print("77")
    else:
        print(num1/num2)
elif ch == 3:
    if num1 == 45 and num2 == 3:
        print("555")
    else:
        print(num1*num2)
elif ch == 4:
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)
else:
    print("Wrong Choice")