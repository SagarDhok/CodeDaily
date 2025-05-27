

# Count Inversions
class Solution:
    def inversionCount(self, arr):
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr, 0
            mid = len(arr) // 2
            left, inv_left = merge_sort(arr[:mid])
            right, inv_right = merge_sort(arr[mid:])
            merged, inv_merge = merge(left, right)
            return merged, inv_left + inv_right + inv_merge

        def merge(left, right):
            i = j = inv_count = 0
            merged = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
                    inv_count += len(left) - i  
            merged += left[i:]
            merged += right[j:]
            return merged, inv_count

        _, total_inversions = merge_sort(arr)
        return total_inversions
sol = Solution()
arr = [2, 4, 1, 3, 5]
print(sol.inversionCount(arr))
arr = [2, 3, 4, 5, 6]
print(sol.inversionCount(arr))
arr =[10, 10, 10]
print(sol.inversionCount(arr))