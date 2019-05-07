# 8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []

for i in range(5):
    array = [int(input(f'{j} элемент {i} массива ')) for j in range(3)]
    matrix.append(array)
    for line in matrix:
        sum_line = 0
        for item in line:
            sum_line += item
    line.append(sum_line)

for line in matrix:
    print(line)



