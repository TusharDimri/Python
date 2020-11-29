"""
print pattern
input an integer &
 boolean=
 and print
*
**
***
****
if true
&
****
***
**
*
if false
"""

num = int(input("Enter a number"))
t = int(input("Enter 0 for False & 1 for True"))
boole = bool(t) # Type casting into boolean
if boole == True:
    # for i in range(num+1):
    #     print("*"*i)
    i = 1
    while num > 0:
        print(i*"*")
        num = num - 1
        i = i + 1
else:
    while num > 0:
        print("*"*num)
        num = num - 1
