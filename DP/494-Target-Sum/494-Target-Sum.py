class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 0-1 knapsack
        total = sum(nums)
        if total < abs(target) or (total + target)%2:
            return 0
        
        capacity = (total + target)//2
        dp = [0] * (capacity + 1)
        dp[0] = 1
        
        for num in nums:
            for j in range(capacity, num - 1, -1):
                dp[j] = dp[j] + dp[j - num]
        return dp[capacity]
       
# TC: O(n * sum)
# SC: O(sum) 
# trasfter function: dp[i][j] = dp[i-1][j] + dp[i-1][j-num]
# dp[i][j] means for the first ith items to get capacity j