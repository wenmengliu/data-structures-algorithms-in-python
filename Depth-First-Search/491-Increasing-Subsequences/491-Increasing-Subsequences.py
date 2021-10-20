class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, cur, res):
            if len(cur) > 1:
                res.add(cur)
            for i in range(idx, n):
                if not cur or cur[-1] <= nums[i]:
                    dfs(i+1, cur + (nums[i],), res)
        res = set()
        n = len(nums)
        dfs(0, (), res) # use tuple to be hashable
        return res