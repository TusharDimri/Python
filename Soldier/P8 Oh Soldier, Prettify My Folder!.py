"""
def Soldier("path", "dictionary file", "file format")
We have to define above functions where user gives path and a text file with words and a format.We have to capitalize
all the words of the files in the folders of the given path but the words in the given text file should not be handld.
Also, files with the format passed by the user should be renamed in order.format.
For Example:-
def Soldier("C://", "tushar.txt", ".jpg")
So all files in path should be handled and jpg files to be renamed as:-
1.jpg,v 2,jpg ,etc.
"""
import os

def Soldier(path, format):
    os.chdir(path)
    files = os.listdir()
    c = 1
    for file in files:
        if str(file.split(".")[1]) in format:
            os.rename(file, str(c)+format)
            c = c+1


path = input("Enter the path of the folder you want to beautify")
form = input("Enter format of the file")
format = "."+form.lower()
Soldier(path, format)
