# Iterables, Iterators and Iteration
"""
Iterables :- Objects that can be iterated. Methods __iter__() or __getitem__() are defined for iterables and generate an
iterator for the iterable.
Iterator :- Object that  is used to iterate an iterable.Function __next__() is defined for an iterator and is used to
iterate the iterable object.
Iteration :- Entire process of iterating is called iteration. For example :-
for i in range(n):
    print(n)
This will generate and print n values,but range function is a generator,It generates one value at a time and these value
-s are then printed one by one.
Here, n is iterable and is then iterated.This process completely is called as iteration.
Generators are  type of iterators which can only be traversed once
"""


def gen(n):
    for i in range(n):
        yield i   # 'yield' keyword will make a user defined generator the stores the  values of i  in an object

g = gen(3) # g is a generator containing yielded values of i
print(g) # this shows that g is an object(an iterable object)

# now we will iterate g using an iterator
print("\n")
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__()) printing again will generate an error as g is capable of generating only 0,1,2
print("\n")
# Alternative method to generate values of g

h = gen(4)

for i in h: # this process stops automatically at the last value of h
    print(i)

print("\n")

t = "tushar"   # t is an iterable string
for char in t:
    print(char)

print("\n")
t1 = t.__iter__() # iterable
print(t1.__next__())  # iterator
print(t1.__next__())
print(t1.__next__())
# complete process from line 42 to line 45 is an iteration

"""
i = 1231243 is an integer
t = __iter__(i)
line 53 will generate an error because i is an integer an integers are  not iterable
"""

"""
NOTE:- Why are generators used?
Generators are used to store iterable values which it is capable of generating at our will.
It is used to save large values to save our ram.
"""

# Factorial of a user input number
fac = 1
def factorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac = fac * i
        yield fac

n = int(input("Enter a number"))
generator = factorial(n)
for j in generator:
    print(j ,end= " ")




# Fibonacci Series upto n terms

def fibonacci(n):
    a = 0
    b = 1
    fibo = 0
    yield a
    yield b
    for i in range(n-2):
        fibo = a + b
        a = b
        b = fibo
        yield fibo

print("\n")
n = int(input("Enter the number of terms of the Fibonacci Series that you want to generate"))
generator = fibonacci(n)
for i in range(n):
    print(generator.__next__(), end=" ")

print("\n")
for i in generator:
    print(i, end=" ")
else:
    print("The chunk of code(98-100) gives no output as a generator can be traversed only once and we already traversed it")