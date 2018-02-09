# Get N from the command line
import sys
import math
N= int(sys.argv[1])

# Your code goes here
ctr = 0
total = 0

while ctr <= N:
  total += math.pow(ctr,2)
  ctr += 1
  
print(int(total))
