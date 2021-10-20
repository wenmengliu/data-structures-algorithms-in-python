class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while l<r:
            limit = (r-l)//2 + l
            if self.mini_groups(nums, limit) > m:
                l = limit + 1
            else:
                r = limit
        return l
    
    def mini_groups(self,nums,limit):
        groups, curr_sum = 1, 0
        for num in nums:
            if curr_sum + num > limit:
                groups += 1
                curr_sum = num
            else:
                curr_sum += num
        return groups

# Time complexity: O(log(sum(nums))*n)
# Space complexity: O(1)