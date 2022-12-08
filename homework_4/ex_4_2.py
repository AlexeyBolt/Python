# 2'. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# * 6 -> [2,3]
# * 144 -> [2,3]

import os 
os.system('cls')

num = int(input("Введите число: "))
i = 2 
lst = []
numb_n = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
lst = list(set(lst))  
lst.sort()      
print(f"Простые множители числа {numb_n} приведены в списке: {lst}")



# Решение от преподавателя
# def dividers(a: int, uniq: bool = False) -> list[int]:
#     """"Возвращает список простых делителей числа.
#     uniq = True вернет список уникальных делителей"""
#     i = 2
#     dividers = []
#     while a != 1:
#         while a % i == 0:
#             dividers.append(i)
#             a //= i
#         i += 1
#     if uniq:
#         return list(set(dividers))
#     else:
#         return dividers


# a = 81
# print(f'Список натуральных делителей числа {a}:{dividers(a)}')
# print(f'Список уникальных делителей числа {a}:{dividers(a, True)}')

# Через функции
def Factor(n):
    Ans=[]
    d=2
    while d*d<=n:
        if n%d==0:
            Ans.append(d)
            n//=d
        else:
            d+=1
    if n>1:
        Ans.append(n)
    return Ans
print(Factor(int(input(' А теперь затестим более глубокое погружение на распил. Введи число, пытливый ум : '))))