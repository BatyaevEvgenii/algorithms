# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

FIRST = 32
LAST = 127

for i in range(FIRST, LAST + 1):
    print(f' {i} - {chr(i)}', end="")
    if i % 10 == 1:
        print('')