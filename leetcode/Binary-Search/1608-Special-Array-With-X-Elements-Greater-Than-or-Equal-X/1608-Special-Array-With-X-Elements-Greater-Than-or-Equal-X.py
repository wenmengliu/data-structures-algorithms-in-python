class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # array should be sorted
        nums.sort(reverse=True)
        l = 0
        r = len(nums)
        
        while l < r:
            m = l + (r - l)//2
            if m < nums[m]:
                l = m + 1
            else:
                r = m
        return -1 if l < len(nums) and l == nums[l] else l