nums = [4,5,6,7,0,1,2]
def findMin(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # If middle element is greater than right, min is in right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:  # min is mid or in left half
            right = mid

    return nums[left]

# Test cases
print(findMin([4,5,6,7,0,1,2]))  # Output: 0
print(findMin([3,4,5,1,2]))      # Output: 1
print(findMin([11,13,15,17]))    # Output: 11