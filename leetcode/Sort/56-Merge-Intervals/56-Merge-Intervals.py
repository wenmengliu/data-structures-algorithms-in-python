class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort O(nlogn) SCL O(nlogn)
        intervals.sort(key = lambda x: x[0])
        
        merge = []
        
        for i in intervals:
            if merge and i[0] <= merge[-1][1]:
                ## there is overlap, then we merge
                merge[-1][1] = max(merge[-1][1], i[1])
            else:
                merge.append(i)
                
        return merge