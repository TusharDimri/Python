# Enumerate Function

l1 = ["Bhindi", "Aloo", "Chopsticks", "Chowmein"]
i = 1
for item in l1:
    if i % 2 != 0:
        print(item)
    i += 1

# Shortcut for above code

for index, item in enumerate(l1):
    if index % 2 == 0:  # Indexing stats from 0
        print(item)