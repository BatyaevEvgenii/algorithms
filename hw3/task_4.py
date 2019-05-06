# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

array = [random.randint(-50, 50) for _ in range(10)]

print(array)

i = 0
max_negative = -1

while i < len(array):
    if array[i] < 0 and max_negative == -1:
        max_negative = i
    elif array[i] < 0 and array[i] > array[max_negative]:
        max_negative = i
    i += 1

print(f'Максимальный отрицательный элемент = {array[max_negative]}, его индекс - {max_negative}')