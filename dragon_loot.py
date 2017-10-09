#Dragon Loot
import pprint

def displayInventory(myDict):
    invCount=0
    print('Inventory:')
    for k,v in myDict.items():
        print(str(v) + ' ' + k)
        invCount += v
    print ('Total number of items:' + str(invCount))

def addToInventory(inv, addedItems):
        for i in range(len(addedItems)):
            if addedItems[i] in inv.keys():
                inv[addedItems[i]]+=1
            else:
                inv[addedItems[i]] = 1

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inv, dragonLoot)
displayInventory(inv)
