

def nextPermutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Test cases
test_cases = [
    [1, 2, 3],
    [3, 2, 1],
    [1, 1, 5],
    [1, 3, 2],
    [2, 3, 1],
    [2, 2, 0, 4, 3, 1]
]

for case in test_cases:
    print("Original:", case)
    nextPermutation(case)
    print("Next permutation:", case)
    print("---")
