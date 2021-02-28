class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # sorting nums and queries
        nums.sort()
        queries =  sorted((q2, q1, idx) for idx, (q1,q2) in enumerate(queries))      
        n, trie, i = len(nums), {}, 0
        ans = [-1] * len(queries)
        
        for q1, q2, idx in queries:
            while i < n and nums[i] <= q1:
                trie = self.insert(trie,nums[i])
                i += 1
            if trie:
                ans[idx] = self.query(trie, q2)
        return ans
    
    
    def insert(self, root, num):
        bitsNum = [(num>>i)& 1 for i in range(31,-1,-1)]
        node = root
        for bit in bitsNum:
            if bit not in node:
                node[bit] = {}
            node = node[bit]
        node['#'] = num
        return root
    
    
    def query(self, root, q):
        node = root
        for i in range(31,-1,-1):
            bit = (q>>i) & 1
            toggled_bit = 1 - bit
            node = node.get(toggled_bit) or node.get(bit)
    
        return q^node['#']