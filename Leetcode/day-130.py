
#! 953. Verifying an Alien Dictionary
class Solution:
    def isAlienSorted(self, words, order):
        rank = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False

        return True

print(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")) 
print(Solution().isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))  
print(Solution().isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")) 
