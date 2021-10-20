class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(visited, idx, cnt):
            if idx > n:
                cnt += 1
                return cnt
            
            for i in range(1, n+1):
                if (not visited[i-1] and (i % idx == 0 or idx % i == 0)):
                    visited[i-1] = True
                    cnt = dfs(visited, idx+1, cnt)
                    ## backtracking
                    visited[i-1] = False
                
            return cnt
        
        visited = [False] * n
        idx, cnt = 1, 0
        
        return dfs(visited, idx, cnt)