'''
for i in range(num):
    do_smth()

if ______:
    do_smth()
else:
    do_smth_another()
'''
from random import randint  # сгенерировать числа в промежутке
rand_list = []
n = int(input('Сколько чисел нужно? '))

for number in range(n):  # для каждого числа в промежутке n
    rand_list.append(randint(-100, 100))  # добавлять случайное число в список

print(rand_list)

