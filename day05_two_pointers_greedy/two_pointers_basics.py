def remove_duplicates(nums):
    if not nums:
        return 0
    write_index = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1
    return write_index



# Test
nums = [1,1,2,2,3,4,4,5]
length = remove_duplicates(nums)
print(length)        # 5
print(nums[:length]) # [1,2,3,4,5]