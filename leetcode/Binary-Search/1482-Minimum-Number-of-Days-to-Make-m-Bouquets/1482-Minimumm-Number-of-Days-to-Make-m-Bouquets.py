class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l, kInf = min(bloomDay), max(bloomDay) + 1
        r = kInf
        while l<r:
            mid = (r-l)//2 + l
            if self.getBouquets(bloomDay, mid, k) >= m:
                r = mid
            else:
                l = mid + 1
        return -1 if l >= kInf else l
        
    def getBouquets(self,bloomDay, m ,k):
        ans=cur=0
        for d in bloomDay:
            if d > m: cur =0
            else:
                cur += 1
                if cur == k:
                    ans += 1
                    cur = 0
        return ans

# TC: O(nlog(max(bloomDay)))
# SC: O(1)