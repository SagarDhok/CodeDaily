
#! 1. Reverse String
# Given a list of characters s, reverse it in-place.
# Example:
# ["h","e","left","left","o"] → ["o","left","left","e","h"]

# s = ["h","e","left","left","o"]
# reversed_s = s[::-1]
# print(reversed_s)

# s= ["h","e","left","left","o"]
# left = 0
# right= len(s)-1
# while left<right:
#     s[left],s[right] = s[right],s[left]
#     left+=1
#     right-=1

# print(s)


#! 2. Valid Palindrome
# Return True if a string is a palindrome, considering only alphanumeric characters and ignoring case.
# Example:
# "A man, a plan, a canal: Panama" → True

# s = "A man, a plan, a canal: Panama"
# left = 0
# right = len(s)-1
# while left<right:
#     while left<right and not s[left].isalnum():
#         left+=1

#     while left<right and not s[right].isalnum():
#         right-=1
    
#     if s[left].lower()!=s[right].lower():
#         print(False)
#         break
#     left+=1
#     right-=1

# else:
#     print(True)

# s = "A man, a plan, a canal: Panama"
# left = 0
# right = len(s) - 1
# while left < right:
#     while left < right and not (
#         ('a' <= s[left] <= 'z') or
#         ('A' <= s[left] <= 'Z') or
#         ('0' <= s[left] <= '9')
#     ):
#         left += 1

#     while left < right and not (
#         ('a' <= s[right] <= 'z') or
#         ('A' <= s[right] <= 'Z') or
#         ('0' <= s[right] <= '9')
#     ):
#         right -= 1

#     left_char = s[left]
#     right_char = s[right]

#     if 'A' <= left_char <= 'Z':
#         left_char = chr(ord(left_char) + 32)

#     if 'A' <= right_char <= 'Z':
#         right_char = chr(ord(right_char) + 32)

#     if left_char != right_char:
#         print(False)
#         break

#     left += 1
#     right -= 1

# else:
#     print(True)



#! 3. First Unique Character in a String
# Return the index of the first non-repeating character.
# If none exists, return -1.
# Example:
# "leetcode" → 0

# s = "leetcode"
# count = {}
# for ch in s:
#     if ch in count:
#         count[ch] += 1
#     else:
#         count[ch] = 1
# for i in range(len(s)):
#     if count[s[i]] == 1:
#         print(i)
#         break
# else:
#     print(-1)


# s = "leetcode"
# count = {}
# for ch in s:
#     count[ch] = count.get(ch, 0) + 1
# for i in range(len(s)):
#     if count[s[i]] == 1:
#         print(i)
#         break
# else:
#     print(-1)


#! 4. Valid Anagram
# Return True if one string is an anagram of another.
# Example:
# "anagram", "nagaram" → True
# s = "anagram"
# t = "nagaram"

# s = "aab"
# t = "abb"


# if len(s) != len(t):
#     print(False)
# else:
#     count = {}

#     for ch in s:
#         count[ch] = count.get(ch, 0) + 1

#     for ch in t:
#         if ch not in count:
#             print(False)
#             break
#         count[ch] -= 1
#         if count[ch] < 0:
#             print(False)
#             break
#     else:
#         print(True)


# s = "anagram"
# t = "nagaram"
# print(sorted(s) == sorted(t))



#! 5. Longest Common Prefix
# Find the longest common prefix among an array of strings.
# Example:
# ["flower","flow","flight"] → "fl"
# def longest_common_prefix(strs):
#     if not strs:
#         return ""

#     prefix = ""
#     for i in range(len(strs[0])):
#         char = strs[0][i]
#         for word in strs[1:]:
#             if i >= len(word) or word[i] != char:
#                 return prefix
#         prefix += char
#     return prefix

# print(longest_common_prefix(["flower", "flow", "flight"]))



# strs = ["flower", "flow", "flight"]

# prefix = strs[0]

# for s in strs[1:]:
#     while not s.startswith(prefix):
#         prefix = prefix[:-1]
#         if not prefix:
#             break

# print(prefix)


#! 📦 ARRAYS
# 6. Two Sum

# Return indices of two numbers that add up to a vtarget.

# Example:
# [2,7,11,15], target = 9 → [0,1]

