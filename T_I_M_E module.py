# code to find execution time of a program
import time

#for loop
initial_f = time.time()
for i in range(51):
    print("Hello World(for loop)")
    # time.sleep(1) gives a timelag of 1 second while executing progra(check output)
print("Execution Time for for loop:-",time.time() - initial_f,"seconds")

#while loop
k=0
initial_w=time.time()
while(k<51):
    print("Hello World(while loop)")
    k+=1
print("Execution Tme for while loop:-",time.time() - initial_w,"seconds")

localtime = time.localtime(time.time())#this returns a tuple form of time(check output)
print(localtime)

local_time = time.asctime(time.localtime(time.time()))#localtime in time localtime is a keyword
print(local_time)



