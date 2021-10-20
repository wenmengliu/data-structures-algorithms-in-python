class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(key = lambda x1: x1[0])
        slots2.sort(key = lambda x2: x2[0])
        
        i, j = 0, 0
        n, m = len(slots1), len(slots2)
        
        while i < n and j < m:
            start = max(slots1[i][0], slots2[j][0])
            end = min(slots1[i][1], slots2[j][1])
            
            if start + duration <= end:
                return [start, start+duration]

            if start + duration > slots1[i][1]:
                i += 1
            elif start + duration > slots2[j][1]:
                j += 1
        return []