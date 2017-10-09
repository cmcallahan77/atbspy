#Collatz sequence

def collatz(num):
    if int(num) % 2 == 0:
        print(int(num)//2)
        return int(num)//2
    elif int(num) % 2 == 1:
        print((int(num) * 3) + 1)
        return (int(num) * 3) + 1
retNum = 0

while retNum != 1:
    try:
        print('Enter a number:')
        myNum = input()
        retNum = collatz(myNum)
    except ValueError:
        print('Exception: Value is not an integer!')
