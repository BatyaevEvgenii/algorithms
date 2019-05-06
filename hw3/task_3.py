# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

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
array_2 = []

if i > j:
    array_2 = array[(j+1):i]
else:
    array_2 = array[(i+1):j]

sum_ = 0
for item in array_2:
    sum_ += item

print(f'Массив элементов между {max_array} и {min_array} - {array_2}')
print(f'Сумма элементов этого массива {sum_}')