class Solution:
    def rob(self, nums: List[int]) -> int:
        dp0 = dp1 = 0
        for i in range(len(nums)):
            dp0, dp1 = dp1, max(dp0+nums[i],dp1)
        return dp1