class Solution:
    def __init__(self):
        self.ans = 1
    def maxUniqueSplit(self, s: str) -> int:  
        def dfs(pos):
            if pos == n:
                self.ans = max(self.ans, len(visited))
                return
            
            for i in range(pos, n):
                ss = s[pos:i+1]
                if ss not in visited:
                    visited.add(ss)
                    dfs(i+1)
                    # backtracking
                    visited.remove(ss)
        
        visited = set()
        n = len(s)
        dfs(0)
        return self.ans