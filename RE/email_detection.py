# EMAIL DETECTION------------------------------
import re
# +
# Causes the resulting RE to match 1 or more repetitions of the
# preceding RE. ab+ will match ‘a’ followed by any non-zero number of ‘b’s; it will not match just ‘a’.

pattern ='[a-zA-Z0-9_]+@[a-zA-Z]+\.(com|net|edu|du)'
# \w is the same to [a-zA-Z0-9_] 
pattern ='\w+@[a-zA-Z]+\.(com|net|edu|du)'

x = input()
# if re.match(pattern,x,re.IGNORECASE):
if re.match(pattern,x):
# if re.search(pattern,x):
    print('ok')
else:
    print('Not a email')