# arr = [2, 7, 11, 15]
# target = 9

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print(i, j)


# arr = [2, 7, 11, 15]
# target = 9

# seen = {}

# for i, num in enumerate(arr):
#     need = target - num

#     if need in seen:
#         print(seen[need], i)
#         break

#     seen[num] = i


#! 7. Contains Duplicate

# Return True if any value appears at least twice.

# Example:
# [1,2,3,1] → True

# lst = [1, 2, 3, 1]

# count = {}
# for i in lst:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1

# for val in count:
#     if count[val] >= 2:
#         print(True)
#         break
# else:
#     print(False)


# lst = [1, 2, 3, 1]
# print(len(lst) != len(set(lst)))

# lst = [1, 2, 3, 1]
# seen = set()
# for i in lst:
#     if i in seen:
#         print(True)
#         break
#     seen.add(i)
# else:
#     print(False)


#! 8. Move Zeroes

# Move all zeroes to the end while maintaining order.

# Example:
# [0,1,0,3,12] → [1,3,12,0,0]

# lst = [0,1,0,3,12]
# pos = 0
# for i in range(len(lst)):
#     if lst[i]!=0:
#         lst[pos]=lst[i]
#         pos+=1
# for i in range(pos, len(lst)):
#     lst[i] = 0
# print(lst)


# arr = [0, 1, 0, 3, 12]
# result = []
# for x in arr:
#     if x != 0:
#         result.append(x)
# zeros = len(arr) - len(result)
# # result.extend([0] * zeros)
# for z in range(zeros):
#     result.append(0)
# print(result)


#! 9. Best Time to Buy and Sell Stock
# Return maximum profit from one buy and one sell.
# Example:
# [7,1,5,3,6,4] → 5

# lst =  [7,1,5,3,6,4] 

# if len(lst)<=1:
#     print(0)
# else:
#     min_price = lst[0]
#     max_price = 0
#     for price in lst:
#         if price<min_price:
#             min_price=price

#         profit = price-min_price
#         if profit>max_price:
#             max_price= profit
#     print(max_price)
    

#! 10. Merge Sorted Array
# Merge two sorted arrays into one sorted array in-place.

# Example:
# [1,2,3,0,0,0] + [2,5,6] → [1,2,2,3,5,6]

# a = [1, 2, 3, 0, 0, 0]
# b = [2, 5, 6]
# m = 3
# n = 3

# i = m - 1
# j = n - 1
# k = m + n - 1

# while i >= 0 and j >= 0:
#     if a[i] > b[j]:
#         a[k] = a[i]
#         i -= 1
#     else:
#         a[k] = b[j]
#         j -= 1
#     k -= 1

# while j >= 0:
#     a[k] = b[j]
#     j -= 1
#     k -= 1

# print(a)


# a = [1,2,3,0,0,0]
# b = [2,5,6]
# m =3
# a[m:] = b
# a.sort()
# print(a)


#! 11. Majority Element

# Find the element that appears more than ⌊n/2⌋ times.

# Example:
# [3,2,3] → 3


# lst = [3,2,3]
# ele = len(lst)//2

# count = {}
# for i in lst:
#         count[i] = count.get(i, 0) + 1

# for val in count:
#     if count[val]>ele:
#         print(val)

# #!Boyer Moore 
# lst = [3, 2, 3]
# candidate = None
# count = 0

# for num in lst:
#     if count == 0:
#         candidate = num
#     count += 1 if num == candidate else -1

# print(candidate)

#! 12. Intersection of Two Arrays
# Return the intersection of two arrays (unique elements).
# Example:
# [1,2,2,1], [2,2] → [2]

# lst1 = [1,2,2,1]
# lst2 = [2,2]

# common_element = set()
# for i in lst1:
#     if i in lst2:
#         common_element.add(i)

# print(common_element)


# lst1 = [1,2,2,1]
# lst2 = [2,2]
# set2 = set(lst2)
# common_element = set()

# for i in lst1:
#     if i in set2:
#         common_element.add(i)

# print(common_element)


#? 13. Top K Frequent Elements
# Return the k most frequent elements.
# Example:
# [1,1,1,2,2,3], k=2 → [1,2]

# nums = [1, 1, 1, 2, 2, 3]
# k = 2

