# введите 5 чисел и выведете на экран максимальное

# мой вариант решения
# list = [input('Введите число : ') for _ in range(5)]
# max_number = max(list)
# print(f'Максимальное число массива {list} является {max_number}')

# Вариант решения в группе
a = input().split()
print(a)
max_numbers = int(a[0])
for i in range(len(a)):
#или
# for i in range(5): 
    if int(a[i]) > max_numbers:
        max_numbers = int(a[i])
print(max_numbers)