# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

array = [random.randint(0, 100) for _ in range(10)]
print(f'Исходный массив чисел {array}')
max_array = array[0]
min_array = array[0]

for i in range(1, len(array)):
    if array[i] > max_array:
        max_array = array[i]
print(f'Максимальное число в массиве {max_array}, индекс этого числа {array.index(max_array)}')

for j in range(1, len(array)):
    if array[j] < min_array:
        min_array = array[j]
print(f'Минимальное число в массиве {min_array}, индекс этого числа {array.index(min_array)}')

i = array.index(max_array)
j = array.index(min_array)

if i > j:
    array[i], array[j] = array[j], array[i]
else:
    array[j], array[i] = array[i], array[j]

print(f'Измененный массив {array}')
