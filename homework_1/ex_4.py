# Напишите программу, 
# которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
a=int(input('Введите четверть плоскости: '))
if a==1:
    print('Диапазон возможных координат лежит в условиях, при которых x>0 и y>0')
elif a==2:
    print('Диапазон возможных координат лежит в условиях, при которых x<0 и y>0')
elif a==3:
    print('Диапазон возможных координат лежит в условиях, при которых x<0 и y<0')
elif a==4:
    print('Диапазон возможных координат лежит в условиях, при которых x>0 и y<0')
else: print('четвертей всего 4')