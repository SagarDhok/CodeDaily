

#! N meetings in one room
# Difficulty: EasyAccuracy: 45.3%Submissions: 387K+Points: 2Average Time: 20m
# You are given timings of n meetings in the form of (start[i], end[i]) where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. Return the maximum number of meetings that can be accommodated in a single meeting room, when only one meeting can be held in the meeting room at a particular time. 

# Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

# Examples :

# Input: start[] = [1, 3, 0, 5, 8, 5], end[] =  [2, 4, 6, 7, 9, 9]
# Output: 4
# Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2), (3, 4), (5,7) and (8,9)
# Input: start[] = [10, 12, 20], end[] = [20, 25, 30]
# Output: 1
# Explanation: Only one meetings can be held with given start and end timings.
# Input: start[] = [1, 2], end[] = [100, 99]
# Output: 1
# Constraints:
# 1 ≤ n ≤ 105
# 0 ≤ start[i] < end[i] ≤ 106

class Solution:
    def maxMeetings(self, start, end):
        n = len(start)
        
        meetings = []
        
        for i in range(n):
            meetings.append((start[i], end[i]))
        
        meetings.sort(key=lambda x: x[1])
        
        count = 1
        last_end = meetings[0][1]
        
        for i in range(1, n):
            if meetings[i][0] > last_end:
                count += 1
                last_end = meetings[i][1]
        
        return count

s = Solution()
start = [1, 3, 0, 5, 8, 5]
end =  [2, 4, 6, 7, 9, 9]
print(s.maxMeetings(start,end))