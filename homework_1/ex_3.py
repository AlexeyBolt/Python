# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт 
# номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
import os 
os.system('cls')

x=int(input('Введите координату X: '))
y=int(input('Введите координату Y: '))
if x>0 and y>0:
    print('точка находится в 1 четверти')
elif x<0 and y>0:
    print('точка находится во 2 четверти')
elif x<0 and y<0:
    print('точка находится в 3 четверти')
elif x>0 and y<0:
    print('точка находится в 4 четверти')
else: print('точка не относится к конкретной четверти')
