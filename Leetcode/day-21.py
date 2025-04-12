

# Binary Search
def searchInsert(nums, target):
    start = 0
    end = len(nums) - 1
                           
    while start <= end:   
        mid = (start + end) // 2      

        if target == nums[mid]:      
            return mid
        elif target > nums[mid]:     
            start = mid + 1           
        else:
            end = mid - 1

    return start

nums = [int(i) for i in input("Enter List of Values : ").split()]
target = int(input("Enter Which Values Index You want : "))
res  = searchInsert(nums,target)
print(f"Insert Position of {target} : {res}")