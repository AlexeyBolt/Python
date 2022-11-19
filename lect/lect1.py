#a = "hello "
#b = "World"
#print(a+b)
# username = input('Введи имя, бедолага: ')
#  if (username == 'Маша'):
#      print ('Маша, раздевайся!')
#  else:
#      print ("Нахер Машу, привет ", username);


# a=int(input("Введи число А: "))
# b=int(input("Введи число B: "))
# print(b+a)
# print(b*a)
# print(b**a)
koloda = [6,7,8,9,10,2,3,4,11] * 4
import random
random.shuffle(koloda)
print('Поиграем в очко?')
count = 0

while True:
    choice = input('Будете брать карту? y/n\n')
    if choice == 'y':
        current = koloda.pop()
        print('Вам попалась карта достоинством %d' %current)
        count += current
        if count > 21:
            print('Извините, но вы проиграли')
            break
        elif count == 21:
            print('Поздравляю, вы набрали 21!')
            break
        else:
            print('У вас %d очков.' %count)
    elif choice == 'n':
        print('У вас %d очков и вы закончили игру.' %count)
        break

print('До новых встреч!')