# 8. Определить, является ли год, который ввел пользователь, високосным или не високосным.

year = int(input('Введите год: '))

if year % 400 == 0:
    print(f'{year} високосный')
elif year % 4 == 0:
    # print(f'{year} високосный')
    if year % 100 == 0:
        print(f'{year} НЕвисокосный')
    else:
        print(f'{year} високосный')
else:
    print(f'{year} НЕвисокосный')