nums = [1,2,3,4,5,6,7,8] 

def binary_search(nums, target):
    start = 0
    end = len(nums) - 1
    while end >= start:
        middle = (start + end) // 2
        if target == nums[middle]:
            return True
        elif target > nums[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return False

print(binary_search(nums, int(input("Enter number to search: "))))
