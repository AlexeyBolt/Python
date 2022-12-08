# 4'. Задана натуральная степень k. Сформировать 
# случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.(записать в строку)
# Пример:
# k=2 => 2*x^2 + 4*x + 5 или x^2 + 5 или 10*x**2
# k=3 => 2*x^3 + 4*x^2 + 4*x + 5

import os 
os.system('cls')
import random

k = int(input("Введите натуральную степень: "))
ratio = []
for i in range(k + 1):
    ratio.append(random.randint(0, 100))


def create_polynomial(some_list):
    result = ""
    if len(some_list) < 1:
        result = "x = 0"
    else:
        for i in range(len(some_list)):
            if i != len(some_list) - 1 and some_list[i] != 0 and i != len(some_list) - 2:
                result += f"{some_list[i]}x^{len(some_list) - i - 1}"
                if some_list[i + 1] != 0:
                    result += " + "
            elif i == len(some_list) - 2 and some_list[i] != 0:
                result += f"{some_list[i]}x"
                if some_list[i + 1] != 0:
                    result += " + "
            elif i == len(some_list) - 1 and some_list[i] != 0:
                result += f"{some_list[i]} = 0"
            elif i == len(some_list) - 1 and some_list[i] == 0:
                result += " = 0"
    return result


def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)


write_file("file.txt", create_polynomial(ratio))
print("Уравнение записано в файл!")