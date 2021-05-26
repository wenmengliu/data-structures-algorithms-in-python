class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        counts = [0] * (n + 1)
        counts[0] = 1
        ans = 0
        ssum = 0
        for n in nums:
            ssum += n
            if (ssum >= goal): 
                ans += counts[ssum - goal]
            counts[ssum] += 1
        return ans