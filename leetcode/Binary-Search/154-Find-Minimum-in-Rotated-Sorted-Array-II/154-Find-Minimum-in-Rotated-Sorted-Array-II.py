class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        if nums[left] < nums[right] or len(nums) == 1:
            return nums[0]
        
        while left < right:
            mid = left + (right - left)//2
            
            if nums[mid] > nums[right]:
                # mid in left
                left = mid + 1
            elif nums[mid] < nums[right]:
                # mid in the right
                right = mid 
            else:
                # duplicated cases
                right -= 1
        
        return nums[left]