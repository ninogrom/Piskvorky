import os
import time
bd = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
c = 1
start = time.time()
def show_board():
    print('   PIŠKVORKY')
    print('     _____')
    print('\n\n   1   2   3 ')
    print(f'a [', bd[0], '] [', bd[1], '] [', bd[2], ']', sep = '')
    print(f'b [', bd[3], '] [', bd[4], '] [', bd[5], ']', sep = '')
    print(f'c [', bd[6], '] [', bd[7], '] [', bd[8], ']', sep = '')
def clear_board():
    command = "'clear'"
    if os.name in ('nt', 'dos'):
        command = "'cls'"
    os.system(command)
def recognition1(x):
    s = 0
    while s == 0:
        if x == 'a1' and bd[0] == ' ':
            bd[0] = 'X'
            s = 1
        elif x == 'a2' and bd[1] == ' ':
            bd[1] = 'X'
            s = 1
        elif x == 'a3' and bd[2] == ' ':
            bd[2] = 'X'
            s = 1
        elif x == 'b1' and bd[3] == ' ':
            bd[3] = 'X'
            s = 1
        elif x == 'b2' and bd[4] == ' ':
            bd[4] = 'X'
            s = 1
        elif x == 'b3' and bd[5] == ' ':
            bd[5] = 'X'
            s = 1
        elif x == 'c1' and bd[6] == ' ':
            bd[6] = 'X'
            s = 1
        elif x == 'c2' and bd[7] == ' ':
            bd[7] = 'X'
            s = 1
        elif x == 'c3' and bd[8] == ' ':
            bd[8] = 'X'
            s = 1
        else:
            clear_board()
            show_board()
            x = input('\n\nZle zadaná hodnota alebo obsadené políčko\nSkús znova: ')
def recognition2(x):
    s = 0
    while s == 0:
        if x == 'a1' and bd[0] == ' ':
            bd[0] = 'O'
            s = 1
        elif x == 'a2' and bd[1] == ' ':
            bd[1] = 'O'
            s = 1
        elif x == 'a3' and bd[2] == ' ':
            bd[2] = 'O'
            s = 1
        elif x == 'b1' and bd[3] == ' ':
            bd[3] = 'O'
            s = 1
        elif x == 'b2' and bd[4] == ' ':
            bd[4] = 'O'
            s = 1
        elif x == 'b3' and bd[5] == ' ':
            bd[5] = 'O'
            s = 1
        elif x == 'c1' and bd[6] == ' ':
            bd[6] = 'O'
            s = 1
        elif x == 'c2' and bd[7] == ' ':
            bd[7] = 'O'
            s = 1
        elif x == 'c3' and bd[8] == ' ':
            bd[8] = 'O'
            s = 1
        else:
            clear_board()
            show_board()
            x = input('\n\nZle zadaná hodnota alebo obsadené políčko\nSkús znova: ')
def win():
    if bd[0] == bd[1] == bd[2] == 'X' or bd[3] == bd[4] == bd[5] == 'X' or bd[6] == bd[7] == bd[8] == 'X' or bd[0] == bd[3] == bd[6] == 'X':
        print('\n\nHráč 1 vyhral')
        end = time.time()
        print(f'Čas hry: ', "{:.2f}".format(end - start), 's', sep = '')
        quit()
    elif bd[1] == bd[4] == bd[7] == 'X' or bd[2] == bd[5] == bd[8] == 'X' or bd[0] == bd[4] == bd[8] == 'X' or bd[2] == bd[4] == bd[6] == 'X':
        print('\n\nHráč 1 vyhral')
        end = time.time()
        print(f'Čas hry: ', "{:.2f}".format(end - start), 's', sep = '')
        quit()
    elif bd[0] == bd[1] == bd[2] == 'O' or bd[3] == bd[4] == bd[5] == 'O' or bd[6] == bd[7] == bd[8] == 'O' or bd[0] == bd[3] == bd[6] == 'O':
        print('\n\nHráč 2 vyhral')
        end = time.time()
        print(f'Čas hry: ', "{:.2f}".format(end - start), 's', sep = '')
        quit()
    elif bd[1] == bd[4] == bd[7] == 'O' or bd[2] == bd[5] == bd[8] == 'O' or bd[0] == bd[4] == bd[8] == 'O' or bd[2] == bd[4] == bd[6] == 'O':
        print('\n\nHráč 2 vyhral')
        end = time.time()
        print(f'Čas hry: ', "{:.2f}".format(end - start), 's', sep = '')
        quit()
    elif ( bd[0] == 'X' or bd[0] == 'O' ) and ( bd[1] == 'X' or bd[1] == 'O' ) and ( bd[2] == 'X' or bd[2] == 'O' ) and ( bd[3] == 'X' or bd[3] == 'O' ) and ( bd[4] == 'X' or bd[4] == 'O' ) and ( bd[5] == 'X' or bd[5] == 'O' ) and ( bd[6] == 'X' or bd[6] == 'O' ) and ( bd[7] == 'X' or bd[7] == 'O' ) and ( bd[8] == 'X' or bd[8] == 'O' ):
        print('\n\n    Remíza')
        end = time.time()
        print(f'Čas hry: ', "{:.2f}".format(end - start), 's', sep = '')
        quit()
    else:
        pass
show_board()
while c == 1:
    move1 = input('\n\nHráč 1: ')
    recognition1(move1)
    clear_board()
    show_board()
    win()
    move2 = input('\n\nHráč 2: ')
    recognition2(move2)
    clear_board()
    show_board()
    win()
