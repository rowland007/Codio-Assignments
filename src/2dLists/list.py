# Get our list from the command line arguments
import sys
numbers = sys.argv[1:]

# Convert the command line arguments into 2d list
for i in range(0,len(numbers)): 
  numbers[i]= numbers[i].split(',')
  
# Write your code below
total = 0

# We work through the rows first, dimension 1
for x in range(0, len(numbers)):
  rowVal = 0
  for y in range(0, len(numbers[0])):
    rowVal += int(numbers[x][y])
    y += 1
  print(rowVal)
  total += rowVal
  x += 1

print(total)