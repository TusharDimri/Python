import re

text = """farsatsdgbvhqefscbgvdxuhsIAdkbcwfuhvbcwuthnfskdnfhwirbgsdiunfaduognfivnfsjngdbklndgovnsflkvnfsljbnflkbsbnksflk
wjvnfjnvsfbnsfljbnfsljbnfsjlbnfsjbnsfkjbnfsljbntogndslbnsjlbtvjlsdnvosfdndljafnwoafncfsjvnsdljncealfnaiorgnrouanfoaaofns

AVDCWHDASDIAUVBEGIBFVIADNBVEIGBVIESVBPRUVBINIUPGIUPVGIUPRIPVUEGWUIVBGRVPIUGRBVGIRWNIHJBVFGWFVBUGDFBVUFBEFQUHVBEFVHBFBVLE

1234465836835

Ha HaHa
MetaCharacters (need to be escaped)
. ^ $ *+ ? {} [] \ | ()

https://www.google.com
http://coreyms.com
https://youtube.com
http://www.nasa.gov

231-555-4321
231.433.4231
321*312*2312

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mr Ak47

tushar.dimri22@gmail.com
tushar.dimri@university@edu
tushar-321-dimri@my-work.net
"""

sentence = "Start a sentence and bring it to an end"

# What is a raw string
print("Tushar \t Dimri")
print(r"Tushar \t Dimri") # This is a raw string
# As we saw in the output, raw string ignores escape sequences and give preference to meta characters

pattern = re.compile(r'fsj') # This creates a variable which can be search in the string we want
matches = pattern.finditer(text)
for match in matches:
    print(match)
# This returns a match object where match is the pattern and span is the index in which it was found(check output)

# Meta characters carry special meaning for pattern and are ery helpful while forming patterns
# To search for meta characters normally we need to escape the ]m using '\'. For example:-
fullstop = re.compile(r'\.')
matches1 = fullstop.finditer(text)
for fullstop in matches1:
    print(fullstop)
# If we don't escape the '.' then we will get all characters except newline in the string as an object as '.' is a meta
# character


# Searching using word boundary (\b)
# Word Boundary means that we have a space(Space, Whitespace, Newline) before our pattern
pattern = re.compile(r'\b Ha')
matches3 = pattern.finditer(text)
for match in matches3:
    print(match)

# ^ and $ are used to search something at the beginning or at the end of a string
pattern1 = re.compile(r'^Start')
matches4 = pattern1.finditer(sentence)
for match in matches4:
    print(match)

pattern2 = re.compile(r'end$')
matches5 = pattern2.finditer(sentence)
for match in matches5:
    print(match)

# Creating a pattern to match digits(phone number)
pattern3 = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')
matches6 = pattern3.finditer(text)
for match in matches6:
    print(match)

# Create a pattern to check for digits in range 1 to 5
pattern4 = re.compile(r'[1-5a-z]')# It will check for numbers between 1 and 5 including 1 & 5.Also, a-z match lower case
matches7 = pattern4.finditer(text)
for match in matches7:
    print(match)

pattern5 = re.compile(r'^[1-5a-z\n\.]a-z\n\.') # It will check for anything except specified values
matches7 = pattern5.finditer(text)
for match in matches7:
    print(match)

# Alternative for 67-70
pattern6 = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
matches8 = pattern6.finditer(text)
for match in matches8:
    print(match)

# Pattern to match name(20-24)
pattern7 = re.compile(r'M(r|s|rs)\.?\s[A-Za-z]\w*')
matches8 = pattern7.finditer(text)
for match in matches8:
    print(match)

# Matching different types of e-mails
pattern8 = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
matches9 = pattern8.finditer(text)
for match in matches9:
    print(match)

# Matching urls
pattern9 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches10 = pattern9.finditer(text)
subbed_urls = pattern9.sub(r'\2\3', text)
print(subbed_urls)

for match in matches10:
    print(match)

# Other Regular Expressions Functions

# findall() method
pat = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
mat = pat.findall(text)
print(mat)
for match in mat:
    print(match)
# As we can observe that findall method matched the groups i.e. pattern inside () which in this case is ((Mr|Ms|Mrs))

# Bur=t, if there are no groups in our pattern then this method will return a list containing the matches found
# For Example:-

pat2 = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
mat2 = pat2.findall(text)
print(mat2)
for match in mat2:
    print(match)

# If there are multiple groups in our pattern the see for yourself what this returns
pat3 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
mat3 = pat3.findall(text)
print(mat3)
for match in mat3:
    print(match)
# As we can  see in the output this returned a sting containing all the matching groups in a tuple as one element

# Another method of regular expressions module is match() method
patt = re.compile(r'Start')
match = patt.match(sentence)
print(match)

# Note that this method is used to match only the beginning of of the string
# Check this example
patt1 = re.compile(r'sentence')
match = patt1.match(sentence)
# Although there is a 'sentence' in the specified string yet no match us returned
# An alternative is to used ^ character of re.finditer method

# Another method of regular expressions is search()

patt3 = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
match = patt3.search(text)
print(match)

# As we can see in the output, this method returns the first match it found while traversing the string

# Concept of flags:-

patte = re.compile(r'start', re.IGNORECASE)
matc = patte.finditer(sentence)
for match in matc:
    print(match)