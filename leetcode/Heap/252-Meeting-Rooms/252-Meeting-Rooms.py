class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        
        heap = []
        
        for i in intervals:
            if heap:
                if i[0] < heap[0]:
                    return False
                else:
                    heapq.heapreplace(heap, i[1])
            else:
                heapq.heappush(heap, i[1])
        
        return True