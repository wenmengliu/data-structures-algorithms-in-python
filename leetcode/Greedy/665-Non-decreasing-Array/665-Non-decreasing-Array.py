class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n, cnt = len(nums), 1
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                if cnt == 0: return False
                if i==1 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                cnt -= 1
        return True

# TC: O(N)
# SC: O(1)