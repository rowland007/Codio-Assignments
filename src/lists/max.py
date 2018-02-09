
# Get our numbers from the command line
import sys
numbers= sys.argv[1].split(',')
numbers= [int(i) for i in numbers]

# Your code goes here
index = 0
maxVal = 0
maxIndex = index

for index in range(0, len(numbers)):
  if numbers[index] > maxVal:
    maxVal = numbers[index]
    maxIndex = index
    
print(maxIndex)