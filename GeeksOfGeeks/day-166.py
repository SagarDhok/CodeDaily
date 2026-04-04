

#! 6. Zigzag Conversion
# Medium
# Topics
# premium lock icon
# Companies
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows==1:
            return s
        else:
                rows = ["" for _ in range(numRows)]

                current_row = 0 
                direction = 1

                for ch in s :
                     rows[current_row] += ch 

                     if current_row== 0:
                          direction = 1
                     elif current_row == numRows-1:
                          direction = -1 

                     current_row += direction

                return "".join(rows)
 
s = Solution()
print(s.convert("PAYPALISHIRING",3))

print(s.convert("PAYPALISHIRING",4))

print(s.convert("A",1))
