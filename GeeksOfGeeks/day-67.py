
# Jay's Apples

class Solution:
    def minimumApple(self, arr):
        unique_persons = {}

        for person in arr:
            unique_persons[person] = True

        count = 0
        for person in unique_persons:
            count += 1

        return count


s = Solution()
arr = [1, 1, 1, 1, 1]
print(s.minimumApple(arr))


arr = [1, 2, 3, 1, 2]
print(s.minimumApple(arr))