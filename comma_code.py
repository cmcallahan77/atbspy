#Comma code

def myListBreaker(myList):
    myString = ''
    for i in range(len(myList)-1):
            myString += (str(myList[i]) + ',')
    myString += 'and ' + str(myList[-1])
    print(myString)

newList = [1, 'two', 3, 'four']
myListBreaker(newList)
