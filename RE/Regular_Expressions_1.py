# EMAIL DETECTION------------------------------
import re
pattern ='[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|edu|du)'
x = input()
# if re.match(pattern,x,re.IGNORECASE):
if re.match(pattern,x):
# if re.search(pattern,x):
    print('ok')
else:
    print('Not a email')
