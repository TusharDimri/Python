# JSON stands for Java Script Object Notation & it is a way to send data(somewhat like a protocol)
# JSON is a built in module in python

import json

data = '{"var1":"Tushar","var2":"Jason","var3":"parsing", "var4":false, "var5":null}' # This is a json string

# json.loads coverts/parses a json string to a python object(dictionary)
# This process is called as

parsed = json.loads(data) # This function parses a json string to a python dictionary(check output and compare it with data)
print(parsed)
print(type(parsed))

"""
In the above example we used a json string and parsed it into a python object(dictionary) using json.loads
But, if the json text is stored in json file(Say, abc.json) then to load it to our python code we use json.load function
NOTE:- The json file we are loading and parsing should be present in the same directory we are working in
"""

# json.dump module coverts/parses python dictionaries/objects  to a json string.(Opposite of json.loads)
# This process is called as

data2 = {
    "Name" : " Tushar",
    "Cars" : ['BMW', 'Mclaren', 'Lamborghini', 'Ferrari'],
    "Houses" : ("Japan", "USA", "New Zealand", "France"),
    "Loves" : "Himself"
}

details = json.dumps(data2, indent= 2, sort_keys=True) # Details is now a json string.
print(details)
print(type(details))

"""
In the above example we used a python object and parsed it into a json string using json.dump
But, if we want to store the python object amd store it in a json file(.json), we use json.dump function
NOTE:- The json file we are using should be present in the same directory we are working in

"""

"""
indent and sort keys parameters of json.dumps make it easier to beautify the json text be indenting per key and sorting
keys alphabetically.
"""
