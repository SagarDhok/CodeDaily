



#! 119. Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex) :
        result = []

        for i in range(rowIndex + 1):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(row)

        return result[rowIndex]

s = Solution()
print(s.generate(int(input("Enter A Number : "))))