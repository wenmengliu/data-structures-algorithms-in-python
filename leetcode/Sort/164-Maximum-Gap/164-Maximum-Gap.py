class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """Bucket Sorting
        
        TC: O(n)
        SC: O(b) b is number of buckets
        
        Arguments:
            nums {List[int]} -- [description]
        
        Returns:
            int -- [description]
        """

        # bucket sorting 
        if len(nums) < 2 or min(nums)==max(nums): return 0
        a, b = min(nums), max(nums)
        size = (b-a)//(len(nums)-1) or 1
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        
        for n in nums:
            b = bucket[(n-a)//size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        # filter out bucket when b[0] is None
        bucket = [b for b in bucket if b[0] is not None]
        
        return max(bucket[i][0] - bucket[i-1][1] for i in range(1, len(bucket)))