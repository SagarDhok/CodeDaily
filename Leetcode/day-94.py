


#! 682. Baseball Game
class Solution:

 def calPoints(operations):
    stack = []

    for op in operations:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))  # safe here
    return sum(stack)





s = Solution()
print(s.calPoints(["5","2","C","D","+"]))          
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))  
print(s.calPoints(["1","C"]))                        
