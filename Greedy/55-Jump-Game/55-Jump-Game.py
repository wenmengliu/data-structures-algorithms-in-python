class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far, n = nums[0], len(nums)    
        for i in range(n):
            # if current ind is large than far, then break and stop
            # it cannot be reached
            if i > far: break
            # Keep tracking the farthest index you can jump to.
            far = max(far, i + nums[i])
        return far >= n-1

# TC: O(n) we are doing a single pass through the nums array.
# SC: O(1)