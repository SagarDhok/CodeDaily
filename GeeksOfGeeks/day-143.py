


#! K-th element of two Arrays
# Difficulty: MediumAccuracy: 37.4%Submissions: 396K+Points: 4Average Time: 15m
# Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array.

# Examples :

# Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
# Output: 6
# Explanation: The final combined sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.
# Input: a[] = [1, 4, 8, 10, 12], b[] = [5, 7, 11, 15, 17], k = 6
# Output: 10
# Explanation: Combined sorted array is [1, 4, 5, 7, 8, 10, 11, 12, 15, 17]. The 6th element of this array is 10.
# Constraints:
# 1 ≤ a.size(), b.size() ≤ 106
# 1 ≤ k ≤ a.size() + b.size()
# 0 ≤ a[i], b[i] ≤ 108


class Solution:
    def kthElement(self, a, b, k):
        n = len(a)
        m = len(b)

        if n > m:
            return self.kthElement(b, a, k)

        low = max(0, k - m)
        high = min(k, n)

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = k - cut1

            l1 = a[cut1 - 1] if cut1 > 0 else float('-inf')
            l2 = b[cut2 - 1] if cut2 > 0 else float('-inf')
            r1 = a[cut1] if cut1 < n else float('inf')
            r2 = b[cut2] if cut2 < m else float('inf')

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)

            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1