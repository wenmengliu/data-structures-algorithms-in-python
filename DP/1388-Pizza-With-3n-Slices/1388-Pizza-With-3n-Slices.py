class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
         # the total of pieces you can get is m // 3
        n = len(slices)//3
        def getMaxSlices(slices):
            m = len(slices)
            dp = [ [0] * (n + 1) for _ in range(m+1)]
            
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    dp[i][j] = max(dp[i-1][j], slices[i-1] + (dp[i-2][j-1] if i > 1 else 0))
            
            return dp[m][n]
        
        return max(getMaxSlices(slices[1:]), getMaxSlices(slices[:-1]))

# TC: O(n x m)
# SC: O(n x m)