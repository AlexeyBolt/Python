# Задача с конфетами

# В идеале, допилить до выбора в меню, с кем играть

import random

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")                        # активировать для игры со своими голосами внутри головы
# player2 = 'Bot'                                                      # активировать для ИИ

value = 117
# value = int(input("Введите количество конфет на столе: "))            # активация изменения количества конфет
flag = random.randint(0,2) 
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        # k=random.randint(0,28)                       # активировать для ИИ
        k = input_dat(player2)                         # активировать для игры со своими голосами внутри головы
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")