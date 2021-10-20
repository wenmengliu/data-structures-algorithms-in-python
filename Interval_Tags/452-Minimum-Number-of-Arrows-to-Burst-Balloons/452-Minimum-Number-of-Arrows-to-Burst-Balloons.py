class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==0: return 0
        points.sort(key = lambda x: x[1])
        ans = 1
        right = points[0][1]
        for i in range(1, len(points)):
            cur = points[i]
            if cur[0] <= right:
                continue
            else:
                right = cur[1]
                ans += 1
        
        return ans