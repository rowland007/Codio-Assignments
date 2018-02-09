
# Get the filepath from the command line
import sys
import re
I= sys.argv[1] 
O= sys.argv[2] 
S= sys.argv[3]
T= sys.argv[4]

# Your code goes here
# open our files
input = open(I, 'r')
output = open(O, 'w')

data = input.read()
# replace the string
replace_results = re.sub(S, T, data)

# write the text to the file
output.write(replace_results)

# close the files
input.close()
output.close()
