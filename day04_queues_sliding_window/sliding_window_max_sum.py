nums = [2, 1, 5, 1, 3, 2]
k = 3
windowSum = sum(nums[:k])
maxSum = windowSum

for i in range(len(nums) - k):
    windowSum = windowSum - nums[i] + nums[k + i]
    if windowSum > maxSum:
        maxSum = windowSum
print(maxSum)
