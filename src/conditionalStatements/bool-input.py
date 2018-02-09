
# Get our boolean values from the command line
import sys
isCold= sys.argv[1]
isRainy= sys.argv[2]

# Your code goes here
print(('cold' if isCold=='True' else 'warm') + ' and ' + ('rainy' if isRainy=='True' else 'dry'))