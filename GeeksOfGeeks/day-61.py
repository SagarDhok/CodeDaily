
# Remove Duplicates from unsorted array

class Solution:
    def removeDuplicate(self, arr):

            st = set()
            lst = []
            for i in arr:
                if i not in st:
                    lst.append(i)
                    st.add(i)   
            return lst

s = Solution()
print(s.removeDuplicate([1, 2, 3, 1, 4, 2]))
print(s.removeDuplicate( [1, 2, 3, 4]))