class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        window_start = 0
        count_repeat_ones = 0
        ans = 0
        
        for window_end, num in enumerate(nums):
            if num == 1:
                count_repeat_ones += 1
            
            if window_end - window_start + 1 - count_repeat_ones > k:
                if nums[window_start] == 1:
                    count_repeat_ones -= 1
                window_start += 1
            
            ans = max(ans, window_end - window_start + 1)
        return ans