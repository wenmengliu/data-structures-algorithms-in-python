class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap, stack, res = {}, [], []
        for n in nums2:
            while len(stack) and n > stack[-1]:
                hashmap[stack.pop(-1)] = n
            stack.append(n)
        
        for i in nums1:
            res.append(hashmap.get(i, -1))
        
        return res

## SC: O(n+m): stack and hashmap of size n and res of size m
## TC: O(n+m) The entired nums2 of size n is scanned only once. The stack's n elements are poped up only once. The entired nums1 (findNums) is also scanned only once.