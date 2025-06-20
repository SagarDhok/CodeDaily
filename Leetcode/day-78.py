



#  Search in Rotated Sorted Array
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return -1
    

s = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(s.search(nums,target))

nums = [4,5,6,7,0,1,2]
target = 3
print(s.search(nums,target))


nums = [1]
target = 0
print(s.search(nums,target))