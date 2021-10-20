class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        m = len(costs)
        n = len(costs[0])
        
        dp = [[0] * n for _ in range(m)]
        dp[0] = costs[0]
        
        for i in range(1, m):
            for j in range(n):
                prev_costs = dp[i-1][:j] + dp[i-1][j+1:]
                
                dp[i][j] = min(prev_costs) + costs[i][j]
        
        return min(dp[-1])