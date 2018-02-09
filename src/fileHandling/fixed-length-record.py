
# Get the filepath from the command line
import sys
P= sys.argv[1] 
F= sys.argv[2]
L= sys.argv[3]
B= sys.argv[4]

# Your Code Goes Here
record = []
recordList = []
# Get the file
file = open(P, 'r')
data = file.read()
file.close()

# read all the records
while len(data) > 0:
    record.append(data[0:16])
    record.append(data[16:32])
    record.append(data[32:40])
    recordList.append(record)
    data = data[40:]

# Find and replace
output = ''
for i in range(0, len(recordList)):
    thisRecord = recordList[i]
    if thisRecord[0].strip() == F:
        if thisRecord[1].strip() == L:
            thisRecord[2] = B


# print out all of our records
output += thisRecord[0] + thisRecord[1] + thisRecord[2]

file = open(P, 'w')
file.write(output)
file.close()