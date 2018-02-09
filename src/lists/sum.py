
# Get our list from the command line
import sys
numbers = sys.argv[1].split(",")

# Your code goes here
total = 0
for element in numbers:
  total += int(element)
  
print(str(total))