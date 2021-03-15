class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x[1])
    
        cnt, end, n = 1, intervals[0][1], len(intervals)
        
        for i in range(1, n):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                cnt += 1
        
        return n-cnt