
aNumber = 8             # set a number variable

aString = str(aNumber)  # this way will work
#aString = aNumber       # this way will fail

result = 'a string combined with the number: ' + aString
print(result)


# or use it directly in another statement
aNumber = 8
print('a string combined with the number: ' + str(aNumber) + aString + \n + result)
