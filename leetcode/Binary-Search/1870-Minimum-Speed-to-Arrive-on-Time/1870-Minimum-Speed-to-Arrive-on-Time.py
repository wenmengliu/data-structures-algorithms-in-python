import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        lo, n = 1, len(dist)
        # the function to calcute total time consumed
        total = lambda speed: sum(map(lambda x: ceil(x/speed), dist[:-1])) + dist[-1]/speed
        # the highest speed
        hi = max(max(dist), ceil(dist[-1]/0.01))
        if total(hi) > hour:
            return -1
        
        while lo < hi:
            speed = lo + (hi - lo) // 2
            need = total(speed)
            if need > hour:
                lo = speed + 1 # to find a large one
            else:
                hi = speed # explore a smaller one
        return lo