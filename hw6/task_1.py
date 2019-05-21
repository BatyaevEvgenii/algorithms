import sys
import ctypes
import struct



# 8. Определить, является ли год, который ввел пользователь, високосным или не високосным.

# year = int(input('Введите год: '))
#
# if year % 400 == 0:
#     print(f'{year} високосный')
# elif year % 4 == 0:
#     if year % 100 == 0:
#         print(f'{year} НЕвисокосный')
#     else:
#         print(f'{year} високосный')
# else:
#     print(f'{year} НЕвисокосный')

# print(id(year))
# print(sys.getrefcount(year))
# print(sys.getsizeof(year))

# Введите год: 2000
# 2000 високосный
# 4413235120
# 2
# 28
#  type=<class 'int'>, size=28, obj=2000



# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

# import random
#
# array = [random.randint(0, 100) for _ in range(10)]
# print(f'Исходный массив чисел {array}')
# max_array = array[0]
# min_array = array[0]
#
# for i in range(1, len(array)):
#     if array[i] > max_array:
#         max_array = array[i]
# print(f'Максимальное число в массиве {max_array}, индекс этого числа {array.index(max_array)}')
#
# for j in range(1, len(array)):
#     if array[j] < min_array:
#         min_array = array[j]
# print(f'Минимальное число в массиве {min_array}, индекс этого числа {array.index(min_array)}')
# i = array.index(max_array)
# j = array.index(min_array)
# array_2 = []
#
# if i > j:
#     array_2 = array[(j+1):i]
# else:
#     array_2 = array[(i+1):j]
#
# sum_ = 0
# for item in array_2:
#     sum_ += item
#
# print(f'Массив элементов между {max_array} и {min_array} - {array_2}')
# print(f'Сумма элементов этого массива {sum_}')

# print(id(array))
# print(sys.getrefcount(array))
# print(sys.getsizeof(array))
# print(id(max_array))
# print(sys.getrefcount(max_array))
# print(sys.getsizeof(max_array))
# print(id(min_array))
# print(sys.getrefcount(min_array))
# print(sys.getsizeof(min_array))

# Исходный массив чисел [58, 35, 16, 38, 88, 88, 27, 8, 19, 73]
# Максимальное число в массиве 88, индекс этого числа 4
# Минимальное число в массиве 8, индекс этого числа 7
# 4374082248
# 2
# 192
# 4371273440
# 6
# 28
# 4371270880
# 48
# 28
#  type=<class 'list'>, size=192, obj=[58, 35, 16, 38, 88, 88, 27, 8, 19, 73]
# 	 type=<class 'int'>, size=28, obj=58
# 	 type=<class 'int'>, size=28, obj=35
# 	 type=<class 'int'>, size=28, obj=16
# 	 type=<class 'int'>, size=28, obj=38
# 	 type=<class 'int'>, size=28, obj=88
# 	 type=<class 'int'>, size=28, obj=88
# 	 type=<class 'int'>, size=28, obj=27
# 	 type=<class 'int'>, size=28, obj=8
# 	 type=<class 'int'>, size=28, obj=19
# 	 type=<class 'int'>, size=28, obj=73


# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# matrix = []
#
# for i in range(5):
#     array = [int(input(f'Введите {j} элемент {i} массива: ')) for j in range(3)]
#     matrix.append(array)
#
# for line in matrix:
#     sum_line = 0
#     for item in line:
#         sum_line += item
#     line.append(sum_line)
#
# for line in matrix:
#     print(line)



# print(id(matrix))
# print(sys.getrefcount(matrix))
# print(sys.getsizeof(matrix))
# Введите 0 элемент 0 массива: 1
# Введите 1 элемент 0 массива: 1
# Введите 2 элемент 0 массива: 1
# Введите 0 элемент 1 массива: 1
# Введите 1 элемент 1 массива: 2
# Введите 2 элемент 1 массива: 2
# Введите 0 элемент 2 массива: 2
# Введите 1 элемент 2 массива: 2
# Введите 2 элемент 2 массива: 3
# Введите 0 элемент 3 массива: 3
# Введите 1 элемент 3 массива: 3
# Введите 2 элемент 3 массива: 3
# Введите 0 элемент 4 массива: 4
# Введите 1 элемент 4 массива: 4
# Введите 2 элемент 4 массива: 4
# [1, 1, 1, 3]
# [1, 2, 2, 5]
# [2, 2, 3, 7]
# [3, 3, 3, 9]
# [4, 4, 4, 12]
# 4479672648
# 2
# 128
#  type=<class 'list'>, size=128, obj=[[1, 1, 1, 3], [1, 2, 2, 5], [2, 2, 3, 7], [3, 3, 3, 9], [4, 4, 4, 12]]
# 	 type=<class 'list'>, size=96, obj=[1, 1, 1, 3]
# 		 type=<class 'int'>, size=28, obj=1
# 		 type=<class 'int'>, size=28, obj=1
# 		 type=<class 'int'>, size=28, obj=1
# 		 type=<class 'int'>, size=28, obj=3
# 	 type=<class 'list'>, size=96, obj=[1, 2, 2, 5]
# 		 type=<class 'int'>, size=28, obj=1
# 		 type=<class 'int'>, size=28, obj=2
# 		 type=<class 'int'>, size=28, obj=2
# 		 type=<class 'int'>, size=28, obj=5
# 	 type=<class 'list'>, size=96, obj=[2, 2, 3, 7]
# 		 type=<class 'int'>, size=28, obj=2
# 		 type=<class 'int'>, size=28, obj=2
# 		 type=<class 'int'>, size=28, obj=3
# 		 type=<class 'int'>, size=28, obj=7
# 	 type=<class 'list'>, size=96, obj=[3, 3, 3, 9]
# 		 type=<class 'int'>, size=28, obj=3
# 		 type=<class 'int'>, size=28, obj=3
# 		 type=<class 'int'>, size=28, obj=3
# 		 type=<class 'int'>, size=28, obj=9
# 	 type=<class 'list'>, size=96, obj=[4, 4, 4, 12]
# 		 type=<class 'int'>, size=28, obj=4
# 		 type=<class 'int'>, size=28, obj=4
# 		 type=<class 'int'>, size=28, obj=4
# 		 type=<class 'int'>, size=28, obj=12


def show_size(x, level=0):
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)


# show_size(year)
# show_size(array)
# show_size(max_array)
# show_size(min_array)
# show_size(matrix)


# Все замеры производились на macOS Mojave, 64-bit
# Массивы ресурсоемкие объекты.
# В связи с чем могу предположить что нужно более грамотно подходить к алгоритмам их обработки.