 
#! Max Consecutive Ones
def findMaxConsecutiveOnes(nums):
    mc = 0  
    cc = 0  

    for i in nums:
        if i == 1:
            cc += 1
        else:
            if cc > mc:
                mc = cc
            cc = 0

    if cc > mc:
        mc = cc

    return mc

print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))  
print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))  
