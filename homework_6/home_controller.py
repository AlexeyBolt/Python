import os 
os.system('cls')
import ex_6_1
import ex_6_2
import ex_6_3
import home_view

def run():
    while True:
        mode = home_view.choose
        if mode =='1':
        run(os.system('./ex_6_1.py'))
        elif mode =='2' : 
        os.system('./ex_6_2.py')
        else mode =='3':
        os.system('./ex_6_3.py')

