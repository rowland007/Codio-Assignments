
# Get the filepath from the command line
import sys
P= sys.argv[1] 
F= sys.argv[2]
L= sys.argv[3]
B= sys.argv[4]

# Your Code Goes Here
recordLength= 16
start= 0
records= []

# Get the file
input = open(P, 'r')
data = input.read()

# use the substring function to read all the records
while( (len(data) - start) >= recordLength):
  record= data[start:start + recordLength]
  records.append(record)
  start+= recordLength
  
input.close()
output = open(P, 'w')

# print out all of our records
for i in range(0,len(records)):
  if record[i] == F:#F,L in record[i]
    replace_record = 0
      # replace_record = replace B
  else:
    replace_record = 0

output.write(str(replace_record))
output.close()