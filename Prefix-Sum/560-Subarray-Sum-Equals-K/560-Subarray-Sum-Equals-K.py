class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = collections.Counter()
        hash_map[0] = 1
        cnt = 0
        prefix_sum = 0
        for n in nums:
            prefix_sum += n
            cnt += hash_map[prefix_sum - k]
            hash_map[prefix_sum] += 1
        return cnt