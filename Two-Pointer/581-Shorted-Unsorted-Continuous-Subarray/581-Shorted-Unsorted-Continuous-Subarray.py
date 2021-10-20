class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = sorted(nums) # O(nlogn)
        start, end, n = len(nums)-1, 0, len(nums)
        # tc: O(n)
        for i in range(n):
            if nums[i] != temp[i]:
                start = min(start, i)
                end = max(end, i)
        # equal sign for single element
        if start >= end:
            return 0
        else:
            return end - start + 1