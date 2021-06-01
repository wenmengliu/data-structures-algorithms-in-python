class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        ssum = sum(nums)
        n = len(nums)
        if ssum < x:
            return -1
        if ssum == x:
            return n
        target = ssum - x
        left = curr_sum = max_subarray_size = 0
        for right, num in enumerate(nums):
            curr_sum += num
            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                max_subarray_size = max(max_subarray_size, right - left + 1)
                
        return n - max_subarray_size if max_subarray_size > 0 else -1