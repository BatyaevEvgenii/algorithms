# 3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.
x1, y1 = map(int, input('Введите, через пробел, целые координаты первой точки: ').split())
x2, y2 = map(int, input('Введите, через пробел, целые координаты второй точки: ').split())

print(f'Координаты первой точки A1({x1}, {y1})')
print(f'Координаты второй точки A2({x2}, {y2})')

k = int((y1 - y2) / (x1 - x2))
b = int(y2 - k * x2)


if k == 0:
    if b ==0:
        print(f'y1 = 0')
    elif b > 0:
        print(f'y2 = {b}')
    else:
        print(f'y3 = {b}')
elif k > 0:
    if (k == 1 and b == 0):
        print(f'y4 = 1')
    elif (k == 1 and b > 0):
        print(f'y5 = {k}*x + {b}')
    else:
        # print(f'y6 = x')
        print(f'y6 = {k}*x {b}')
else:
    if b == 0:
        print(f'y7 = {k}*x')
    elif b > 0:
        print(f'y8 = {k}*x + {b}')
    else:
        print(f'y9 = {k}*x {b}')

