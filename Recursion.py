# To  print factorial 5 using for loop
from typing import Any, Union

def fac_iterative():  # Calculate factorial using Iterative Approach
    f = 1
    for i in range(1,6):
      f = f * i
    return f

factorial = fac_iterative()
print("Factorial of 5 is",factorial)

def fac_recursive(n): # Calculate factorial using Recursive Approach
    if n == 1:
        return n
    else :
        return n * fac_recursive(n-1)
f = fac_recursive(5)
print("Factorial of 5 using recursion is",f)
"""

Logic Behind above Recursion:-

Recursion Stack:-
5 * fac_recursive(4)
5 * 4 * fac_recursive(3)
5 * 4 * 3 * fac_recursive(2)
5 * 4 * 3 * 2 * fac_recursive(1)
5 * 4 * 3 * 2 * 1

"""


# Fibonacci series using recursion
def fibo(n):
    if n <= 1:
        return n
    else:
        return n + fibo(n-1)
n=int(input("Enter the number of series elements to be printed"))
print("Fibonacci Series upto", n, " terms is:-")
for i in range(n):
    ser = fibo(i)
    print(ser, end=" ")
