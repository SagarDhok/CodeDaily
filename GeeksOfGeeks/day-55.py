

# Max and Min Product from 2 Arrays

class Solution:
    def find_multiplication(self, arr1, arr2):
        mx = float("-inf")
        for i in arr1:
            if i>=mx:
                mx = i
        
        mn = float("inf")
        for j  in arr2:
            if j<=mn:
                mn = j
        return mx*mn
            
s = Solution()
arr1 = [5, 7, 9, 3, 6, 2]
arr2 = [1, 2, 6, 1, 9]
print(s.find_multiplication(arr1,arr2))



arr1 = [0, 0, 0, 0]
arr2 = [1, 1, 2]
print(s.find_multiplication(arr1,arr2))