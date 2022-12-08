# 3'. Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

import os 
os.system('cls')

import random

lst = [random.randint(0, 6) for i in range(11)]
print(lst)
def return_unique(lst):
    result = []
    count = 0
    for i in range (0, len(lst)):
        for j in range (0, len(lst)):
            if lst[i] == lst[j]:
                count += 1
        if count < 2:
            result.append(lst[i]) 
        count = 0  
        j = 0   
    return result  
print(f"Список из неповторяющихся элементов: {return_unique(lst)}")