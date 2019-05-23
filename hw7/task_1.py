# 1 Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

SIZE = 10
array = [random.randrange(-100, 100) for i in range(SIZE)]

def sort_bubble(array):
    n = len(array)
    spam = True
    while spam:
        spam = False
        for i in range(n - 1):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                spam = True
        print(f'in {array}')

print(array)
sort_bubble(array)
print(array)