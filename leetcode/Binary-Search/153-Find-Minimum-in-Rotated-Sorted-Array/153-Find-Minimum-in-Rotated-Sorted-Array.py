class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[-1]
        
        left, right = 0, len(nums) - 1
        
        if nums[left] < nums[right]:
            return nums[0]
        
        while left < right:
            mid = left + (right - left)//2
            
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]