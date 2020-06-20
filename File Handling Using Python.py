#file io basics
"""  "r" = open file for reading(default mode)
     "w" = open file for writing
     "X" = creates a file if already exists and fail if it already exists
     "a" = adds\append more content to a file
     "t" = text mode for text files(default mode)
     "b" = binary mode
     "+" = read + write mode
"""
#print(func1.__doc__)# it is the code to print doc string of a function func1(answer to question of the day)

td = open("Tushar.txt")
obj = td.read()
print(obj)
td.close()

td = open("Tushar.txt")
obj = td.read(3) #first 3 characters of tect file are accessed
print(obj)
obj = td.read(3) #next 3 characters of tect file are accessed(check output)
print(obj)
td.close()
"""above code shows the importance of closing a file after opening it"""

td = open("Tushar.txt")
obj = td.read(56666)
print("2",obj)#obj gets ignored as 56666 is greater than the file's lenghth(check output)
td.close()

td = open("Tushar.txt")# check output and compare it with the next chunk
obj = td.read()
for line in obj:
    print(line)
td.close()

td = open("Tushar.txt")
for line in td:
    print (line,end="")
td.close()

#BUT THIS CHUNK OF (because of line 43)
td = open("Tushar.txt")
obj = td.read()
for line in obj:
    print(line)
td.close()
#WILL PRINT NOTHING


td = open("Tushar.txt")
print(td.readline()) #prints one line of the file at a time
td = open("Tushar.txt")
print(td.readline())
#check output (that space is beacause uf newline character at the end of line)
td.close()

td = open("Tushar.txt")
print(td.readlines())#prints a list whose elements are the lines of the text file
#\n in the list shows the end of line of the file
td.close()

#writing and appending in a text file
td2 = open("Tushar2.txt","w")
td2.write("Delhi is not far")
# creates a file if it don"t exist and overwrites already existing files
td2.close()

td3= open("Tushar.txt","a")
a=td3.write("\nViolin and Guitar are awesome")
print(a)
td3.close()

td4= open("Tushar2.txt","r+")#Handle both read and write mode
print(td4.read())
td4.write("\nKeep Rocking")