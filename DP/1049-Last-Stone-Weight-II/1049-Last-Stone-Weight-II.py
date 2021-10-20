class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        ssum = sum(stones)
        target = ssum//2
        
        dp = [0] * (target + 1)
        
        for stone in stones:
            for i in range(target, stone-1, -1):
                dp[i] = max(dp[i-stone] + stone, dp[i])
        
        return ssum - dp[target] - dp[target]

  # TC: O(ns)
  # SC: O(s)
  # dp[i] means for the current weight of i