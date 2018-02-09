import re

pattern='a{3}'
str_a_quad='aaaa'
str_a_tripple='aaa'
str_a_tripple_b='aaab'
str_a_double='aa'
str_a_single='a'

m7 = re.match(pattern, str_a_quad)
if m7 != None:
    print("matched %s" % str_a_quad)
else:
    print(pattern + " did not match " + str_a_quad)

m8 = re.match(pattern, str_a_tripple)
if m8 != None:
    print("matched %s" % str_a_tripple)
else:
    print(pattern + " did not match " + str_a_tripple)

m9 = re.match(pattern, str_a_tripple_b)
if m9 != None:
    print("matched %s" % str_a_tripple_b)
else:
    print(pattern + " did not match " + str_a_tripple_b)

m10 = re.match(pattern, str_a_double)
if m10 != None:
    print("matched %s" % str_a_double)
else:
    print(pattern + " did not match " + str_a_double)

m11 = re.match(pattern, str_a_single)
if m11 != None:
    print(m11.group(0))
else:
    print(pattern + " did not match " + str_a_single)
