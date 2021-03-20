class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        events = {}
        for x1, y1, x2, y2 in rectangles:
            events.setdefault(y1, []).append((1, x1, x2)) # start this interval
            events.setdefault(y2, []).append((0, x1, x2)) # end this interval
        events = sorted(events.items(), key=lambda x: x[0])
        area = 0
        intervals = []
        last_y = events[0][0]
        width = 0
        for y, event in events:
            area += width * (y - last_y)
            for start, x1, x2 in event:
                if start:
                    intervals.append((x1,x2))
                else:
                    intervals.remove((x1,x2))
            width = self.merge_interval(intervals)
            last_y = y
        return area % (10**9 + 7)
    
    def merge_interval(self, intervals):
        if not intervals:
            return 0
        intervals.sort()
        end = intervals[0][1]
        total = intervals[0][1] - intervals[0][0]
        for l, r in intervals:
            if l < end and r > end:
                total += r - end
                end = r
            if l>=end:
                total += r - l
                end = r
        return total