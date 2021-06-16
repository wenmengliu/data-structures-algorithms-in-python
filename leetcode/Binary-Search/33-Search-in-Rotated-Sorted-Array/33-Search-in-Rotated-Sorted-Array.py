class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # search space [l, r]
        left, right = 0, len(nums)   
        # 通过nums[left], nums[mid] 与 target关系， 来确定三者之间的关系
        while left < right:
            mid = left + (right - left)//2
            if target == nums[mid]:
                return mid
             # 在同一个区间
            if (nums[left] <= nums[mid] and nums[left] <= target) or (nums[left] > nums[mid] and nums[left] > target):
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            # 不在同一个区间
            elif (nums[left] <= nums[mid] and nums[left] > target):
                left = mid + 1
            elif (nums[left] > nums[mid] and nums[left] <= target):
                right  = mid
        return -1