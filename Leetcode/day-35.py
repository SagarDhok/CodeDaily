
#! Find Smallest Letter Greater Than Target
#APPROACH - 1
class Solution:
    def nextGreatestLetter(self, letters, target):
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]  
s = Solution()
print(s.nextGreatestLetter(["c","f","j"], "a")) 
print(s.nextGreatestLetter(["c","f","j"], "c"))  
print(s.nextGreatestLetter(["x","x","y","y"], "z"))  



#APPROACH - 2
def nextGreatestLetter(letters, target):
    low,= 0
    high=len(letters) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if letters[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
            
    return letters[low % len(letters)]
