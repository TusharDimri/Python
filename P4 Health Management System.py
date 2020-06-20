# Health Management System
def getdate():
    import datetime
    return datetime.datetime.now()
name=input("Enter your name")
nm=name.capitalize()
if name=="Tushar":
    track=input("press D to track you diet & E to track your workout")
    if track == "D":
        a = getdate()
        d=input("Enter your Diet")
        t1=open("TD1.txt","a")
        t1.write(d)
        t1.write(str(a))
    elif track == "E":
        a = getdate()
        e=input("Track your Workout")
        t2=open("TD2.txt","a")
        t2.write(e)
        t2.write(str(a))
    else:
        print("Wrong Input")
elif name=="John":
    track=input("press D to track you diet & E to track your workout")
    if track == "D":
        a = getdate()
        d=input("Enter your Diet")
        t1=open("J1.txt","a")
        t1.write(d)
        t1.write(str(a))
    elif track == "E":
        a = getdate()
        e=input("Track your Workout")
        t2=open("J2.txt","a")
        t2.write(e)
        t2.write(str(a))
    else:
        print("Wrong Input")
elif name=="Jimmi":
    track=input("press D to track you diet & E to track your workout")
    if track == "D":
        a = getdate()
        d=input("Enter your Diet")
        t1=open("Ji1.txt","a")
        t1.write(d)
        t1.write(str(a))
    elif track == "E":
        a = getdate()
        e=input("Track your Workout")
        t2=open("Ji2.txt","a")
        t2.write(e)
        t2.write(str(a))
    else:
        print("Wrong Input")
else:
    print("Input Out Of Our Range")