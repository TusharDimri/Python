age=int(input("Enter Your Age"))

if age < 18:
    print("You cannot drive legally")
elif age > 18:
    print("You can drive")
elif age == 18:
    print("You need to come for examination")

"""
If we use if statement is place of elif statement the condition will be tested for every if statement even if it is
found to be true for ome such statement.
This is why we use elif statement in place of multiple if statements.
"""

l1 = [1, 5, 21]
if 5 in l1:
    print("Yes")
elif 4 not in l1:
    print("Yes")
else:
    print("No")
print(1 in l1)
print(21 in l1)

# Shorthand if and else statements in python

num1 = int(input("Enter a number"))
num2 = int(input("Enter another number"))
if num1 > num2: print("The number you entered first is bigger")
else : print("The number you entered second is bigger")

# One liner Conditional Statements :-

a1 = int(input("Enter a number"))
a2 = int(input("Enter a number"))
print("The number you entered first is bigger") if a1 > a2 else print("The number you entered second is bigger")