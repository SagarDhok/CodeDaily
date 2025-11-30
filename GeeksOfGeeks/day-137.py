
#! Anagram
class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        freq = [0] * 26  
        
        for ch in s1:
            freq[ord(ch) - ord('a')] += 1
        
        for ch in s2:
            freq[ord(ch) - ord('a')] -= 1
        
        for f in freq:
            if f != 0:
                return False
        
        return True
s = Solution()
s1 = "geeks" 
s2 = "kseeg"
print(s.areAnagrams(s1,s2))

s1 = "allergy"
s2 = "allergyy"
print(s.areAnagrams(s1,s2))


s1 = "listen", 
s2 = "lists"
print(s.areAnagrams(s1,s2))


class Solution:
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        freq = {}

        for ch in s1:
            freq[ch] = freq.get(ch, 0) + 1
        
        for ch in s2:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False
        
        return True

s = Solution()
s1 = "geeks" 
s2 = "kseeg"
print(s.areAnagrams(s1,s2))

s1 = "allergy"
s2 = "allergyy"
print(s.areAnagrams(s1,s2))


s1 = "listen", 
s2 = "lists"
print(s.areAnagrams(s1,s2))