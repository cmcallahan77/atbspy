#Strong Password Detection

#Write a function that uses regular expressions
#to make sure the password string it is passed is strong.
#A strong password is defined as one that is at least
#eight characters long, contains both uppercase and
#lowercase characters, and has at least one digit.
#You may need to test the string against
#multiple regex patterns to validate its strength.

import re

uppercaseRegex = re.compile(r'''(
    [A-Z]+               # username
    )''', re.VERBOSE)

lowercaseRegex = re.compile(r'''(
    [a-z]+               # username
    )''', re.VERBOSE)

numRegex= re.compile(r'''(
    [0-9]+               # username
    )''', re.VERBOSE)



print('Please enter your password:')
password = input()
if len(password) < 8:
    print('Minimum Password length is 8')
elif uppercaseRegex.search(password) == None:
    print ('Password must contain at least 1 uppercase')
elif lowercaseRegex.search(password) == None:
    print ('Password must contain at least 1 lowercase')
elif numRegex.search(password) == None:
    print ('Password must contain at least 1 number')
else:
    print ("Good Password!")
