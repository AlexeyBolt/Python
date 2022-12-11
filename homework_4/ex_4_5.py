# Даны два файла, в каждом из которых находится 
# запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

import os 
os.system('cls')
import sympy
import random

def polin_wr(name_file):
    k = int(input('Введите степень: '))
    koef = [str(random.randint(0, 100)) for i in range(k + 1)]
    polin = ''
    for i in range(k + 1):
        if i == 0: polin = koef[i]
        elif i ==1: polin = f'{koef[i]}*x + {polin}'
        else: polin =  f'{koef[i]}*x**{i} + {polin}'
    with open(name_file, 'w') as f:
        f.write(polin) 

polin_wr('f_1.txt')
polin_wr('f_2.txt')

with open('f_1.txt', 'r') as f1, open('f_2.txt', 'r') as f2,\
    open('f_rez.txt', 'w') as frez:

    p1 = f1.read()
    p2 = f2.read() 

    x = sympy.Symbol('x')

    rez = sympy.simplify(eval(p1) + eval(p2))

    frez.write(str(rez))