# Mock API for testing (first bad version is 4)
def isBadVersion(version):
    return version >= 4

def firstBadVersion(n):
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid       # first bad is at mid or before
        else:
            left = mid + 1    # first bad is after mid
    return left               # left points to first bad version

# Test
n = 5
print(firstBadVersion(n))  # Output: 4