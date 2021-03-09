class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # sort intervals O(nlong)
        intervals.sort(key = lambda x: x[0])
        
        heap = []
        for i in intervals:
            if heap and i[0]>=heap[0]:
                # two intervals can use the same room
                heapq.heapreplace(heap, i[1])
            else:
                heapq.heappush(heap, i[1])
        return len(heap)