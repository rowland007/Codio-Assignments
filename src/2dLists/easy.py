# Get our list from the command line arguments
import sys
list2d= sys.argv[1:]
# Convert the command line arguments into 2d list
for i in range(0,len(list2d)): 
  list2d[i]= list2d[i].split(',')
  
# Write your code below
print(list2d[1][2])