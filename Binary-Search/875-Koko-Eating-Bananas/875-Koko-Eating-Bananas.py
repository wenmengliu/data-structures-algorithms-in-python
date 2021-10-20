class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)+1
        while l < r:
            m = (r-l)//2 + l
            sumH = 0
            for p in piles:
                sumH += (p+m-1)//m
            if sumH <= h:
                r = m
            else:
                l  = m + 1
        return l

# TC: O(nlogH)
# SC: O(1)
# return l means it must have a solution