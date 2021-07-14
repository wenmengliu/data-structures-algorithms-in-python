global n, res
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, curr):
            res.append(curr)
            if index == n:
                return 
            for i in range(index, n):
                if i > index and nums[i-1] == nums[i]:
                    continue
                dfs(i+1, curr + [nums[i]])
        # sort the array
        nums.sort()
        n = len(nums)
        res = []
        dfs(0,  [])
        
        return res