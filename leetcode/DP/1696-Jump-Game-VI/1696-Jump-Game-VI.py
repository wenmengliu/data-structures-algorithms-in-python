class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        """ DP + Compressed deque
        TC: O(N) 
        SC: O(k)
        """
        n = len(nums)
        score = nums[0]
        dq = deque()
        dq.append((0, score))
        for i in range(1, n):
            # pop the old index
            while dq and dq[0][0] < i-k:
                dq.popleft()
            score = nums[i] + dq[0][1]
            # pop the smaller value
            while dq and dq[-1][1] <= score:
                dq.pop()
            dq.append((i, score))
        return score

# for push and pop each element into the deque at most once