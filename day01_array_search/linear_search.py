nums = [1,2,3,4,5,6,7,8] 

def linear_search(nums, target):
    for num in nums:
        if num == target:
            return True
    return False

#TEST
print(linear_search(nums, int(input("Enter number to search: "))))
