# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81

import os 
os.system('cls')

import math

n = int(input('Введите число: '))
for x in range(n):
    print(int(math.pow(-3, x)))

