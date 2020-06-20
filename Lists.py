
#list slicing is simiar to string slicing
list = [1,5,3,7,10]
list1 =list[::-1]
print(list1)
list.append(6)
print(list)
list.insert(1,69)#at 1st index of the sting value 69 will be inserted
print(list)
list.pop(3)
print(list)
list[1]=98
print(list)#list are mutable i.e. they can change
tp =(1,5,3,7,10)
print(tp)
"""tp(1)=8
print(tp)"""#this will generate error because tuples are immutable i.e. they cannot change
tp=(1,)#when tuple has only 1 element thean a ',' is added after the element
print(tp)
#swapping traditionally
""" a & b are two int variables with differemt values
temp=a
a=b
b=temp"""
#easy swapping
a=10
b=8
print("a is",a," & b is",b)
a,b=b,a
print("after swapping,a is",a," & b is",b)