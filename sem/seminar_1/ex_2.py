# Напишите программу, которая при введении 2х чисел проверяет является ли одно число квадратом другого
# print('Введите первое число: ')
a = int(input('Введите первое число: '))
# print('а теперь введите второе число ')
b = int(input('а теперь введите второе число ')) # прикольный способ избавления от строчки Print в копилку))
if (b == a*a):
     print (f'число {b} является квадратом числа {a}')
elif (a == b*b): 
     print (f'число {a} является квадратом числа {b}')
else:
     print (f"числа {a} и {b} не являются квадратами друг друга")

