class Solution:
    def jump(self, nums: List[int]) -> int:
        steps, near = 0, 0
        far, n = nums[0], len(nums)
        for i in range(n):
            if i > near:
                steps += 1
                near = far
            far = max(far, i+nums[i])
        return steps

# TC: O(n)
# SC: O(1)