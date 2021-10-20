class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        hash_map = collections.Counter()
        hash_map[0] = -1
        prefix_sum = res = 0
        for i, v in enumerate(nums):
            prefix_sum += v
            if (prefix_sum - k) in hash_map:
                res = max(res, i - hash_map[prefix_sum - k])
            if prefix_sum not in hash_map:
                hash_map[prefix_sum] = i
        return res