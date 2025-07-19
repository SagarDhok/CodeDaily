
#! 819. Most Common Word
import string
from typing import List

class Solution:
    def mostCommonWord(self, paragraph, banned):
        lower_paragraph = paragraph.lower()
        clean_paragraph = ''.join(char if char not in string.punctuation else ' ' for char in lower_paragraph)
        list_words = clean_paragraph.split()
        
        freq = {}
        for word in list_words:
            if word not in banned:
                if word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1
        
        max_freq = 0
        most_common = ""
        for word in freq:
            if freq[word] > max_freq:
                max_freq = freq[word]
                most_common = word
        
        return most_common

s = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(s.mostCommonWord(paragraph,banned))

paragraph = "a."
banned = []
print(s.mostCommonWord(paragraph,banned))