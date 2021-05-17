class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda a: a[1] - a[0]) # O(nlogn)
        res = 0
        for a, m in tasks:
            res = max(res+a, m)
        return res