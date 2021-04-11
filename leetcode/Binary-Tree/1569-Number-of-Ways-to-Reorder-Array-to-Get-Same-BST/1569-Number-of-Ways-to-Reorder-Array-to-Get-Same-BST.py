class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def helper(nums):
            # the elements less than 3, it will be only one way 
            if len(nums) <=2 : return 1
            l = [i for i in nums if i < nums[0]]
            r = [j for j in nums if j > nums[0]]
            # total_ways = combination(l+r,l) * way_left * way_right
            return comb(len(l) + len(r), len(l)) * helper(l) * helper(r)
        return (helper(nums) - 1) % (10**9 + 7)

# TC: O(nlogn) for balanced tree ~ O(n^2) for skewed tree
# SC: O(nlogn) for balanced tree ~ O(n^2) for skewed tree