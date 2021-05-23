class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def dfs(path,sub):
            if not sub:
                res.append(path)
                return
           
            for i in range(1, len(sub)+1):
                if self.is_Valid(sub[:i]):
                    dfs(path + [sub[:i]], sub[i:])
            
        dfs([], s)
        
        return res
    
    def is_Valid (self, s):
        return  s == s[::-1]