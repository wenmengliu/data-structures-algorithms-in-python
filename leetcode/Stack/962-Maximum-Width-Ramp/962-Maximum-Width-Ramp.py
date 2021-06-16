class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        s = []
        res = 0
        
        # first scan nums to get decreasing stack
        for i, n in enumerate(nums):
            if not s or nums[s[-1]] > n:
                s.append(i)
        # reverse the nums to compare
        for j in range(len(nums))[::-1]:
            while s and nums[s[-1]] <= nums[j]:
                res = max(res, j - s.pop())
        return res