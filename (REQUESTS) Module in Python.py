# NOTE :- There are many different type of requests but here we will cover only get & post requests
# Check out documentation of this module("Requests for humans") for better understanding of this module
# Do check out financial modeling prep.com. We will use it as an example here.

import requests

req1 = requests.get("https://financialmodelingprep.com/api/v3/cryptocurrency/BTC") #this is a get request
print(req1.text) # prints the given parameter from the api of the given link
print(req1.status_code) # Check "http status code" online to fine out meaning of different status codes

# Given below is an example of post request(not a real time example)
# url = "www.something.com"
# data = {"p1": 4,
#         "p2": 5
#     }
# r2 = requests.post(url = url, data = data )  # this will not give any response as this is not a valid website in real time

# Do note that this module cannot be used to parse the data we get using this module