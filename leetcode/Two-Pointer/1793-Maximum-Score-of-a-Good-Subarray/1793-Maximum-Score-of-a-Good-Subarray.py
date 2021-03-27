class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans = mini = nums[k]
        l, r, n = k, k , len(nums)
        while l>0 or r<n-1:
            if (nums[l-1] if l else 0) < (nums[r+1] if r < n-1 else 0):
                r += 1
            else:
                l -= 1
            mini = min (mini, nums[r], nums[l])
            ans = max(ans, mini * (r-l+1))
        return ans

# TC: O(n)
# SC: O(1)