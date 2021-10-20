class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        l, r = toBeRemoved[0], toBeRemoved[1]
        for interval in intervals:
            if interval[0] >= r or interval[1] <= l:
                ans.append(interval)
            else:
                if interval[0] < l:
                    ans.append([interval[0], l])
                if interval[1] > r:
                    ans.append([r, interval[1]])
        
        return ans