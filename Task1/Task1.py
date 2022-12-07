# Вычислить число Пи c заданной точностью d
# Пример: 
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415  

import os

from math import pi

os.system('cls')

print('Найдем число π с заданной точностью до знака после запятой.')

print()

d = input('Введите точность вывода числа π в виде 0.1 или 0.01 и так далее: ')

h = 0

b = list()

for x in str(pi):
    h += 1
    b.append(x)
    
    if h == len(d):
        break

h = ''.join(b)

print()

print(f'Число π с округлением до {d} равно: {h}.')