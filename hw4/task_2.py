# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и
# возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

# import cProfile

def simple(x):
    for i in range(2, x):
        if x % i == 0:
            return x
    return x
    # print(f'{x}, - простое')


def simple_x(x):
    array_1 = []
    for i in range(2, x):
        simple(i)
        array_1.append(i)
    return array_1

# "task_2.simple_x(10)"
# 1000 loops, best of 5: 3.62 usec per loop
# "task_2.simple_x(100)"
# 1000 loops, best of 5: 79.1 usec per loop
# "task_2.simple_x(1000)"
# 1000 loops, best of 5: 4.06 msec per loop

# cProfile.run('simple_x(1000)')

# 1    0.000    0.000    0.000    0.000 task_2.py:14(simple_x)
# 8    0.000    0.000    0.000    0.000 task_2.py:6(simple)

#  1    0.000    0.000    0.000    0.000 task_2.py:14(simple_x)
# 98    0.000    0.000    0.000    0.000 task_2.py:6(simple)

#   1    0.000    0.000    0.007    0.007 task_2.py:14(simple_x)
# 998    0.006    0.000    0.006    0.000 task_2.py:6(simple)


#
#
# sieve = [i for i in range(10000)]
# sieve[1] = 0
#
# for i in range(2, 10000):
#     if sieve[i] != 0:
#         j = i + i
#         while j < 10000:
#             sieve[j] = 0
#             j += i
# # print(sieve)
# result = [i for i in sieve if i != 0]
#
# print(result)

# "task_2"
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 100 loops, best of 5: 18.1 nsec per loop

# Возможно ли такое, что более "сложный" алгоритм работает быстрее?

