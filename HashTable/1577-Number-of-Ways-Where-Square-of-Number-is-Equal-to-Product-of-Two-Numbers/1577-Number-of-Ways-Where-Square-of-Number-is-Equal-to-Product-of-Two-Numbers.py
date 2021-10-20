class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def helper(nums1, nums2):
            unordered_map = Counter([x**2 for x in nums1])
            counter = Counter()
            ans = 0
            for x in nums2:
                for y, c in counter.items():
                    if y*x in unordered_map.keys():
                        ans += c * unordered_map[y*x]
                counter[x] += 1
            return ans
        return helper(nums1, nums2) + helper(nums2, nums1)