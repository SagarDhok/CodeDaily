
#! 1. Reverse String
# Given a list of characters s, reverse it in-place.
# Example:
# ["h","e","l","l","o"] → ["o","l","l","e","h"]

s = ["h","e","l","l","o"]
reversed_s = s[::-1]
print(reversed_s)

s= ["h","e","l","l","o"]
left = 0
right= len(s)-1
while left<right:
    s[left],s[right] = s[right],s[left]
    left+=1
    right-=1

print(s)
