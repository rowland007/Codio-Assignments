
# Get N from the command line
import sys
N = int(sys.argv[1])

# Your code goes here
if N > 0:
  while N > 0:
    print(N)
    N -= 1
else:
  while N < 0:
    print(N)
    N += 1
    