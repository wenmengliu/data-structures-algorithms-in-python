class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        if 6 * min(l1,l2) < 1 * max(l1, l2):
            return -1
        
        if sum(nums1) == sum(nums2):
            return 0
        # to make sure sum of nums1 is smaller than that of nums2, otherwise switch nums1 with nums2.
        # then nums1 sort ascending and nums2 sort descending
        if sum(nums1) > sum(nums2):
            nums1.sort(reverse=True)
            nums2.sort()
            return self.calOps(nums2, nums1)
        nums1.sort()
        nums2.sort(reverse=True)
        return self.calOps(nums1, nums2)
    
    def calOps(self, nums1, nums2):
        n, m, i, j = len(nums1), len(nums2), 0, 0
        ans = 0
        s1, s2 = sum(nums1), sum(nums2)
        
        while s1 < s2:
            d1 = 6 - nums1[i] if i < n else 0
            d2 = nums2[j] - 1 if j < m  else 0
            if d1 < d2:
                s2 -= d2
                j += 1
            else:
                s1 += d1
                i += 1
            ans += 1
        return ans
        