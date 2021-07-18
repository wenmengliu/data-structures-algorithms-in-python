class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        # sort the array to deal with the duplicated elements
        nums.sort()
        n = len(nums)
        used = [0 for _ in range(n)]
        cur = []
        ans = 0
        
        def dfs():
            if len(cur) == n:
                nonlocal ans
                ans += 1 
                return
        
            for i in range(n):
                if used[i]:
                    continue
                # avoid duplicates
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                    continue
                # prune invalid solutions
                if len(cur) > 0 and self.isSquareful(cur[-1], nums[i]) is False:
                    continue
                
                used[i] = 1
                cur.append(nums[i])
                dfs()
                # backtracking
                cur.pop()
                used[i] = 0
        dfs()
        return ans
    
    def isSquareful(self, x, y):
        s = int(math.sqrt(x + y))
        
        return s ** 2 == x + y