class Solution:
    '''
    recursion: brute force method
    TC: O(2**n) n: the number of array elements. The recursive solution takes the form of
    a binary tree where there are 2 possibilities for every array
    SC: O(n) this space will be used to store the recursion stack. We can't have more 
    than n recursive calls on the call stack at any time.
    '''
    def canPartition(self, nums: List[int]) -> bool:
        # edge cases
        if len(nums) < 2 or sum(nums)%2 != 0:
            return False
        
        target = sum(nums)//2
        
        dp = [True] + [False] * target
        
        for i, n in enumerate(nums):
            # reverse finding
            for j in range(target, n-1, -1):
                # transfer state func
                # dp[j] = dp[j] | dp[j - nums[i]]
                dp[j] |= dp[j-n]
        
        return dp[target]