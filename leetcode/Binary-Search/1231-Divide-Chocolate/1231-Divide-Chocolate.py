class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        l, r = 1, sum(sweetness)//(K+1)
        while l<r:
            m = (r-l)//2 + l
            cur = cuts = 0
            for s in sweetness:
                cur += s
                if cur > m:
                    cuts += 1
                    cur = 0
            if cuts <= K:
                r = m
            else:
                l = m + 1
        return int(l)   