# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) 
# -2 -1 0 1 2 Позиции: 0,1 -> 2
import os 
os.system('cls')

with open('file.txt','r') as f:    
    a = f.read().split('\n')
print(a)                              # выводим элементы из TXT файла на экран

spisok_elements=[]                    # создаем list
n=int(input('Введите число N: '))           

for i in range (-n,n+1):                # Выводим список элементов от -N до N
    spisok_elements.append((i))         # Выводим список элементов от -N до N
print(spisok_elements)                  # Выводим список элементов от -N до N

print(type(a[0]))                       # Проверка типа данных

res = 1                                 # само решение
for item in a: 
    res *= spisok_elements[int(item)]

print(res)