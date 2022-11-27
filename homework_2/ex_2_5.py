# Реализуйте алгоритм перемешивания списка

import os 
os.system('cls')
import random   # Призываем рандомайзер
 
sptsok = ['первый элемент ', 'второй элемент ', '3 ', 'Василий ', 'бомж', 'питонист']
random.shuffle(sptsok)
print(f'Проверка 1 {sptsok}')
random.shuffle(sptsok)   
print(f'Проверка 2 {sptsok}')
random.shuffle(sptsok)
print(f'Проверка 3 {sptsok}')
