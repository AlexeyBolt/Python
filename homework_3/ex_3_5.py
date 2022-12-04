# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов. (Дополнительное)


# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def Fibo(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)

def NegaFibo(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

n = int(input('Введите любое число: '))
mirror_fibo = []
for elem in range(1, n + 1):
    mirror_fibo.append(Fibo(elem))
    mirror_fibo.insert(0, NegaFibo(elem))
print(mirror_fibo)