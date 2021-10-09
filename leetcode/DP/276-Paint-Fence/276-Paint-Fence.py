class Solution:
    def numWays(self, n: int, k: int) -> int:
        # top_down memory
        memo = {}
        
        def dp(i):
            if i == 1:
                return k
            if i == 2:
                return k ** 2
            
            if i in memo:
                return memo[i]
            
            memo[i] = (k-1) * (dp(i-1) + dp(i-2))
            
            return memo[i]
        
        return dp(n)