class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg, ans = 0, 0, 0
        
        for n in nums:
            if n < 0:
                pos, neg = neg + 1 if neg else 0, pos + 1
            elif n > 0:
                pos, neg = pos + 1, neg + 1 if neg else 0
            else:
                pos, neg = 0, 0 
            ans = max(ans, pos)
        return ans