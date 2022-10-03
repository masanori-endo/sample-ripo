import random

def bogo_sort(numbers):
    len_numbers = len(numbers) - 1
    i = 0
    while i < len_numbers:
        if numbers[i] > numbers[i+1]:
            random.shuffle(numbers)
            i = 0
        else:
            i += 1
    return numbers        


def bubble_sort(numbers):
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 -i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers






nums = [random.randint(0, 100) for _ in range(100)]
# print(bogo_sort(nums))
result = bubble_sort(nums)
# print(bubble_sort(nums))
print(result)

def binary_search(nums, value):

    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == value:
            return mid
        elif nums[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return - 1


print(binary_search(nums, 100))