# dct = {}
# for i in nums:
#     dct[i] = dct.get(i, 0) + 1

# sorted_items = sorted(dct.items(), key=lambda x: x[1], reverse=True)

# result = [key for key in sorted_items[:k]]
# print(result)



#! 📚 STACK
# 14. Valid Parentheses

# Check if parentheses are valid.

# Example:
# "()[]{}" → True

# def isValid(s):
#     stack = []
#     closeToOpen = {')':'(', ']':'[', '}':'{'}

#     for c in s:
#         if c in closeToOpen:
#             if not stack or stack[-1] != closeToOpen[c]:
#                 return False
#             stack.pop()
#         else:
#             stack.append(c)
#     return not stack


# print(isValid("()[]{}"))  
# print(isValid("([)]"))       
# print(isValid("{[]}"))      
# print(isValid("((("))        




#! 15. Min Stack
# Design a stack that supports retrieving the minimum element in O(1).

#* “We push (value, min_so_far) because when elements are popped, the minimum might be removed. Storing the minimum at each step ensures getMin() stays O(1) without recalculation.”
# class MinStack:
#     def __init__(self):
#         self.stack = []

#     def push(self, val):
#         if not self.stack:
#             self.stack.append((val, val))
#         else:
#             current_min = min(val, self.stack[-1][1])
#             self.stack.append((val, current_min))

#     def pop(self):
#         self.stack.pop()

#     def top(self):
#         return self.stack[-1][0]

#     def getMin(self):
#         return self.stack[-1][1]


# s = MinStack()
# s.push(5)
# s.push(3)
# s.push(7)

# print(s.top())     # 7
# print(s.getMin())  # 3

# s.pop()
# print(s.getMin())  # 3

# s.pop()

# print(s.getMin())  # 5

#! 16. Factorial (Recursion)
# Compute factorial using recursion.

#Normal Factorial
# n = int(input("Enter A Value : "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)


# Factorial using Recursion (Python)
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)

# n = int(input())
# print(fact(n))




#! 17. Fibonacci Number

# Return the nth Fibonacci number.

# n = int(input("Enter Value : "))
# a = 0
# b = 1

# for i in range(n): 
#     temp = a+b
#     a = b         
#     b = temp 

# print(a)

#! 📐 TWO POINTERS
# 18. Remove Duplicates from Sorted Array

# nums = [0,0,1,1,1,2,2,3,3,4]

# if len(nums) == 0:
#     print(0)

# i = 0  

# for j in range(1, len(nums)):  
#     if nums[j] != nums[i]:
#         i += 1
#         nums[i] = nums[j]

# print(nums[:i+1])
# print(nums[:i+1])



#! 19. Squares of a Sorted Array
# Return a sorted array of squares.

# lst = [-4,-1,0,3,10]
# for i in range(len(lst)):
#      lst[i] = lst[i]*lst[i]

# lst.sort()
# print(lst)


# nums = [-4, -1, 0, 3, 10]

# n = len(nums)
# ans = [0] * n

# i = 0
# j = n - 1
# k = n - 1

# while i <= j:
#     if abs(nums[i]) > abs(nums[j]):
#         ans[k] = nums[i] * nums[i]
#         i += 1
#     else:
#         ans[k] = nums[j] * nums[j]
#         j -= 1
#     k -= 1

# print(ans)



# def sortedSquares(nums):
#     left, right = 0, len(nums) - 1
#     res = []

#     while left <= right:
#         if nums[left] * nums[left] > nums[right] * nums[right]:
#             res.append(nums[left] * nums[left])
#             left += 1
#         else:
#             res.append(nums[right] * nums[right])
#             right -= 1

#     return res[::-1]
# print(sortedSquares( [-4, -1, 0, 3, 10]))



#! 20. Subarray Sum Equals K
# Count subarrays whose sum equals k.

# def subarraySum(nums, k):
#     count = 0
#     n = len(nums)

#     for i in range(n):
#         s = 0
#         for j in range(i, n):
#             s += nums[j]
#             if s == k:
#                 count += 1

#     return count

# nums = [3, 4, 7, 2, -3, 1, 4, 2]
# k = 7
# print(subarraySum(nums, k))  

# nums = [1, 1, 1]
# k = 2
# print(subarraySum(nums, k)) 

