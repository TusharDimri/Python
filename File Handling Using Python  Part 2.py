# .tell() tells us the position of the file pointer
t = open("Tushar.txt")
print(t.tell())
print(t.readline())
print(t.tell())
print(t.readline())
print(t.tell())
print(t.readline())
print(t.tell())
t.close()

# .seek() brings the file pointer to the specified position
t = open("Tushar.txt")
print(t.tell())
print(t.readline())
print(t.tell())
print(t.readline())
print(t.tell())
print(t.seek(0)) # prints argument of seek funtion i.e. 0 in this case & bring pointer to the n th charecter of the argument in the file
print(t.readline())


t.close()

# Opening files using with block

t = open("Tushar.txt")
print(t.readline())
print(t.readline())
t.close()

# Alternative for above code using with block

with open("Tushar.txt") as t:
    print(t.readline())
# No need to close the file

"""
If we open a file outside with block and print readline() once and close it the file opened will print its 
first line if exists.
"""