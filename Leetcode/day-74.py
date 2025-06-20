

# Container With Most Water

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        max_water = max(max_water, min(height[left], height[right]) * width)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

height1 = [1,8,6,2,5,4,8,3,7]
print(maxArea(height1))  

height2 = [1,1]
print(maxArea(height2)) 
