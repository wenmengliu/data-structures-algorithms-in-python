class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        dp1, dp2 = 0, 0
        while i < n1 or j < n2:
            if i < n1 and j < n2 and nums1[i] == nums2[j]:
                dp1=dp2= max(dp1,dp2) + nums1[i]
                i += 1
                j += 1
            elif i<n1 and (j==n2 or nums1[i] < nums2[j]):
                dp1 += nums1[i]
                i += 1
            else:
                dp2 += nums2[j]
                j += 1
        return max(dp1,dp2) % (10**9+7)
# TC: O(n)
# SC: O(1)