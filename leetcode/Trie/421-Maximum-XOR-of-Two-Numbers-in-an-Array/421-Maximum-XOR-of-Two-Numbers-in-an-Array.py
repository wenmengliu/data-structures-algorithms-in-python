class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int: 
        ## convert nums to binary bits with the same L, L is the maximum num bits len
        L = len(bin(max(nums))) - 2
        bitsNums = [[(x>>i) & 1 for i in range(L)][::-1] for x in nums]
        
        trie = {}
        max_xor = 0
        
        for num in bitsNums:
            curr_xor= 0
            node = trie
            xor_node = trie  
            # insert number in trie
            for bit in num:
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
                target_bit = 1 - bit   
                if target_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[target_bit]
                else:
                    curr_xor = (curr_xor <<1)
                    xor_node = xor_node[bit]
                
            max_xor = max(max_xor, curr_xor)
            
        return max_xor