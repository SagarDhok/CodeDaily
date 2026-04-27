
#! Zero Converter - Python
# Difficulty: BasicAccuracy: 43.48%Submissions: 114K+Points: 1Average Time: 10m
# You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.

# Note:- You don't have to return anything, you just have to print the array.

# Example 1:

# Input:
# n = 0
# Output:
# already Zero
# Example 2:

# Input:
# n = 4
# Output:
# 3 2 1 0
# Example 3:

# Input:
# n = -3
# Output:
# -3 -2 -1 0
# Your Task:
# This is a function problem. You don't need to take input of test cases. Just complete the functions pos() and neg().

# Constraints:
# -103 <= x <= 103

def pos(n):
    if n > 0:
        for i in range(n-1, -1, -1):
            print(i, end=" ")
print(pos(int(input("Enter A number : "))))

def neg(n):
    if n < 0:
        for i in range(n, 1):
            print(i, end=" ")
print(neg(int(input("Enter A number : "))))
