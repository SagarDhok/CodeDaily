

#! Tywin's War Strategy
import math
class Solution:
    def minSoldiers(self, arr, k):
       required = math.ceil( len(arr)/2)

       lucky = 0
       add_list = []
       
       
       for x in arr:
              if x % k == 0:
                lucky += 1
              else:
                  add_list.append(k - (x % k))  
                  
       if lucky >= required:
        return 0 
        
       add_list.sort()
       soldiers_needed = sum(add_list[:required - lucky])
       return soldiers_needed