#! 21. Group Anagrams

# Group strings that are anagrams.

# from collections import defaultdict

# class Solution:
#     def groupAnagrams(self, strs):
#         groups = defaultdict(list)

#         for s in strs:
#             key = ''.join(sorted(s))
#             groups[key].append(s)

#         return list(groups.values())

# s = Solution()
# print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


# from collections import defaultdict
# groups = defaultdict(list)
# print(groups)





# Q22. Product of Array Except Self
# Return array where each element is product of all others (no division).


# nums = [1,2,3,4]
#Output:[24,12,8,6]

# nums = [1,2,3,4]
# ans = [1] * len(nums)

# prefix = 1
# for i in range(len(nums)):
#     ans[i] = prefix
#     prefix *= nums[i]

# # [1, 1, 2, 6]
# suffix = 1
# for i in range(len(nums) - 1, -1, -1):
#     ans[i] *= suffix
#     suffix *= nums[i]

# print(ans)


# nums = [1,2,3,4]
# ans = []
# for i in range(len(nums)):
#         prod = 1
#         for j in range(len(nums)):
#             if i != j:
#                 prod *= nums[j]
#         ans.append(prod)
# print(ans)



#!Q23) Problem: Find the Missing Number
# Problem Statement
# You are given an array nums containing n distinct numbers taken from the range [0, n].
# That means:
# The array has n elements
# Numbers are from 0 to n
# Exactly one number is missing
# Your task is to return the missing number.
# Example 1
# Input: nums = [3, 0, 1]
# Output: 2

# Example 2
# Input: nums = [0, 1]
# Output: 2

# Example 3
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8

# Constraints
# 1 <= n <= 10^4
# All numbers in nums are unique
# nums contains numbers from [0, n] with one missing

# nums = [9,6,4,2,3,5,7,0,1]

# for i in range(len(nums)+1):
#     if i not in nums:
#         print(i)


# nums = [9,6,4,2,3,5,7,0,1]

# n = len(nums)
# expected_sum = n * (n + 1) // 2  #formula to calculate sum of natural numbers 

# print(expected_sum)
# actual_sum = sum(nums)

# print(expected_sum - actual_sum)



#!Q24) Find the Largest Element in an Array

# Problem Statement (clean + realistic):

# Given an integer array nums, return the largest element in the array.

# Example
# Input: nums = [3, 7, 2, 9, 4]
# Output: 9

# Constraints

# 1 <= len(nums) <= 10^4

# Array contains at least one element

# Integers can be negative

# Why this question matters (don’t underestimate it)

# Interviewers use this to check:

# Can you reason without overengineering?

# Do you handle negatives correctly?

# Do you explain time & space cleanly?

# Do you avoid unnecessary data structures?

# People fail this by:

# Sorting the array (wasteful)

# Using extra space for no reason

# Not explaining edge cases

# What you must submit

# Same strict format:

# 1. Python code

# (No max() built-in — pretend interviewer banned it)

# 2. Explanation

# Answer:

# How you initialize

# How you update

# Why this always works

# 3. Time & Space Complexity


# nums = [3, 7, 2, 9, 4]
# Output: 9


# nums = [3, 7, 2, 9, 4]

# max_val = nums[0]
# for num in nums:
#     if num > max_val:
#         max_val = num

# print(max_val)




#! Q25) Second Largest Element in an Array

# Problem Statement:

# Given an integer array nums, find the second largest distinct element.

# If the second largest element does not exist, return -1.

# Examples
# Input: [3, 7, 2, 9, 4]
# Output: 7

# Input: [10, 10, 10]
# Output: -1

# Input: [-5, -2, -9, -1]
# Output: -2

# Constraints

# 1 <= len(nums) <= 10^4

# Integers can be negative

# Elements may repeat



# lst = [3, 7, 2, 9, 4]
# lst.sort()
# print("Second Max :",list(set(lst))[-2])


# lst = [3, 7, 2, 9, 4]

# mv = float('-inf')
# sv = float('-inf')

# for i in lst:
#     if i > mv:
#         sv = mv
#         mv = i
#     elif i != mv and i > sv:
#         sv = i

# print(sv if sv != float('-inf') else -1)




