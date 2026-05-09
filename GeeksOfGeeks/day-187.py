



class Solution:
    
    def maximumMeetings(self, start, end):
        
        meetings = []
        
        for i in range(len(start)):
            meetings.append((end[i], start[i]))
        
        meetings.sort()
        
        count = 1
        last_end = meetings[0][0]
        
        for i in range(1, len(meetings)):
            curr_start = meetings[i][1]
            curr_end = meetings[i][0]
            
            if curr_start > last_end:
                count += 1
                last_end = curr_end
        
        return count
s = Solution()
start= [1, 3, 0, 5, 8, 5]
end =  [2, 4, 6, 7, 9, 9]
print(s.maximumMeetings(start,end))


start = [1, 3, 0, 5, 8, 5]
end =  [2, 4, 6, 7, 9, 9]
print(s.maximumMeetings(start,end))

