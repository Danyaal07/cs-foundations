def remove_dup(nums):
    if not nums:
        return 0  # empty array

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]  # move unique number forward

    # nums[:slow+1] now contains all unique elements
    return slow + 1
    
nums = [1,2, 2, 3, 4, 4]
k = remove_dup(nums)
print(k)        # 2
print(nums[:k])  # [1,2]
