# '3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.
import os 
os.system('cls')

# str1=str(input('введите первую строку: '))
# str2=str(input('введите вторую строку: '))
# print(str1.count(str2))
# print(int((len(str1) - len(str1.replace(str2, '')))/len(str2)))

a = input()
b = input()
count = 0
for i in range(len(a)):
    if a[i:i+len(b)] == b:
        count += 1
print(count)
print(a.count(b))
