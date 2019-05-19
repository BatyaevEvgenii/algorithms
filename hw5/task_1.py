# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

company = defaultdict(None, {})
n = int(input("Введите количество предприятий: "))

for i in range(n):
    name = input("Введите " + str(i+1) + " предприятие: ")
    first = int(input("Выручка за первый квартал: "))
    second = int(input("Выручка за второй квартал: "))
    third = int(input("Выручка за третий квартал: "))
    fourth = int(input("Выручка за четвертый квартал: "))
    print('*' * 3)
    company[name] = first + second + third + fourth

sum_ = 0
for key, value in company.items():
    sum_ += value

avrg = sum_ / n
print(f'Средняя прибыль у {n} предприятий {avrg} за целый год')

for i in company:
    if company[i] > avrg:
        print(f'Прибыль у {i} выше среднего')
    else:
        print(f'Прибыль у {i} ниже среднего')