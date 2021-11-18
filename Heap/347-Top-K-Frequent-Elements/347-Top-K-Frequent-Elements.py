class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1)
        if k == len(nums):
            return nums
        
        # O(N)
        freq = collections.Counter(nums)
        heap = []
      
        # O(NlogK)
        for key, val in freq.items():
            heapq.heappush(heap, [val, key])
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [f[1] for f in heap]