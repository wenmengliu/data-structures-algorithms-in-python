class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.lower_bound(nums, target), self.upper_bound(nums,target)]
        
    # Find First Position of Element in Sorted Array -> in Left interval
    def lower_bound(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left)//2 # l: 0, r: 1
            
            if nums[mid] < target:
                left = mid + 1
            
            elif nums[mid] > target:
                right = mid - 1
            
            else:
                right = mid
        
        if left == right and nums[left] == target:
            return left
        return -1
    
    def upper_bound(self, nums,target):
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = right - (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            
            elif nums[mid] > target:
                right = mid - 1
            
            else: 
                left = mid
        
        if left == right and nums[left] == target:
            return left
        return -1