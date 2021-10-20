class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """ Binary Search
        
        TC: O(logn)
        SC: O(1)
        
        Arguments:
            citations {List[int]} -- [description]
        
        Returns:
            int -- [description]
        """
        n = len(citations)
        l, r = 0, n 
        while l < r:
            mid = l + (r-l)//2
            # find the smallest idx
            if mid + citations[mid] >= n:
                r = mid 
            else:
                l = mid + 1
        return n - l