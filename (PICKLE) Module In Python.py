# Pickle is a built in module in pyhton
# Pickling is the process of preservation of an object

import pickle

# Pickling a Python object in a binary file:-
cars = ["BMW", "FERRARI", "AUDI", "LAMBORGHINI"]
vehicles = ["Private Jet", "Private Helicopter", "Luxury Cruise"]
preserve = "Preservation.pkl"
td = open(preserve, "ab")
pickle._dump(vehicles, td)
pickle.dump(cars, td)

td.close()

# Obtaining a pickled Python object from a binary file

file = "Preservation.pkl"
td = open(file, "rb")
myvehicles = pickle.load(td)
print(myvehicles)
print(type(myvehicles))

mycars = pickle.load(td)
print(mycars)
print(type(mycars))

td.close()
