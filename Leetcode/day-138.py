

#! 17. Letter Combinations of a Phone Number
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = "2"
# Output: ["a","b","c"]
 

# Constraints:

# 1 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
 

class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = [""]

        for digit in digits:
            temp = []
            for combination in result:
                for letter in phone[digit]:
                    temp.append(combination + letter)
            result = temp

        return result


sol = Solution()

print("Test 1:", sol.letterCombinations("23"))
print("Test 2:", sol.letterCombinations("2"))
print("Test 3:", sol.letterCombinations(""))
print("Test 4:", sol.letterCombinations("79"))