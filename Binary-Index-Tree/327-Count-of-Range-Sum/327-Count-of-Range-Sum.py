class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        BITree, sums = [0] * (n+2), [0] * (n+1)
        
        for i in range(n):
            sums[i+1] = sums[i] + nums[i]
        
        def query(i):
            s = 0
            while i:
                s += BITree[i] 
                i -= (i & -i)
            return s
        
        def update(i):
            while i <= n + 1:
                BITree[i] += 1
                i += (i & -i)
        
        sSums, res = sorted(sums), 0
        for j in sums:
            cnt = query(bisect.bisect_right(sSums, j - lower)) - query(bisect.bisect_left(sSums, j - upper))
            res += cnt
            update(bisect.bisect_left(sSums,j) + 1)
        
        return res