class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # sorted unique nums and sorted
        ranks = {v: i + 1 for i, v in enumerate(sorted(nums))}
        res, N = [], len(nums)
        BITree = [0] * (N+1)
        
        def update(i):
            while i <= N:
                BITree[i] += 1
                i += (i & -i)
        
        def query(i):
            s = 0 
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s
        
        # reversed the nums
        for n in reversed(nums):
            # Check how many numbers are smaller than the current number.
            res.append(query(ranks[n] - 1))
            # update the freqs of current number
            update(ranks[n])
        return res[::-1]
        