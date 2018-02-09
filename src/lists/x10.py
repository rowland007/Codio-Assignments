
# Get our input from the command line
import sys
M= int(sys.argv[2])
N= int(sys.argv[3])

# convert strings to integers
numbers= sys.argv[1].split(',')
for i in range(0, len(numbers)):
  numbers[i]= int(numbers[i])

# Your code goes here
result = 0
ctr = N -1

for element in range(0, len(numbers)):
  if ctr == 0:
    ctr = N
    numbers[element] = numbers[element] * M
  ctr -= 1
  
print(numbers)