class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        nextSmaller = [len(nums)] * len(nums)
        stack = []
        # next Smaller element number
        for i, n in enumerate(nums):
            while stack and stack[-1][1] > n:
                nextSmaller[stack.pop()[0]] = i
            stack.append([i, n])
        # end
        # for element that coulnd'd finf a next smaller element, then set it as len(nums)
        return sum([v - i for i, v in enumerate(nextSmaller)])