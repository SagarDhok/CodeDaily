

#! 914. X of a Kind in a Deck of Cards
class Solution:
    def hasGroupsSizeX(self, deck):
        count_dict = {}
        for card in deck:
            if card not in count_dict:
                count_dict[card] = 1
            else:
                count_dict[card] += 1
        
        def find_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        counts = list(count_dict.values())
        x = counts[0]
        for c in counts[1:]:
            x = find_gcd(x, c)
        
        return x >= 2

s = Solution()
deck = [1,2,3,4,4,3,2,1]
print(s.hasGroupsSizeX(deck))

deck = [1,1,1,2,2,2,3,3]
print(s.hasGroupsSizeX(deck))