#!Q26) You’re given a list of integers nums.
# Task:
# Write a function that returns the first non-repeating integer in the list.
# If all numbers repeat, return -1.
# Preserve the original order of the list.
# Time complexity should be better than O(n²).
# Example
# nums = [4, 5, 1, 2, 0, 4]
# output = 5
# nums = [1, 1, 2, 2]
# output = -1
# nums = [1, 1, 2, 2,3]
# output = 3
# Constraints
# Input list length: 0 ≤ n ≤ 10^5
# Integers can be negative
# You may assume the input is a Python list
# Requirements
# Write clean, readable Python code
# No external libraries except Python standard library
# Function signature:
# def first_non_repeating(nums):
#     pass

# def first_non_repeating(nums):
#    count ={}
#    for i in nums:
#       count[i] = count.get(i,0)+1
#    for key in nums:
#        if count[key]==1:
#            return key
#    return -1
           
# res = first_non_repeating([4, 5, 1, 2, 0, 4])
# print(f"First Non Repeating Numbers are : {res}")
# res = first_non_repeating([1, 1, 2, 2])
# print(f"First Non Repeating Numbers are : {res}")


#!Q27) You’re given a string s.
# Task
# Write a function that returns the first non-repeating character in the string.
# The comparison should be case-sensitive
# Preserve the original order
# If no such character exists, return None
# Examples
# s = "swiss"
# output = "w"

# s = "aabbcc"
# output = None

# s = "Python"
# output = "P"

# Constraints
# 0 ≤ len(s) ≤ 10^5
# String contains only ASCII characters
# Function signature
# def first_non_repeating_char(s):
#     pass
# Rules
# No nested loops that make it O(n²)
# Use only Python standard features
# Write clean, readable code


# def first_non_repeating_char(s):


#     freq = {}
#     for c in s:
#         freq[c]=freq.get(c,0)+1

#     for c in s:
#         if freq[c]==1:
#             return i

#     return None

# s = "swiss"       
# res = first_non_repeating_char(s)
# print("first non-repeating character in the string : ",res)

# print(first_non_repeating_char("Python"))

# print(first_non_repeating_char("aabbcc"))





#! Q28) You are given a list of integers.

# Task

# Write a function that returns all elements that appear more than once,
# without duplicates, and preserve the order of their first repetition.

# If no element repeats, return an empty list.

# Examples
# [1, 2, 3, 2, 4, 1, 5]  → [2, 1]
# [1, 2, 3, 4]          → []
# [5, 5, 5, 5]          → [5]

# Function signature
# def find_duplicates(nums):
#     pass

# Rules
# Do not sort the list
# Do not use count() inside a loop
# Time complexity should be O(n)
# Use only Python standard features

# def find_duplicates(nums):
#    seen = set()
#    added = set()
#    res = []
#    for val in nums:
#        if val in seen and val not in added:
#            res.append(val)
#            added.add(val)
#        else:
#            seen.add(val)
#    return res
 
# print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))



# #! Q29) You are given a list of integers nums.
# # Task
# # Write a function that returns the count of each number, but only for numbers that appear more than once,
# # and preserve the order of their first appearance.
# # Return the result as a list of tuples: (number, count).
# # If no number repeats, return an empty list.
# # Examples
# # nums = [1, 2, 3, 2, 4, 1, 5]
# # output = [(1, 2), (2, 2)]
# # nums = [5, 5, 5, 3, 3]
# # output = [(5, 3), (3, 2)]
# # nums = [1, 2, 3]
# # output = []
# # Function signature
# # def count_duplicates(nums):
# #     pass
# # Rules
# # Do NOT sort the list
# # Do NOT use count() inside a loop
# # Preserve order of first appearance
# # Be ready to explain time & space complexity


# def count_duplicates(nums):
#     count = {}
#     for val in nums:
#         count[val] = count.get(val, 0) + 1

#     res = []
#     added = set()

#     for val in nums:
#         if count[val] > 1 and val not in added:
#             res.append((val, count[val]))
#             added.add(val)

#     return res


# print(count_duplicates([1, 2, 3, 2, 4, 1, 5]))
# print(count_duplicates( [5, 5, 5, 3, 3]))



