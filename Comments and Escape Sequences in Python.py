# This is a single line comment

""""
This is a
multiline
comment
"""
'''
This is 
also
a Mult
Line Comment
'''

print("Hello")
print("World\n")
# As we can see 2 different print statements are separated by a newline character

print("Hello",end = "")
print("World\n")
#  Every print statement ends with a default newline character

print("Violin",end="and")
print("Guitar\n")

print("Welcome to my world.","Let's go\n")
# In the above code ',' adds space(single space) between 2 different statements

# To skip escape sequences we use //
#  For Example :-
print("C:Harry\\narry")
# Above statement will ignore \n and read it as n.

# When giving system path we use \\ in place of \ tp avoid clash with Escape Sequence Characters.