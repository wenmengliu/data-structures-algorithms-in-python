class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ssum = sum(nums)
        if ssum < target:
             return 0
        
        kMaxN = 2 * ssum + 1
        kOffset = ssum
        dp = [0] * kMaxN
        dp[kOffset] = 1
        
        for num in nums:
            temp = [0] * kMaxN
            for i in range(num, kMaxN - num):
                if dp[i]:
                    temp[i + num] += dp[i]
                    temp[i - num] += dp[i]
            temp, dp = dp, temp
        
        return dp[kOffset + target]
            
# TC: O(n * sum)
# SC: O(sum) 
# trasfter function: dp[i][j] += dp[i-1][j-nums[i]] or dp[i][j] += dp[i-1][j+nums[i]]