#!Q30) You are given a list of integers nums.
# Task
# Write a function that returns a new list where:
# All even numbers come first
# All odd numbers come after
# The relative order of even numbers and odd numbers must be preserved
# This is called a stable partition.
# Examples
# nums = [1, 2, 3, 4, 5, 6]
# output = [2, 4, 6, 1, 3, 5]

# nums = [2, 4, 6]
# output = [2, 4, 6]

# nums = [1, 3, 5]
# output = [1, 3, 5]

# nums = []
# output = []

# Function signature
# def stable_even_odd(nums):
#     pass

# Rules

# Do not sort

# Do not change relative order

# Be ready to explain time & space complexity

# Clean, readable Python

# def stable_even_odd(nums):
#     pass

# def stable_even_odd(nums):
#     evens = []
#     odds = []

#     for val in nums:
#         if val % 2 == 0:
#             evens.append(val)
#         else:
#             odds.append(val)

#     return evens + odds


# print(stable_even_odd([1, 2, 3, 4, 5, 6]))
# print(stable_even_odd([1, 3,5]))
# print(stable_even_odd([2,4,6]))
# print(stable_even_odd([]))


#!Q31) You are given a string s
# Task
# Write a function that checks whether the string is a palindrome,
# ignoring case and spaces.
# Do NOT use slicing (s[::-1])
# Do NOT use extra libraries
# Return True or False
# Examples
# "madam"                → True
# "Never odd or even"    → True
# "Hello"                → False
# ""                     → True
# Function signature
# def is_palindrome(s):
#     pass

# Rules

# Use basic Python only

# Be ready to explain time & space complexity

# Clean, readable logic


# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     left = 0
#     right = len(s)-1
#     while left < right:
#         if s[left]!=s[right]:
#            return False
#         left +=1
#         right-=1
#     return True

# print(is_palindrome("Never odd or even"))
# print(is_palindrome("madam"))
# print(is_palindrome("Hello"))
# print(is_palindrome(""))





#!Q32) Topic: List + Two Pointers (Very common)
# You are given a sorted list of integers nums and an integer target.
# Task
# Write a function that returns the indices (0-based) of two numbers whose sum equals target.
# Constraints:
# Exactly one valid pair exists
# You must use the two-pointer approach
# Time complexity should be O(n)
# Do NOT use extra data structures (no dict/set)
# Examples
# nums = [1, 2, 3, 4, 6]
# target = 6
# output = (1, 3)   # nums[1] + nums[3] = 2 + 4 = 6
# nums = [2, 7, 11, 15]
# target = 9
# output = (0, 1)
# Function signature
# def two_sum_sorted(nums, target):
#     pass
# Rules
# Use two pointers
# No nested loops
# Be ready to explain time & space complexity

# def two_sum_sorted(nums, target):
#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         current_sum = nums[left] + nums[right]

#         if current_sum == target:
#             return (left, right)
#         elif current_sum < target:
#             left += 1
#         else:
#             right -= 1

# print(two_sum_sorted( [1, 2, 3, 4, 6],6))




#!Q34) Topic: List + Basic Validation Logic (Backend-style)
# You are given a list of integers nums.
# Task
# Return True if the list contains any duplicate element, otherwise return False.
# Examples
# [1, 2, 3, 4]        → False
# [1, 2, 3, 2]        → True
# [5, 5, 5, 5]        → True
# []                  → False
# Function signature
# def contains_duplicate(nums):
#     pass
# Rules
# Time complexity target: O(n)
# Space complexity: explain clearly
# Do NOT use count() inside a loop
# Clean, readable logic

# def contains_duplicate(nums):
#     freq = {}

#     for val in nums:
#         if val in freq:
#             return True
#         freq[val] = 1

#     return False

# print(contains_duplicate([1, 2, 3, 4]  ))
# print(contains_duplicate( [1, 2, 3, 2]))
# print(contains_duplicate([5, 5, 5, 5]  ))
# print(contains_duplicate([]  ))


