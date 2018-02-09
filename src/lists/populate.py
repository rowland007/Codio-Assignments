
# Get N from the command line
import sys
N= int(sys.argv[1])
aList = []

# Your code goes here
if N == 0:
  x = True
else:
  element = 0
  for element in range(0, N):
    aList.append(element * 10)
    element += 1
    
print(aList)