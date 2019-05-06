# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

nums = list(range(2, 100))
print(nums)

for i in range(2, 10):
    count = 0
    for item in nums:
        if item % i == 0:
            count += 1
    print(f'Числу {i} - кратны {count} цифр(-ы, -а)')
