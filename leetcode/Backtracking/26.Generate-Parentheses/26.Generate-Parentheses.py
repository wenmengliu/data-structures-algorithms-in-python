class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(s, left, right):
            if len(s) == 2*n:
                res.append(s)
                return 

            if left < n:
                dfs (s+'(', left+1, right)

            if right< left:
                dfs(s + ')', left, right+1)
                
        s, left, right = "", 0, 0
        dfs(s, left, right)
        
        return res