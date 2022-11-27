# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

import os 
os.system('cls')
import math

n=int(input('введите число, для выявления списка элементов последовательностей: '))
list_posled = []
count = 0
for i in range(1, n+1):
    count=(1+1/i)**i
    list_posled.append((count))

print(f'последовательность (1+1/n)^n для n={n} выглядит так:')
print(list_posled)