class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        q = collections.deque([[0, 0]]) # nums, prefix_sum
        modulo = 10 ** 9 + 7
        res = 0
        nums.append(0) # edge case: nums itself is an increasing stack 
        for n in nums:
            prefix_sum = 0
            while q and q[-1][0] >= n:
                prefix_sum +=  q[-1][1]
                res = max(res, q[-1][0] * prefix_sum)
                # pop out
                q.pop()
            # pop in for mono stack
            prefix_sum += n
            q.append([n, prefix_sum])
        return res % modulo