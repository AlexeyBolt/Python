
import export

def choise():
    try:
        i = int(input('Введите запрос 1 - занесение данных в справочник, 0 - поиск телефона в справочнике: '))
        if type(i) == int:
            if i == 1:
                a = input('Введите имя фамилию город телефон(через пробел): ')
                return (a, 1)
            else:
                b = input("Введите данные для поиска телефона в справочнике(фамилию, имя и(или) город, через пробел:) ")
                return (b, 0)
    except ValueError:
        print("Неверный ввод")

def out_put(list_export : list):
       print(list_export)