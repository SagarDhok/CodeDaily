
#! Display longest name
class Solution:
    def longest(self, arr):
        max_len = 0
        longest_word = ""
        for word in arr:
            if len(word) > max_len:
                max_len = len(word)  
                longest_word = word
        return longest_word


s = Solution()
print(s.longest(["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks", "GeeksforGeeks"]))
print(s.longest(["Apple", "Mango", "Orange", "Banana"]))  