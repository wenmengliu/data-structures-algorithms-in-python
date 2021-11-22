class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for idx, point in enumerate(points):
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(max_heap, [-dist, point])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        return [r[1] for r in max_heap]