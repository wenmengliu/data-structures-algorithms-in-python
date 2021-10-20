class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # sort the position
        position.sort()
        def isOK(d):
            n = len(position)
            count = 1
            i = 0
            while i < n:
                j = i
                while j < n and position[j] - position[i] < d:
                    j += 1
                if j == n:
                    break
                else:
                    count += 1
                    i = j
                if count == m:
                    return True
            return False 
        # search spaces
        l, r = 0, position[-1] - position[0] 
        while l < r:
            mid = r - (r - l)//2
            if isOK(mid):
                l = mid # mid might be a possible solution but not optimal
            else:
                r = mid - 1 # guess too large
        return l 
            