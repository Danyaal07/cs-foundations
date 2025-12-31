nums = [1,3,5,6]

target = 7


def search_insert(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        if nums[middle] > target:
            end = middle - 1
        if nums[middle] < target:
            start = middle + 1
    return start 

print(search_insert(nums, target))

