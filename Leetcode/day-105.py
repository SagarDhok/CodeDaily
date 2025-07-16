


# #! 748. Shortest Completing Word

# from collections import Counter

# class Solution:
#     def shortestCompletingWord(self, licensePlate,words) :
#         letters = [ch.lower() for ch in licensePlate if "A" <= ch <= "Z" or "a" <= ch <= "z"]
#         required = Counter(letters)
#         answer = ""

#         for word in words:
#             word_count = Counter(word)
#             if all(word_count[char] >= required[char] for char in required):
#                 if answer == "" or len(word) < len(answer):
#                     answer = word

#         return answer
# s = Solution()
# licensePlate = "1s3 PSt"
# words = ["step","steps","stripe","stepple"]
# print(s.shortestCompletingWord(licensePlate,words))

# licensePlate = "1s3 456"
# words = ["looks","pest","stew","show"]
# print(s.shortestCompletingWord(licensePlate,words))