#!Q35) You are given an unsorted list of integers nums.
# Task
# Return the length of the longest consecutive sequence.
# Sequence elements must be consecutive numbers (x, x+1, x+2…)
# Order in the list does NOT matter
# Time complexity target: O(n)
# Examples
# [100, 4, 200, 1, 3, 2]
# → 4
# # Because the longest consecutive sequence is [1,2,3,4]
# [0, -1, 1, 2, -2, 3]
# → 6
# # Sequence: [-2,-1,0,1,2,3]
# []
# → 0
# Function signature
# def longest_consecutive(nums):
#     pass
# Rules
# Do NOT sort the list (that would be O(n log n))
# Target time complexity: O(n)
# Explain space complexity clearly
# Clean and readable logic


# def longest_consecutive(nums):
#     if not nums:
#         return 0

#     num_set = set(nums)
#     longest = 0

#     for num in num_set:
#         if num-1 not  in num_set:
#             current = num
#             length = 1

#             while current+1 in num_set:
#                 current+=1
#                 length+=1

#             longest = max(longest,length)

#     return longest                                        

# print(longest_consecutive( [0, -1, 1, 2, -2, 3]))
# print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# print(longest_consecutive([]))



#!36Q) Dictionary + Data Aggregation (Very Common in Backend)
# You are given a list of dictionaries representing user transactions:
# transactions = [
#     {"user": "A", "amount": 100},
#     {"user": "B", "amount": 200},
#     {"user": "A", "amount": 300},
#     {"user": "C", "amount": 50},
#     {"user": "B", "amount": 100}
# ]
# 🧠 Task
# Return a dictionary where:
# Key = user
# Value = total amount spent by that user
# Expected Output
# {
#     "A": 400,
#     "B": 300,
#     "C": 50
# }
# Function signature
# def aggregate_transactions(transactions):
#     pass


# def aggregate_transactions(transactions):
#                 res = {}
#                 for t in transactions:
#                         user = t["user"]
#                         amount = t["amount"]

#                         if user in res:
#                                 res[user] += amount
#                         else:
#                                 res[user] = amount
#                 return res

# transactions = [
#     {"user": "A", "amount": 100},{"user": "B", "amount": 200},{"user": "A", "amount": 300},{"user": "C", "amount": 50},{"user": "B", "amount": 100}
# ]
# print(aggregate_transactions(transactions))



# def aggregate_transactions(transactions):
#     res = {}
#     for t in transactions:
#         user = t["user"]
#         amount = t["amount"]
#         res[user] = res.get(user, 0) + amount
#     return res
# transactions = [
#     {"user": "A", "amount": 100},{"user": "B", "amount": 200},{"user": "A", "amount": 300},{"user": "C", "amount": 50},{"user": "B", "amount": 100}
# ]
# print(aggregate_transactions(transactions))



#! Q37) You are given a list of API request timestamps (in seconds), sorted in increasing order.\
# Example:
# requests = [1, 2, 3, 4, 10, 11, 12]
# Task
# Implement a function that returns True if more than 3 requests occur within any 5-second window, otherwise return False.
# Example 1
# requests = [1, 2, 3, 4]
# From time 1 to 4 → 4 requests within 5 seconds
# Return:
# True
# Example 2
# requests = [1, 6, 11, 16]
# No 5-second window contains more than 3 requests
# Return:
# False
# Function signature
# def is_rate_limited(requests):
#     pass
# Rules
# Time complexity target: O(n)
# Use efficient logic (no nested loops)
# Clean readable solution
# Explain space complexity


# def is_rate_limited(requests):
#     n = len(requests)

#     if n < 4:
#         return False

#     for i in range(n - 3):
#         if requests[i + 3] - requests[i] <= 5:
#             return True

#     return False

# print(is_rate_limited([1, 2, 3, 4]))
# print(is_rate_limited([1, 2, 3, 4]))



#! Q38) You are given a list of log strings.
# Each log is in this format:
# "IP_ADDRESS - TIMESTAMP"
# Example:
# logs = [
#     "192.168.1.1 - 10",
#     "192.168.1.2 - 15",
#     "192.168.1.1 - 20",
#     "192.168.1.3 - 25",
#     "192.168.1.2 - 30"
# ]
# 🎯 Task
# Write a function:
# def most_active_ip(logs):
#     ...
# Return the IP address that appears the most times.
# If multiple IPs have the same highest frequency, return the one that appears first in the logs.
# Example
# Input:
# logs = [
#     "192.168.1.1 - 10",
#     "192.168.1.2 - 15",
#     "192.168.1.1 - 20",
#     "192.168.1.3 - 25",
#     "192.168.1.2 - 30",
#     "192.168.1.2 - 35"
# ]
# Output:
# "192.168.1.2"
# Constraints
# 1 <= len(logs) <= 10^5
# Each log is valid format
# Target time complexity: O(n)
# No sorting allowed
# What I’ll Evaluate
# String parsing cleanly
# Dictionary usage
# Tie-breaking logic
# Time & space complexity
# Clean code structure

