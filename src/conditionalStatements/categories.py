# Get the age from the command line
import sys
age= int(sys.argv[1])

# Your code goes here
if(age > 18 or age < 6):
  print('NA')
else:
  print('primary school' if (age > 5 and age < 12) else 'secondary school')