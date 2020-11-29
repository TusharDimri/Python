import math

# String Formatting


me = "Tushar"
t = "This is %s"%me
print(t)

ca = "Mayer"
nm = "John"
a = "This is {1} {0}"
b = a.format(ca, nm)
print(b)

# f strings
c1 = input("Enter Your Name")
c2 = input("Enter Your Surname")
f_str = f"This is {c1} {c2} {23*3} {math.cos(65)}"
print(f_str)
"""
f strings are in simple words strings which contain  variable values
f in s strings stands for fast as f strings is the fastest method for string formatting
"""