


class Solution:
    def findRelativeRanks(self, score):
        original_score = score[:]  
        
        for i in range(len(score)):
            for j in range(i + 1, len(score)):
                if score[i] > score[j]:
                    score[i], score[j] = score[j], score[i]

        sorted_score = score[::-1]

        rank_map = {}
        for index, val in enumerate(sorted_score):
            if index == 0:
                rank_map[val] = "Gold Medal"
            elif index == 1:
                rank_map[val] = "Silver Medal"
            elif index == 2:
                rank_map[val] = "Bronze Medal"
            else:
                rank_map[val] = str(index + 1)

        return [rank_map[val] for val in original_score]

s = Solution()
score = [5, 4, 3, 2, 1]
print(s.findRelativeRanks(score))
