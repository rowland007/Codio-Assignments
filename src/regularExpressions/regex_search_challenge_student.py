import re
#The string to search for the regular expression occurrence (This is provided to the student)

search_string='''This is a string to search for a regular expression like regular expression or 
regular-expression or regular:expression or regular&expression'''

#1.  Write a regular expression that will find all occurrences of:
#    a.  regular expression
#    b.  regular-expression
#    c.  regular:expression
#    d.  regular&expression
#    in search_string
#2.  Assign the regular expression to a variable named pattern
pattern = 'regular?expression'

#1.  Using the findall() method from the re package determine if there are occurrences in search_string
#.   Assign the outcome of the findall() method to a variable called match1
#2.  If match1 is not None:
#    a.  Print to the console the pattern used to perform the match, followed by the word 'matched'
#3.  Otherwise:
#    a.  Print to the console the pattern used to perform the match, followed by the words 'did not match'

match1 = re.findall(pattern, search_string)
if match1 != None:
  print(pattern + " matched")
else:
  print(pattern + " did not match")