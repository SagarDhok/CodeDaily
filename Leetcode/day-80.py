

# Keyboard Row
class Solution:
    def findWords(self, words) :
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        found = []


        for word in words:
            lower_word = word.lower()

            row1 = True
            row2 = True
            row3 = True
            
            for ch in lower_word:
              if ch not in first_row:
                row1 = False
              if ch not in second_row:
                row2 = False
              if ch not in third_row:
                row3 = False
            
            if row1 or row2 or row3:
             found.append(word)
        return found
    
print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))
print(Solution().findWords(["omk"]))
print(Solution().findWords(["adsdf","sfd"]))