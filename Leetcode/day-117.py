

#! 888. Fair Candy Swap

class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes) :
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        diff = (sumA - sumB) // 2
        setB = set(bobSizes)
        for x in aliceSizes:
            if x - diff in setB:
                return [x, x - diff]

s= Solution()
aliceSizes = [1,1]
bobSizes = [2,2]
print(s.fairCandySwap(aliceSizes,bobSizes))

aliceSizes = [1,2]
bobSizes = [2,3]
print(s.fairCandySwap(aliceSizes,bobSizes))

aliceSizes = [2]
bobSizes = [1,3]
print(s.fairCandySwap(aliceSizes,bobSizes))
