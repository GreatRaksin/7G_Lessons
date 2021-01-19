from random import randint
# randint(a, b) возвращает случайное число в промежутке от a до b

arr = []  # ⬅️ пустой массив
for num in range(10):  # ⬅️ цикл на 10 повторений
    arr.append(randint(-99, 99))  # ⬅️ добавить в массив случайное число

print(f'Получившийся массив {arr}')

i = 0
while i < len(arr) - 1:
    j = 0
    while j < len(arr) - 1 - i:
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
        j += 1
    i += 1

print(f'Отсортированный массив {arr}')