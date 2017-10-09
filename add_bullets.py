#Password Locker
import sys,pyperclip


myList = pyperclip.paste()

print(myList)

myLines = myList.split('\n')
myString=''
for i in range(len(myLines)):
    myString += '* ' + myLines[i] + '\n'
pyperclip.copy(myString)
