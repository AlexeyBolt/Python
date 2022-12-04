# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 
# (максимальное значение у числа 1.2 ,минимальное у 10.01)

my_list = [float(elements) for elements in input('Введите элементы массива через пробел: ').split()]
new_list = [round(i%1,2) for i in my_list if i%1 != 0]
print(f'Разница между максимальным и минимальным дробным значением равна: {max(new_list) - min(new_list)}')
