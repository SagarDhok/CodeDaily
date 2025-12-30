
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


#! 2. Valid Palindrome
# Return True if a string is a palindrome, considering only alphanumeric characters and ignoring case.
# Example:
# "A man, a plan, a canal: Panama" → True

s = "A man, a plan, a canal: Panama"
left = 0
right = len(s)-1
while left<right:
    while left<right and not s[left].isalnum():
        left+=1

    while left<right and not s[right].isalnum():
        right-=1
    
    if s[left].lower()!=s[right].lower():
        print(False)
        break
    left+=1
    right-=1

else:
    print(True)

#* Without Built in Funtion
s = "A man, a plan, a canal: Panama"
left = 0
right = len(s) - 1
while left < right:
    while left < right and not (
        ('a' <= s[left] <= 'z') or
        ('A' <= s[left] <= 'Z') or
        ('0' <= s[left] <= '9')
    ):
        left += 1

    while left < right and not (
        ('a' <= s[right] <= 'z') or
        ('A' <= s[right] <= 'Z') or
        ('0' <= s[right] <= '9')
    ):
        right -= 1

    left_char = s[left]
    right_char = s[right]

    if 'A' <= left_char <= 'Z':
        left_char = chr(ord(left_char) + 32)

    if 'A' <= right_char <= 'Z':
        right_char = chr(ord(right_char) + 32)

    if left_char != right_char:
        print(False)
        break

    left += 1
    right -= 1

else:
    print(True)


