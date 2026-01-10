
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



#! 3. First Unique Character in a String
# Return the index of the first non-repeating character.
# If none exists, return -1.
# Example:
# "leetcode" → 0

s = "leetcode"
count = {}
for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1
for i in range(len(s)):
    if count[s[i]] == 1:
        print(i)
        break
else:
    print(-1)


s = "leetcode"
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
for i in range(len(s)):
    if count[s[i]] == 1:
        print(i)
        break
else:
    print(-1)


#! 4. Valid Anagram
# Return True if one string is an anagram of another.
# Example:
# "anagram", "nagaram" → True
s = "anagram"
t = "nagaram"

s = "aab"
t = "abb"


if len(s) != len(t):
    print(False)
else:
    count = {}

    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    for ch in t:
        if ch not in count:
            print(False)
            break
        count[ch] -= 1
        if count[ch] < 0:
            print(False)
            break
    else:
        print(True)


s = "anagram"
t = "nagaram"
print(sorted(s) == sorted(t))



#! 5. Longest Common Prefix
# Find the longest common prefix among an array of strings.
# Example:
# ["flower","flow","flight"] → "fl"
def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for word in strs[1:]:
            if i >= len(word) or word[i] != char:
                return prefix
        prefix += char
    return prefix

print(longest_common_prefix(["flower", "flow", "flight"]))



strs = ["flower", "flow", "flight"]

prefix = strs[0]

for s in strs[1:]:
    while not s.startswith(prefix):
        prefix = prefix[:-1]
        if not prefix:
            break

print(prefix)


#! 📦 ARRAYS
# 6. Two Sum

# Return indices of two numbers that add up to a vtarget.

# Example:
# [2,7,11,15], target = 9 → [0,1]

arr = [2, 7, 11, 15]
target = 9

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(i, j)


arr = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(arr):
    need = target - num

    if need in seen:
        print(seen[need], i)
        break

    seen[num] = i


#! 7. Contains Duplicate

# Return True if any value appears at least twice.

# Example:
# [1,2,3,1] → True

lst = [1, 2, 3, 1]

count = {}
for i in lst:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for val in count:
    if count[val] >= 2:
        print(True)
        break
else:
    print(False)


lst = [1, 2, 3, 1]
print(len(lst) != len(set(lst)))

lst = [1, 2, 3, 1]
seen = set()
for i in lst:
    if i in seen:
        print(True)
        break
    seen.add(i)
else:
    print(False)


#! 8. Move Zeroes

# Move all zeroes to the end while maintaining order.

# Example:
# [0,1,0,3,12] → [1,3,12,0,0]

lst = [0,1,0,3,12]
pos = 0
for i in range(len(lst)):
    if lst[i]!=0:
        lst[pos]=lst[i]
        pos+=1
for i in range(pos, len(lst)):
    lst[i] = 0
print(lst)


arr = [0, 1, 0, 3, 12]
result = []
for x in arr:
    if x != 0:
        result.append(x)
zeros = len(arr) - len(result)
# result.extend([0] * zeros)
for z in range(zeros):
    result.append(0)
print(result)


#! 9. Best Time to Buy and Sell Stock
# Return maximum profit from one buy and one sell.
# Example:
# [7,1,5,3,6,4] → 5

lst =  [7,1,5,3,6,4] 

if len(lst)<=1:
    print(0)
else:
    min_price = lst[0]
    max_price = 0
    for price in lst:
        if price<min_price:
            min_price=price

        profit = price-min_price
        if profit>max_price:
            max_price= profit
    print(max_price)
    

#! 10. Merge Sorted Array
# Merge two sorted arrays into one sorted array in-place.

# Example:
# [1,2,3,0,0,0] + [2,5,6] → [1,2,2,3,5,6]

a = [1, 2, 3, 0, 0, 0]
b = [2, 5, 6]
m = 3
n = 3

i = m - 1
j = n - 1
k = m + n - 1

while i >= 0 and j >= 0:
    if a[i] > b[j]:
        a[k] = a[i]
        i -= 1
    else:
        a[k] = b[j]
        j -= 1
    k -= 1

while j >= 0:
    a[k] = b[j]
    j -= 1
    k -= 1

print(a)


a = [1,2,3,0,0,0]
b = [2,5,6]
m =3
a[m:] = b
a.sort()
print(a)


#! 11. Majority Element

# Find the element that appears more than ⌊n/2⌋ times.

# Example:
# [3,2,3] → 3


lst = [3,2,3]
ele = len(lst)//2

count = {}
for i in lst:
        count[i] = count.get(i, 0) + 1

for val in count:
    if count[val]>ele:
        print(val)

#!Boyer Moore 
lst = [3, 2, 3]
candidate = None
count = 0

for num in lst:
    if count == 0:
        candidate = num
    count += 1 if num == candidate else -1

print(candidate)
