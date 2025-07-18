


#! 812. Largest Triangle Area
from itertools import combinations
def triangle_area(a,b,c):
        x1,y1 = a
        x2,y2 = b
        x3,y3 = c
        return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

def largestTriangleArea(points):
                max_area = 0
                for a, b, c in combinations(points, 3):
                        area = triangle_area(a, b, c) 
                        max_area = max(max_area, area)
                return max_area


points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
print(largestTriangleArea(points))  

