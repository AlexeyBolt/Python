# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет
import os 
os.system('cls')
a = int(input('введите цифру дня недели(от 1 до 7): '))
if 6>a>0 :
    print('это будний(нет)')
elif 8>a>5:
    print('это выходной(да)')
else:
    print('неверный ввод')