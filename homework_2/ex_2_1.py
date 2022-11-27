# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

import os 
os.system('cls')
# import math


a_list = list(input("Введите число: "))

if a_list.count(',')>0:
    a_list.remove(',')

# print(a_list) проверка
a_list = map(int,a_list)
sumOfElements=sum(a_list)

print("сумма элементов числа = ", sumOfElements)