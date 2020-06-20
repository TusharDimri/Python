# Content from Corey Schafer"s You Tube channel
import requests

r = requests.get('https://xkcd.com/353/')

print(r) # Returns a response object

print(dir(r)) # Object Introspection

print(help(r)) # In depth Object Introspection

print(r.text) # We used text using object introspection
# Above returned HTML text which can be parsed using HTML parser(Beautiful Soup)

# Image using requests module

image = requests.get('https://imgs.xkcd.com/comics/python.png')
print(image.content) # Returns bytes
with open("comic.png", 'wb') as f:
    f.write(image.content)


print(r.status_code) #To introspect response
print(r.ok) # If response if ok and is accepted
print(r.headers)