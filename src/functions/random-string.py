
# Get our arguments from the command line
import sys
character= sys.argv[1]
count= int(sys.argv[2])

# Your code goes here
def generateString(char, val):
  str = char
  for ctr in range(1, val):
    str += char
    ctr += 1
  return str

print(generateString(character, count))
