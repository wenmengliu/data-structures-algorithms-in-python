class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:   
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1
        
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                result[i] = nums[right] ** 2
                right -= 1
            else:
                result[i] = nums[left] ** 2
                left += 1
        return result

# Two Pointers method from Merged Two Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:   
        neg_arr = [x ** 2 for x in nums if x < 0]
        pos_arr = [x ** 2 for x in nums if x >= 0]
        
        m, n, k = len(neg_arr), len(pos_arr), len(nums)
        
        left, right = 0, n - 1
        
        while left < m and right >= 0:
            if neg_arr[left] <= pos_arr[right]:
                nums[m - left + right] = pos_arr[right]
                right -= 1
            else:
                nums[m - left + right] = neg_arr[left]
                left += 1
        
        nums[: m - left + right + 1] = neg_arr[left:][::-1] if left < m else pos_arr[:right + 1]
        return nums