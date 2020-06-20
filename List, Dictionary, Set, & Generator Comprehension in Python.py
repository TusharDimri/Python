# The code given below is to print a list containing multiples of 3 which are less than 100 using 3 different methods

# Method 1

l1 = list()

for i in range(100):
    if i % 3 == 0:
        l1.append(i)

print(l1, "\n")

# Method 2(Better logic)

l2 = list()

for i in range(0, 100, 3):
    l2.append(i)

print(l2, "\n")

# Method 3 (Using List comprehension)

l3 = [i for i in range(100) if i % 3 == 0]
print(l3, "\n")

# Or

l4 = [i for i in range(0, 100, 3)]
print(l4, "\n")

# We can do many complex list tasks in a single line using list comprehensions


# We can also do "Dictionary" comprehension in python

dict = {i: f"item {i}" for i in range(100) if i % 3 == 0}  # Creating a dictionary using dictionary comprehension
print(dict, "\n")

# Using Dictionary Comprehension to reverse key : value pairs if a dictionary
dict2 = {i: f"item {i}" for i in range(10)}
dict3 = {value: key for key, value in dict2.items()}
print(dict2)
print("\n")
print(dict3)
print("\n")
# We can also use Set Comprehensions in Python

dresses = {dress for dress in ["dress 1", "dress 1", "dress 2", "dress 3", "dress 2", "dress 3"]}
print(dresses)  # note that sets don't contain repeated values
print("\n")

# Generator Comprehensions in Python

gen = (i for i in range(50) if i % 2 == 0)  # Parenthesis are use for Generator Comprehension
print(type(gen))
print(gen.__next__())
print(gen.__next__())
for item in gen:  # This don't start generating values from 0 as 0 has been already generated
    print(item)
# Remember that generators can be generated only once
