# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

xyz = int(input('Введите положительное трехзначное число: '))

# первый вариант
# number = list(map(int, str(xyz)))
#
# x = number[0]
# y = number[1]
# z = number[2]

# второй варант
x = xyz // 100
y = xyz % 100 // 10
z = xyz % 10

sum = x + y + z
mult = x * y * z

print(f'Сумма введенных чисел x = {x}, y = {y}, z = {z}, равна {sum}')
print(f'Произведение введенных чисел x = {x}, y = {y}, z = {z}, равно {mult}')




# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.



# 4. Написать программу, которая генерирует в указанных пользователем границах: ● случайное целое число, ● случайное вещественное число, ● случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.



