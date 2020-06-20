import os

# OS module is a built in module in Python.OS stands for operating System

# print(dir(os))
# print(os.getcwd()) Tells us the directory we are currently working in
# Now we will see how to change our current working directory
# os.chdir("C://")   #chdir :- change directory
# print(os.getcwd())


# listdir returns a list containing names of folders and  in current working directory or specified path
print(os.listdir())
print(os.listdir("C://"))  # returns the name of folders in given path


#  Now to create a folder using os module we will use mkdir method
# os.mkdir("This") if no path is specified the folder is created in the current working directory
# We can create a directory(folder) and its subdirectories(subfolders) using makedirs function
# os.makedirs("Folder/Subfolder")

# Now we will rename a file using rename method
# os.rename("P2 Star Pattern.py", "P2 Pattern.py")

# Now we will check the enviroment variables in the path.Every time we use are computer, some enviroment variables are set

print(os.environ,"\n")

print(os.environ.get('Path'))

# This is how we use os module to join paths
print(os.path.join("C:/", "/TD1.txt"))

# Now using os module we will check whether a path exists or not
print(os.path.exists("C://Program Files"))

# Now using os module we will check whether a file exists or not
print(os.path.isfile("Ji.txt"))

# Now using os module we will check whether a directory exists or not
print(os.path.isdir("C://Program Files"))


# Statement given below imports the name of the operating system dependent module
print(os.name)


# Some useful alternative ways to get information about the operating system we are working on
import sys
import platform
p = sys.platform
print(p)
r = platform.release()
print(r)
print(platform.architecture())
print(platform.machine())

