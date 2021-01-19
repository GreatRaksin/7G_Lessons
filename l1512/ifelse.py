rand_list = []
n = int(input('Сколько чисел нужно? '))

for number in range(n):  # для каждого числа в промежутке n
    if number % 3 == 0 or number % 5 == 0:
        rand_list.append(number)  # добавлять случайное число в список
    else:
        rand_list.append('!!!')

print(rand_list)