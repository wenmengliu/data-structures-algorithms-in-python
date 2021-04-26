class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # BIT: (nlogn); SC: O(n) for BITS array
        nnums = nums + [n*2 for n in nums]
        snums = sorted(list(set(nnums)))
        tree = BIT(len(snums))
        res = 0
        rank = {j:i+1 for i, j in enumerate(snums)}
        for n in nums[::-1]:
            res += tree.query(rank[n]-1)
            tree.update(rank[n*2])
        return res

        
class BIT:
    def __init__ (self, size):
        self.nums = [0] * (size + 1)
    
    def query (self, i):
        res = 0
        while i:
            res += self.nums[i]
            i -= (i & -i)
        return res
    
    def update(self, i):
        while i < len(self.nums):
            self.nums[i] += 1
            i += (i & -i)