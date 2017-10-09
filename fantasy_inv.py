#Fantasy Inventory

def displayInventory(myDict):
    invCount=0
    print('Inventory:')
    for k,v in myDict.items():
        print(str(v) + ' ' + k)
        invCount += v
    print ('Total number of items:' + str(invCount))


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)
