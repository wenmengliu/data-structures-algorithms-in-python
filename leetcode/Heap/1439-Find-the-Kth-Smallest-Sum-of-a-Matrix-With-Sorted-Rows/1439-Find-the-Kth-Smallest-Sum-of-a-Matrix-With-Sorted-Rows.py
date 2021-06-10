class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        res = mat[0]
        for i in range(1, m):
            res = self.kSmallestPairs(res, mat[i], k)
        return res[k-1]
    
    def kSmallestPairs(self, nums1, nums2, k):
            res = []
            h = []
            if len(nums1) == 0 or len(nums2) == 0 or k == 0:
                return res
            i = 0 
            while i < len(nums1) and i < k:
                heapq.heappush(h, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))
                i += 1
            while k and h:
                cur = heappop(h)
                res.append(cur[0])
                if cur[3] == len(nums2) - 1:
                    continue
                heapq.heappush(h, (cur[1] + nums2[cur[3] + 1], cur[1], nums2[cur[3] + 1], cur[3] + 1))
                k -= 1
            return res