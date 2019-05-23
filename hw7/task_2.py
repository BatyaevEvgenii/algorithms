# 2 Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

SIZE = 10
array = [round(random.random()*50, 2) for i in range(SIZE)]

def merge(left, right):
    sorted_list = []
    left_index = right_index = 0

    left_length, right_length = len(left), len(right)

    for _ in range(left_length + right_length):
        if left_index < left_length and right_index < right_length:
            if left[left_index] <= right[right_index]:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1

        elif left_index == left_length:
            sorted_list.append(right[right_index])
            right_index += 1
        elif right_index == right_length:
            sorted_list.append(left[left_index])
            left_index += 1

    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    middle = len(nums) // 2

    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])

    return merge(left, right)

print(array)
random_nums = merge_sort(array)
print(random_nums)