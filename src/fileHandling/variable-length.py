
# Get the filepath from the command line
import sys
P= sys.argv[1] 
F= sys.argv[2]
L= sys.argv[3]
B= sys.argv[4]

# ----------------------------------------------------------------
# 
# Our Helper functions:
# 
# ----------------------------------------------------------------

#
# Loads the file at filepath 
# Returns a 2d array with the data
#


def load2dArrayFromFile(filepath):
    # Your code goes here:
    file = open(filepath, 'r')
    data = file.read()
    lines = data.split("\n")
    for x in range(0, len(lines)):
        lines[x] = lines[x].split("|")
    return data


#
# Searches the 2d array 'records' for firstname, lastname.
# Returns the index of the record or -1 if no record exists
# 
def findIndex(records, firstname, lastname):
    # Your code goes here:
    for row in records:
        if firstname == records[row][0]:
            if lastname == records[row][1]:
                return row
        else:
            return -1
# Sets the birthday of the record at the given index
# Returns: nothing


def setBirthday(records, index, newBirthday):
    # Your code goes here:
    if index == -1:
      return -1
    else:
      records[index][2] = newBirthday
# Convert the 2d array back into a string
# Return the text of the 2d array


def makeTextFrom2dArray(records):
    # Your code goes here:
    for x in range(0, len(records)):
        records[x] = "|".join(records[x])
    return "\n".join(records)
# ----------------------------------------------------------------
# 
#  Our main code body, where we call our functions.
#  
# ----------------------------------------------------------------

# Load our records from the file into a 2d array
records= load2dArrayFromFile(P)

# Find out which index, if any, has the name we are hunting
indexWeAreHunting= findIndex(records, F, L)

# Set the birthday record to the one we were passed
setBirthday(records, indexWeAreHunting, B)

# Convert the records into a text string
output= makeTextFrom2dArray(records)

# Your code goes here
# write the text string out to the file
file = open(P, 'w')
file.write(output)
file.close()