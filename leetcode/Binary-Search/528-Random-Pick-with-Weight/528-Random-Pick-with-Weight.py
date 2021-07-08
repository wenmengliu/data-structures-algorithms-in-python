class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        self.total = 0
        for _w in w:
            self.total += _w
            self.prefix_sum.append(self.total)
        
    def pickIndex(self) -> int:
        t = self.total * random.random()
        # binary search
        left, right = 0, len(self.prefix_sum)-1
        
        while left < right:
            mid = left + (right - left) // 2
            if self.prefix_sum[mid] == t: return mid
            elif self.prefix_sum[mid] > t:
                right = mid
            else:
                left = mid + 1 
        return left 