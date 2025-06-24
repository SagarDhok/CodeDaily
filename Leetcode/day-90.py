



# 599. Minimum Index Sum of Two Lists
class Solution:
    def findRestaurant(self, list1,list2):
        res  = {}
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    res[list1[i]]= i+j

        minv = min(res.values())

        ans = []
        for val in res:
            if res[val]==minv:
                ans.append(val)
        return ans
    
s  = Solution()
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter"]
s.findRestaurant(list1,list2)

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
s.findRestaurant(list1,list2)