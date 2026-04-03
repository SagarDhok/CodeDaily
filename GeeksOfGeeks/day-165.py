




#! Max Min
# Difficulty: BasicAccuracy: 86.09%Submissions: 109K+Points: 1
# Given an array A of size N of integers. Your task is to find the sum of minimum and maximum element in the array.

# Example 1:

# Input:
# N = 5
# A[] = {-2, 1, -4, 5, 3}
# Output: 1
# Explanation: min = -4, max =  5. Sum = -4 + 5 = 1
 

# Example 2:

# Input:
# N = 4
# A[]  = {1, 3, 4, 1}
# Output: 5
# Explanation: min = 1, max = 4. Sum = 1 + 4 = 5
 

# Your Task:  
# You don't need to read input or print anything. Your task is to complete the function findSum() which takes the array A[] and its size N as inputs and returns the summation of minimum and maximum element of the array.

 

# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)

 

# Constraints:
# 1 <= N <= 105
# -109 <= Ai <= 109



class Solution:
    def findSum(self, A, N): 
        srt = sorted(A)
        mxv = srt[-1]   
        miv = srt[0]    
        
        return mxv + miv

s = Solution()
N = 5
A = {-2, 1, -4, 5, 3}
print(s.findSum(A,N))

N = 4
A  = {1, 3, 4, 1}
print(s.findSum(A,N))


class Solution:
    def findSum(self, A, N): 
        srt = sorted(A)
        return srt[0] + srt[-1]

s = Solution()
N = 5
A = {-2, 1, -4, 5, 3}
print(s.findSum(A,N))

N = 4
A  = {1, 3, 4, 1}
print(s.findSum(A,N))



class Solution:
    def findSum(self, A, N): 
        return max(A) + min(A)
    
s = Solution()
N = 5
A = {-2, 1, -4, 5, 3}
print(s.findSum(A,N))

N = 4
A  = {1, 3, 4, 1}
print(s.findSum(A,N))
    

