
# Get N from the command line
import sys
N= int(sys.argv[1])

# Your code goes here
ctr = 0
a = 0
b = 1
while ctr <= N:
  print(a)
  a, b = b, a + b
  ctr += 1