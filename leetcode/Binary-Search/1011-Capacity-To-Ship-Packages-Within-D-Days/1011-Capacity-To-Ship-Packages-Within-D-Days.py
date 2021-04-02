class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights)
        r = sum(weights) + 1
        while l < r:
            m = (r-l)//2 + l
            d = 1
            t = 0
            for w in weights:
                t += w
                if (t) > m:
                    t = w
                    d += 1
            if d <= D:
                r = m
            else:
                l = m + 1
        return l

# TC: O(n*log(sum(weights)))
# SC: O(1)