class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals
        intervals.sort(key = lambda x: (x[0],-x[1]))
        prev_end = cnt = 0
        for i in range(len(intervals)):
            if intervals[i][1] > prev_end:
                prev_end = intervals[i][-1] 
                cnt += 1
        return cnt
# greedy 
# TC O(NlogN) since the soring dominates the complexity of the algoritm
# SC O(N) in python the sorted() function is implemented with the Timsort algorithm whose sc is O(N)
# in Java, the Array.sort() is implemented as a vairant of quicksort algorithm whose SC is O(logN)