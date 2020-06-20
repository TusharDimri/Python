#s= set()
#print(type(s))
#l=[1,2,3,4]
#s_from_list=set(l)
#print(s_from_list)
s1=set()
s1.add(1)#adding elements into a set
print(s1)
s2=s1.union({2,3,4,5})#union of 2 sets
print(s1," ",s2)
s3=s2.intersection({2,3,4,10,11,12,69})#intersection of 2 sets
print(s3)
s3.remove(3)
print(s3)