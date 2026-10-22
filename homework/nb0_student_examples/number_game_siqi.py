x = 1
y = 9
state = 0
bs = 0

while state != 1:

    x1 = x
    y1 = y
    
    print()
    print('-----------the latest picture-----------')
    print()
    print('               Number game')
    
    for i in range(1, 10): #row
        print('----------------------------------------')
        print(i, '|', end = '')
        for j in range(1, 10): #column
            if i + j >= 9:
                if i == y and j == x:
                    if bs == 1:
                        print('FP', '|', end = '') # Start point
                    elif i == 9 and j == 1: 
                        print('SP', '|', end = '') # Final point
                    else:
                        print(' P', '|', end = '') # Player
                elif i == 8 and j == 1:
                    print('  ', ' ', end = '')
                elif i == 1 and j == 9:
                    print(' F', '|', end = '') # Final point
                elif i == 9 and j == 1:
                    print(' S', '|', end = '') # Start point
                else:
                    print('  ', '|', end = '')
            else:
                print('  ', ' ', end = '')
        print()
    print('----------------------------------------')
    
    print()
    print('S = Start point  F = Finish point  P = The place where you are')
    print('You can only go North, East or Northeast.')
    print('(Please read the instruction above the latest picture.)')
    print()

    if bs == 1: # Stop condition
        state = 1
        continue

    direction = str(input('What direction would you like to go? Please enter n, e, or ne.'))
    step = int(input('How many steps would you like to go?'))
    print()
    
    if direction in ('n', 'e', 'ne'):
        if direction == 'n':
            if x == 1 and y == 9:
                print('Error. You went out of the borders.')
                continue
            y1 = y - step
            
        elif direction == 'e':
            x1 = x + step
            
        else:
            if x == 1 and y == 9:
                print('Error. You went out of the borders.')
                continue
            x1 = x + step
            y1 = y - step
        
        if x1 + y1 < 9 or x1 >= 10 or y1 <= 0:
            print('Error. You went out of the borders.')
            
        else:
            x = x1
            y = y1
            if x == 9 and y == 1:
                bs = 1
            
    else:
        print('Error. You can only go North, East or Northeast./ Sorry, I do not understand you.')
        
print('Congratulations, you won.')