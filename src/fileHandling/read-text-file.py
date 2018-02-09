
# Load our command line arguments
import sys
P= sys.argv[1]
S= sys.argv[2]

# Create search function
def readTextFile(search, file):
    count = 0
    for line in file:
        if search in line:
            count += 1
    return count


# Open the file in filename for reading
file1 = open(P, 'r')

# Read the entire file into the variable
# data = file1.read()

# Find the string in the file
print(readTextFile(S, file1))

    
file1.close()

