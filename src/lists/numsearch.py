
# Get our input from the command line
import sys
N= int(sys.argv[2])
# Convert the list of strings into integers
numbers= []
for i in sys.argv[1].split(","):
  if(i.isdigit()):
    numbers.append(int(i))

# numbers now contains the list of integers
index = 0
isFound = False
for index in range(0, len(numbers)):
  if numbers[index] == N:
    print(index)
    isFound = True
    break
  else:
    isFound = False
  index += 1
    
if isFound != True:
  print('-1')
                   
# Write your code below

