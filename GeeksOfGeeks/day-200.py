


#! Josephus problem
# Difficulty: EasyAccuracy: 57.26%Submissions: 183K+Points: 2
# You are playing a game with n people standing in a circle, numbered from 1 to n. Starting from person 1, every kth person is eliminated in a circular fashion. The process continues until only one person remains.
# Given integers n and k, return the position (1-based index) of the person who will survive.

# Examples :

# Input: n = 5, k = 2
# Output: 3
# Explanation: Firstly, the person at position 2 is killed, then the person at position 4 is killed, then the person at position 1 is killed. 
# Finally, the person at position 5 is killed. So the person at position 3 survives. 
# Input: n = 7, k = 3
# Output: 4
# Explanation: The elimination order is 3 → 6 → 2 → 7 → 5 → 1, and the person at position 4 survives.

class Solution:
    def josephus(self, n, k):
        
        ans = 0
        
        for i in range(2, n + 1):
            ans = (ans + k) % i
        
        return ans + 1
s= Solution()
n,k= int(input("Enter Value for n :")),int(input("Enter Value for K :"))
print(s.josephus(n, k))