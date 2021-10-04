class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4 or sum(matchsticks) % 4 != 0:
            return False
        
        target = sum(matchsticks)//4
        
        visited = [False] * len(matchsticks)
        matchsticks.sort(reverse = True)
        n = len(visited)
        
        def dfs( curPos, curGroup, curSum):
            if curGroup == 4:
                return True
            if curSum > target:
                return False 
            if curSum == target:
                return dfs(0, curGroup + 1, 0)
            
            last = -1
            for i in range(curPos, n):
                if last == i:
                    continue
                if visited[i]:
                    continue
                visited[i] = True
                last = i
                if dfs(i, curGroup, curSum + matchsticks[i]):
                    return True
                visited[i] = False
            return False
        
        return dfs(0,0,0)