# File IO basics
"""  "r" = open file for reading (Default Mode)
     "w" = open file for writing
     "x" = creates a file if already exists and fail if it already exists
     "a" = adds more content to a file
     "t" = text mode for text files (Default Mode)
     "b" = binary mode
     "+" = read + write mode
"""
# print(func1.__doc__)  is the code to print doc string of a function func1(answer to question of the day)


#                              READING A FILE



td = open("Tushar.txt") # td is a file pointer / file handle, open returns a file pointer for the file
obj = td.read() # Complete file is printed (Check Output)
print(obj)
td.close()

td = open("Tushar.txt", "rt")
obj = td.read(3) # First 3 characters of text file are accessed
print(obj)
obj = td.read(3) # Next 3 characters of text file are accessed (check output)
print(obj)
td.close()
""" Above code shows the importance of closing a file after opening it """

td = open("Tushar.txt")
obj = td.read(56666)
print("1", obj) # All character are printed as there are less than 56666 characters in the file(check output)
obj = td.read(56666) # It reads the specified number of characters
print("2", obj) # obj gets ignored as we have already accessed all the characters in the file(check output)
td.close()

td = open("Tushar.txt") # check output and compare it with the next chunk/block of code (line 43-46)
obj = td.read()
for char in obj: # we will traverse each 'character' of the file using char variable/loop variable
    print(char)
td.close()

td = open("Tushar.txt")
for line in td: # We will traverse each 'line' of the file using line variable /loop variable
    print(line, end="")
td.close()

# BUT THIS CHUNK OF (because of line 45 as read takes all the content of the file and we cannot use it later)
td = open("Tushar.txt")
obj = td.read()
for line in obj:
    print(line)
td.close()
# WILL PRINT NOTHING


td = open("Tushar.txt")
print(td.readline())  # prints one line of the file at a time with newline character at the end of line
td = open("Tushar.txt")
print(td.readline())
# Check output (that space is because of newline character at the end of line which is part of the line)
td.close()

td = open("Tushar.txt")
print(td.readlines()) # prints a list whose elements are the lines of the text file
# \n in the list shows the end of line / newline character of the file
td.close()


#                        WRITING TO A FILE



# Writing and appending in a text file
td2 = open("Tushar2.txt", "w")
td2.write("Delhi is not far")
td2.write("\nSee You Again Later")
# Creates a file if it doesn't exist and overwrites already existing files
td2.close()

td3= open("Tushar.txt", "a")
a = td3.write("\nViolin and Guitar are awesome")
#  a contains the number of characters that we wrote in the file.
print(a)
td3.close()

td4 = open("Tushar2.txt", "r+") # Handles both read and write mode
print(td4.read())
td4.write("\nKeep Rocking")