
# Get our input from the command line
import sys
text= sys.argv[1]

# Write your code here
def isRed(str):
  found = str.find('red')
  if found >= 0:
    return True
  else:
    return False
  
print(str(isRed(text)))
  