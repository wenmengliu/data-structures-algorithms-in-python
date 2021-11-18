class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        max_heap = []
        def helper(num):
            heapq.heappush(max_heap, -num)
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        for x in range(1, int(n ** 0.5) + 1):
            if n % x == 0:
                helper(x)
                if x != n//x:
                    helper(n//x)
        return -heapq.heappop(max_heap) if k == len(max_heap) else -1