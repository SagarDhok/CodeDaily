

#! 804. Unique Morse Code Words
class Solution:
    def uniqueMorseRepresentations(self, words) :
        

                morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

                res = set()
                for word in words:
                        code = ""
                        for char in word:
                          code +=morse_code[ord(char)-ord('a')]
                        res.add(code)
                return len(res)
s= Solution()
words = ["gin","zen","gig","msg"]
print(s.uniqueMorseRepresentations(words))