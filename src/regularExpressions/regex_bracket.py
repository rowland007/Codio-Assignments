import re

pattern="[abc]"

a_str="a"
b_str="b"
c_str="c"

ab_str="ab"
bc_str="bc"
abc_str="abc"
xabc_str="xabc"

match1 = re.match(pattern, a_str)
if match1 != None:
    print(pattern + " matched " + a_str)
else:
    print(pattern + " did not match " + a_str)

match2 = re.match(pattern, b_str)
if match2 != None:
    print(pattern + " matched " + b_str)
else:
    print(pattern + " did not match " + b_str)

match3 = re.match(pattern, c_str)
if match3 != None:
    print(pattern + " matched " + c_str)
else:
    print(pattern + " did not match " + c_str)

match4 = re.match(pattern, ab_str)
if match4 != None:
    print(pattern + " matched " + ab_str)
else:
    print(pattern + " did not match " + ab_str)

match5 = re.match(pattern, bc_str)
if match5 != None:
    print(pattern + " matched " + bc_str)
else:
    print(pattern + " did not match " + bc_str)

match6 = re.match(pattern, abc_str)
if match6 != None:
    print(pattern + " matched " + abc_str)
else:
    print(pattern + " did not match " + abc_str)

match7 = re.match(pattern, xabc_str)
if match7 != None:
    print(pattern + " matched " + xabc_str)
else:
    print(pattern + " did not match " + xabc_str)