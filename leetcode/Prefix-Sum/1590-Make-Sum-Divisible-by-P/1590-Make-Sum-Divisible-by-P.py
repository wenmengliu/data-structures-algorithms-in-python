class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        r = sum(nums) % p
        if r == 0: return 0
        m = {0: -1}
        ans = len(nums)
        s = 0
        for i, n in enumerate(nums):
            s = (s + n) % p
            t = (s - r) % p
            if t in m:
                ans = min(ans, i - m[t])
            m[s] = i
        
        return -1 if ans == len(nums) else ans