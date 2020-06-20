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
"""

num=int (input("Enter a number"))
t=int(input("Enter 0 for False & 1 for True"))
boole=bool(t)#type casting into boolean
if boole==True:
    for i in range(num+1):
        print("*"*i)
else:
    for i in range(num,0,-1):
        print("*"*i)