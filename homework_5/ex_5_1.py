# Крестики-нолики/ самое тупое решение

pole = [['-','-','-'],['-','-','-'],['-','-','-']]
print(*pole,sep='\n')
for k in range(9):
    i = int(input('Введите новер строки(начиная с 0): '))
    j = int(input('Введите новер столбца(начиная с 0): '))
    if pole[i][j] != '-':
        print('Занято!')
    else:
        pole[i][j] = input('Введите x или o: ')
        if (pole[0][0] == pole[0][1] == pole[0][2] != '-' or
            pole[1][0] == pole[1][1] == pole[1][2] != '-' or
            pole[2][0] == pole[2][1] == pole[2][2] != '-' or
            pole[0][0] == pole[1][1] == pole[2][2] != '-' or
            pole[2][0] == pole[1][1] == pole[0][2] != '-'):
                if pole[i][j] == 'x':
                    print('X победили!!!')
                else: print('О победили!!!')

    print(*pole, sep='\n')