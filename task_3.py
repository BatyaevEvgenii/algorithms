# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
x = int(input('Первое число: '))
y = int(input('Второе число: '))
z = int(input('Третье число: '))

if x > y:
    if y > z:
        print(f'среднее значение1 y = {y}')
    elif x > z:
        print(f'Среднее значение2 z = {z}')
    else:
        print(f'Среднее значение3 x = {x}')
else:
    if y < z:
        print(f'Среднее значение4 y = {y}')
    elif x > z:
        print(f'Среднее значение5 x = {x}')
    else:
        print(f'Среднее значение6 z = {z}')