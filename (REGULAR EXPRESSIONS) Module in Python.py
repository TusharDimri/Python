import re  # This is a built in module in Python
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +91 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
'''

# findall, search, split, sub, match, finditer are various functions of re module


# Meta Characters   [Check file "(REGULAR EXPRESSIONS) Help.txt in this directory"]

patt1 = re.compile(r'fass')
match1 = patt1.finditer(mystr)
for match in match1:
    print(match)
    print(mystr[448:452])


patt2 = re.compile(r'.ca')
match2 = patt2.finditer(mystr)
for match in match2:
    print(match)



patt3 = re.compile(r'^Tata')
matt3 = patt3.finditer(mystr)
for match in matt3:
    print(match)
patt4 = re.compile(r'iin$')

matt4 = patt4.finditer(mystr)
for match in matt4:
    print(match)

patt5 = re.compile(r'ai{2}')
matt5 = patt5.finditer(mystr)
for match in matt5:
    print(match)

patt6 = re.compile(r'(ai){1}')
matt6 = patt6.finditer(mystr)
for match in matt6:
    print(match)

patt7 = re.compile(r'ai{1}|Fax')
matt7 = patt7.finditer(mystr)
for match in matt7:
    print(match)

# Special Sequences  [Check file "(REGULAR EXPRESSIONS) Help.txt in this directory"]

pattern = re.compile(r'Fax\b')
matches = pattern.finditer(mystr)
for match in matches:
    print(match)

pattern = re.compile(r'27\b')
matches = pattern.finditer(mystr)
for match in matches:
    print(match)

pattern = re.compile(r'\d{5}-\d{4}')
matches = pattern.finditer(mystr)
for match in matches:
    print(match)

# Task:-
# Given a string with a lot of indian phone numbers starting from +91
pattern = re.compile(r'(\+91)\s\(\d{3}\)\s\d{3}\s\d{4}')
phno = pattern.finditer(mystr)
for no in phno:
    print(no)

