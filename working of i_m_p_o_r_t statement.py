import speech_recognition as sr
print(sr.__version__)#prints version of module installed in system

import pyaudio
print(pyaudio.__version__)#prints version of module installed in system

import sys
print(sys.path)
"""
this tells us the path(hierarchy) from which modules are imported.A we can check in our output, the first path is the one we are 
currently working in.This is why we are advised to avoid naming our files by module name.If we do so,system will import
our file rather than the required module and system will show error.   
"""
import file2 #file2 is file created for better unDerstanding of this code
print(file2.a)
file2.printjoke()

#alternative meathod
from file2 import a
print(a)
from file2 import printjoke
b=printjoke()#none printed in output is because this function do not return a value
print(b)

# YOUR FILE SHOULD NOT HAVE THE SAME NAME AS A MODULE NAME