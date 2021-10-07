class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        l, r = min(nums), max(nums)
        points = [0] * (r - l + 1)
        # rank points array aesc
        # reduction
        for num in nums:
            points[num - l] += num
        return self.rob(points)
    
    def rob(self, points):
        dp0 = dp1 = 0
        
        for point in points:
            dp0, dp1 = dp1, max(dp0 + point, dp1)
        
        return dp1

# TC: O(r + n)
# SC: O(r)
# r = max(nums) - min(nums) + 1
# transfer function rob[k] = max(rob[k-2] + nums[k], rob[k-1])