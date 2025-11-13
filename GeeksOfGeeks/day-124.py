
#! Distinct Adjacent Element
class Solution:
    def distinctAdjacentElement(self, arr):
        n = len(arr)
        freq = {}
        for i in range(n):
            if arr[i] in freq:
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1
        max_freq = 0
        for key in freq:
            if freq[key] > max_freq:
                max_freq = freq[key]
        if max_freq > (n + 1) // 2:
            return False
        return True

