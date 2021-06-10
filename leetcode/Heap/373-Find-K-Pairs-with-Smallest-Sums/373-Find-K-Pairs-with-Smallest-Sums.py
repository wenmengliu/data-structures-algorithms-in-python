class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        i = 0 
        h = []
        cnt = k
        while i < k and i < len(nums1):
            heapq.heappush(h, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
            i += 1
    
        while h and k:
            cur = heappop(h)
            if len(res) == cnt:
                break
            res.append([cur[1], cur[2]])
            if cur[3] == len(nums2) - 1:
                continue
            heapq.heappush(h, (cur[1] + nums2[cur[3] + 1], cur[1], nums2[cur[3] + 1], cur[3] + 1))
            k -= 1
        return res