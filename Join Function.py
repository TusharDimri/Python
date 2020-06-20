list = ["John Mayer","Jimmi Hendrix","Randy Rhodes","Jimmy Page","Kurt Cobain"]
for item in list:
    print(item, "and", end=" ") #this meathod adds  unwanted "and" at the end of list i.e. after "Kurt Cobain"(check output)

names = " and ".join(list) #point to note is that join function do not add unwanted "and" at the end of the list
print(names, " and other guitarists")