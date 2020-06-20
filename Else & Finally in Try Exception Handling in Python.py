t1 = open("J1.txt")

try:
    t2 = open("No File.txt")

except IOError as e:
    print("IoError Occured")
    print(e)

except EOFError as f:
    print("EOFError Occured")
    print(f)

else:
    print("This will execeute if except block do not execute")

finally:  # Finally is used for code cleanup after Exception Handling
    print("This block will execute no matter what")
    t1.close()

print("Important Stuff")
