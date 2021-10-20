class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = nums[::-1]
        n = len(nums)
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res