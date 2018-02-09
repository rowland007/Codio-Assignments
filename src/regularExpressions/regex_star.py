import re

pattern='xy*'
str_x='x'
str_xy='xy'
str_xyyyyy='xyyyyy'

m1 = re.match(pattern, str_x)
if m1 != None:
    print(pattern + " matched " + str_x)
else:
    print(pattern + " did not match " + str_x)

m2 = re.match(pattern, str_xy)
if m2 != None:
    print(pattern + " matched " + str_xy)
else:
    print(pattern + " did not match " + str_xy)


m3 = re.match(pattern, str_xyyyyy)
if m3 != None:
    print(pattern + " matched " + str_xyyyyy)
else:
    print(pattern + " did not match " + str_xyyyyy)
