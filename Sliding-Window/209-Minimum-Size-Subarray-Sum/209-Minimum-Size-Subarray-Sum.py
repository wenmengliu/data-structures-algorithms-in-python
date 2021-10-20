class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        window_sum = 0
        start = 0
        n = len(nums) + 1
        ans = n
        for end, num in enumerate(nums):
            window_sum += num
            while window_sum >= s:
                ans = min(ans, end - start + 1)
                # shrink the sliding window
                window_sum -= nums[start]
                start += 1
        
        if ans == n:
            return 0
        return ans % n