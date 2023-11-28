nigga = ['delta ','alfa ','beta ','gamma ','shtrix '] *100
import random
random.shuffle(nigga)
print('осел')
maxys = ''

while True:
    choice = input('y/n\n')
    if choice == 'y':
        current = nigga.pop()
        maxys += current
        print(current)
    elif choice == 'n':
        maxys += 'shtrix '
        print(maxys)
        break