class Solution:
    def _rob(self, nums: List[int]) -> int:
        dp0 = dp1 = 0
        for n in nums:
            dp0, dp1 = dp1, max(dp0 + n, dp1)
        return dp1
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        # for a circle: rob (0 - n-1) or (1 - n)
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))