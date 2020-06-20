def printnote(string):
    return f"My Favourite Guitarist Is {string}"

def add(n1, n2):
    return n1+n2+5

print("The Name Is:-",__name__)
print("WE RAN THIS FROM NAME1")

if __name__ == '__main__':
        print(printnote("Jimmi Hendrix"))
        o= add(68,1)
        print(o)

# Name == Main in Python2 is the second part of this code
import os
os.rename("NAME1.py", "(if __name__=='__main__') in Python.py")