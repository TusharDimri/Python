def searcher():
    import time
    time.sleep(4) #Assume this to be any time consuming task
    fil = "This is where you will search. Assume this to be a file"

    while True: #line 6-7 make this function a coroutine
        word = (yield)
        if word in fil:
            print("Found")
        else:
            print("Not Found")


a = searcher()
print("Search Started")
next(a)  # The function will take time when next method is executing(check output)
print("next method ran successfully")
a.send("search")
print("Now function will work smoothly")
a.send("this")
a.send(".")
a.send("wfead")

a.close() # Closes the coroutine(similar to closing a file)