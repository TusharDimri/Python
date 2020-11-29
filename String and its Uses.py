mystr = "Rock is Alive"
print(mystr)
print(mystr[0:5])  # String slicing
print(len(mystr))
print(mystr[0:14]) # For full string,length
# print(mystr[69]) will generate error :- index out of range
print(mystr[0:69])  # This will print complete string
print(mystr[0:]) # 0 to end index of string
print(mystr[:13]) # From 0th index to 13th index(if any) pf string
print(mystr[0:10:2])
print(mystr[0::2])
print(mystr[::2312])
print(mystr[::69]) # Only 1st index is printed
print(mystr[::]) # Complete string is printed
print(mystr[-6:-1])
print(mystr[::-1])# Reverses the string
