class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        """ recursion with memorization Top down
        TC: O(nd + nlogn)
        SC: O(n)
        """
        n = len(arr)
        dp = [1] * n
        for i, a in sorted(enumerate(arr), key = lambda x: x[1]):
            for di in [-1, 1]:
                for j in range(i + di, i + di*d + di, di):
                    if not(0 <= j <n and a > arr[j]): break
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)