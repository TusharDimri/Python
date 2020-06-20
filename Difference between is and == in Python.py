# == :- Value Equality - 2 objects have same identity/value

# is :- reference equality - 2 refernces have same object/allocated memory

a = [2, 43, 69]
b = a
print(b == a)
print(b is a)

# Output is True because both a and b point to the same memory location

# As both a and b point to the same memory location, therefore chanes made to one will be automatically made to the other
a[0] = 3
print(b) # See output

c = [21, 32, 45]
d = c[:]
print(c == d)
print(c is d)
# Output shows that both c and d have same idemtity but don't have same references
# This is because d is a copy of d,Consider them being identical twins with different personalities

user1 = [1,2,3]
user2 = [1,2,3]
print(user1 == user2)
print(user1 is user2)

# Strings show different output though(Depends on hw Python allocates Memory)
user3 = "Poko F1"
user4 = "Poko F1"
print(user3 == user4)
print(user4 is user4)
print(id(user3))
print(id(user4))
user3 = ""
print(user3)
print(user4)

