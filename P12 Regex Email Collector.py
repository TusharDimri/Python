# Herw we will find emails in a string using re module

import re

str = '''
farsatsdgbvhqefscbgvdxuhsIAdkbcwfuhvbcwuthnfskdnfhwirbgsdiunfaduognfivnfsjngdbklndgovnsflkvnfsljbnflkbsbnksflk
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
tushar.dimri@university.edu
tushar-321-dimri@my-work.net
xyz.trfw.@frt.zz
xyz.trfw.@frt.z
dimrivp@gmail.com
lucifer#mo)rningstar@gmail.com
'''

email = re.compile(r'[a-zA-Z1-9._#%]+@[a-zA-Z1-9._+-]+\.\w{2,10}')
match = email.findall(str)
print(match)

# Alternative Method
match = re.findall(r'[a-zA-Z1-9._#%]+@[a-zA-Z1-9._+-]+\.\w{2,10}', str)
print(match)

# As we can see we can skip re.compile part(line 42)
