import re

#The string to search for the regular expression occurrence (This is provided to the student)
search_string='''This is a string to search for a regular expression like regular expression or 
regular-expression or regular:expression or regular&expression'''

#1.  Write a regular expression that will find all occurrances of:
#    a.  regular expression
#    b.  regular-expression
#    c.  regular:expression
#    d.  regular&expression
#    in search_string
#2.  Assign the regular expression to a variable named pattern
pattern="regular[-_=&:]expression"
#The string to use for substitution (This is provided to the student)

substitution="regular expression"

#3.  Using the sub() method from the re package substitute all occurrences of the 'pattern' with 'substitution'
#4.   Assign the outcome of the sub() method to a variable called replace_result
replace_results = re.sub(pattern, substitution, search_string)
#5.  Output to the console replace_results
print(replace_results)
