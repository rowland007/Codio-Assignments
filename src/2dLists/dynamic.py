
# Get our arguments from the command line
import sys
A= int(sys.argv[1])
B= int(sys.argv[2])
list = []

# Your code goes here
for x in range(0, A - 1):
  for y in range(0, B - 1):
    list[x][y] = 'R' + str(x) + 'C' + str(y)

    
for x in range(0, A - 1):
  for y in range(0, B - 1):
    print(list[x][y])
