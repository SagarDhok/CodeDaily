
#! Distinct Elements in a Stream
class Solution:
    def getDistinct(self, arr):
        freq = {}
        result = []

        for num in arr:
            if num > 0:
                freq[num] = freq.get(num, 0) + 1
            else:
                if -num in freq:
                    freq[-num] -= 1
                    if freq[-num] == 0:
                        del freq[-num]
            result.append(len(freq))

        return result

sol = Solution()
print(sol.getDistinct([5, 5, 7, -5, -7, 1, 2, -2]))
print(sol.getDistinct([9, 9, 3, -9, -3, -9]))
