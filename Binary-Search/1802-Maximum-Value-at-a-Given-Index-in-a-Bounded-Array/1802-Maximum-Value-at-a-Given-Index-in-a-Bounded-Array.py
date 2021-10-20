class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def test(a):
            b = max(a - index, 0)
            res = (a + b) * (a - b + 1) / 2
            b = max(a - ((n - 1) - index), 0)
            res += (a + b) * (a - b + 1) / 2
            return res - a
        
        maxSum -= n
        left, right = 0, maxSum
        while left < right:
            mid = (right + left + 1) // 2
            if test(mid) > maxSum:
                right = mid -1
            else:
                left = mid
        return left + 1