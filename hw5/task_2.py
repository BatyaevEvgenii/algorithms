# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import defaultdict

dec_hex = defaultdict(None, {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
     10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})

hex_1 = list(map(str, str(input('Введите число: ').upper())))
hex_2 = list(map(str, str(input('Введите число: ').upper())))

if len(hex_1) < len(hex_2):
    hex_1.insert(0, '0')
else:
    hex_2.insert(0, '0')

dec_1 = []
for k in hex_1:
    for i, j in dec_hex.items():
        if k == j:
            dec_1.append(i)
dec_1.reverse()

sum_dec_1 = 0
for i in dec_1:
    sum_dec_1 += i * (16 ** dec_1.index(i))

dec_2 = []
for k in hex_2:
    for i, j in dec_hex.items():
        if k == j:
            dec_2.append(i)
dec_2.reverse()

sum_dec_2 = 0
for i in dec_2:
    sum_dec_2 += i * (16 ** dec_2.index(i))

sum_dec = sum_dec_1 + sum_dec_2
mult_dec = sum_dec_1 * sum_dec_2

hex_1_2 = ''
hex_1x2 = ''

while sum_dec != 0:
    item = sum_dec % 16
    sum_dec //= 16
    hex_1_2 += dec_hex[item]

hex_1_2 = ''.join(reversed(hex_1_2))
print(f'Сумма чисел {hex_1} и {hex_2} равна {hex_1_2}')

while mult_dec != 0:
    item = mult_dec % 16
    mult_dec //= 16
    hex_1x2 += dec_hex[item]

hex_1x2 = ''.join(reversed(hex_1x2))
print(f'Произведение чисел {hex_1} и {hex_2} равно {hex_1x2}')
