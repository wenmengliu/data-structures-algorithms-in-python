class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        m = max(instructions) + 1
        nums = [0] * m
        
        def update(i):
            while i < m:
                nums[i] += 1
                i += (i & -i)
        
        def query(i):
            res = 0
            while i:
                res += nums[i]
                i -= (i & -i)
            return res
        
        res = 0
        for i, j in enumerate(instructions):
            res += min(query(j-1), i - query(j))
            update(j)
        return res % (10**9 + 7)

# Time O(NlogM), M is the maximum of instructions
# Space O(M)