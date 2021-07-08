class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in nums]
        prefix, suffix = 1, 1
        for i in range(len(nums)):
            ans[i] *= prefix
            ans[~i] *= suffix
            prefix *= nums[i]
            suffix *= nums[~i]
        return ans