# def most_active_ip(logs):
#             freq = {}
#             max_count = 0
#             res_ip = None
#             for log in logs:
#                     ip = log.split(" - ")[0]
#                     freq[ip] = freq.get(ip,0)+1
#                     if freq[ip]>max_count:
#                             max_count= freq[ip]
#                             res_ip = ip
#             return res_ip

                    
# logs = [
#     "192.168.1.1 - 10",
#     "192.168.1.2 - 15",
#     "192.168.1.1 - 20",
#     "192.168.1.3 - 25",
#     "192.168.1.2 - 30",
#     "192.168.1.2 - 35"
# ]
# print(most_active_ip(logs))



#!Q39) You are building a Django backend that receives user registration payloads.
# Each payload is a dictionary like:
# users = [
#     {"username": "alice", "email": "a@gmail.com", "age": 22},
#     {"username": "bob", "email": "b@gmail.com", "age": 17},
#     {"username": "alice", "email": "c@gmail.com", "age": 25},
#     {"username": "dave", "email": "d@gmail.com", "age": 30},
#     {"username": "eve", "email": "e@gmail.com", "age": 16}
# ]
# 🎯 Task
# Write a function:
# def validate_users(users):
# Return a list of valid usernames.
# A user is valid if:
# Age ≥ 18
# Username is unique (no duplicates allowed)
# Expected Output for Above Example
# ["alice", "dave"]
# Explanation:
# "bob" → age < 18 ❌
# "alice" appears twice → only first valid one counts
# "eve" → age < 18 ❌
# Rules
# O(n) time
# No sorting
# Do not modify input list
# Clean logic
# No nested loops




# def validate_users(users):
#     seen = set()
#     result = []

#     for user in users:
#         username = user["username"]
#         age = user["age"]

#         if age >= 18 and username not in seen:
#             result.append(username)

#         seen.add(username)

#     return result

# users = [
#     {"username": "alice", "email": "a@gmail.com", "age": 22},
#     {"username": "bob", "email": "b@gmail.com", "age": 17},
#     {"username": "alice", "email": "c@gmail.com", "age": 25},
#     {"username": "dave", "email": "d@gmail.com", "age": 30},
#     {"username": "eve", "email": "e@gmail.com", "age": 16}
# ]
# print(validate_users(users))



#!Q40) You are building a reporting API.

# You receive a list of orders:

# orders = [
#     {"order_id": 1, "user": "A", "amount": 100},
#     {"order_id": 2, "user": "B", "amount": 200},
#     {"order_id": 3, "user": "A", "amount": 50},
#     {"order_id": 4, "user": "C", "amount": 300},
#     {"order_id": 5, "user": "B", "amount": 100},
# ]
# 🎯 Task
# Write a function:

# def get_top_user(orders):

# Return the user who has spent the highest total amount.

# If multiple users have the same highest total, return the one whose total reached that value first.

# Expected Output for Above Example
# "C"

# Because:

# A → 150

# B → 300

# C → 300

# B reached 300 at order 5.
# C reached 300 at order 4.
# So C wins (reached first).

# Rules

# O(n)

# No sorting

# No nested loops

def get_top_user(orders):
    totals = {}
    max_total = 0
    result_user = None

    for order in orders:
        user = order["user"]
        amount = order["amount"]

        totals[user] = totals.get(user, 0) + amount

        if totals[user] > max_total:
            max_total = totals[user]
            result_user = user

    return result_user
                

orders = [
    {"order_id": 1, "user": "A", "amount": 100},
    {"order_id": 2, "user": "B", "amount": 200},
    {"order_id": 3, "user": "A", "amount": 50},
    {"order_id": 4, "user": "C", "amount": 300},
    {"order_id": 5, "user": "B", "amount": 100},
]
print(get_top_user(orders))