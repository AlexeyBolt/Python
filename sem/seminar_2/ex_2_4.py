import os 
os.system('cls')

with open('file.txt','r') as f:
    a = f.read().split('\n')
print(a)
