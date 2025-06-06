
# Majority Element
class Solution:
    def majorityElement(self, arr: list[int]) -> int:
        n = len(arr)
        
        majority_element = -1
        count = 0

        for num in arr:
            if count == 0:
                majority_element = num
                count = 1
            elif num == majority_element:
                count += 1
            else:
                count -= 1
        
        if n == 0:
            return -1

        actual_count = 0
        for num in arr:
            if num == majority_element:
                actual_count += 1
        
        if actual_count > n // 2:
            return majority_element
        else:
            return -1
        
s = Solution()
print(s.majorityElement([1, 1, 2, 1, 3, 5, 1]))
print(s.majorityElement([7]))
print(s.majorityElement([2,13]))