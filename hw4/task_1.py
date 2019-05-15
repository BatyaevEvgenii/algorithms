# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# number = list(map(int, str(input('Введите число: '))))
# number = str(input('Введите число: '))

import cProfile

def index_xyz():
    # number = list(map(int, str(input('Введите число: '))))
    number = [1, 2, 3]
    x = number[0]
    y = number[1]
    z = number[2]
    sum_xyz = x + y + z
    mult_xyz = x * y * z
    return sum_xyz, mult_xyz

# 100 loops, best of 5: 346 nsec per loop


def add_variable():
    # number = list(map(int, str(input('Введите число: '))))
    number = int(123)
    x = number // 100
    y = number % 100 // 10
    z = number % 10
    sum_xyz = x + y + z
    mult_xyz = x * y * z
    return sum_xyz, mult_xyz

# 100 loops, best of 5: 417 nsec per loop


def num_for():
    # number = list(map(int, str(input('Введите число: '))))
    number = [1, 2, 3]
    sum_ = 0
    mult_ = 1
    for i in number:
        sum_ += int(i)
        mult_ *= int(i)

    return sum_, mult_

# 100 loops, best of 5: 1.05 usec per loop


cProfile.run('num_for()')

# исходя из полученнных данных, можно сделать вывод: использование цикла ведет к уменьшению времени выполнения
# программы для подсчета простых арифметических действий