class Solution:
    def balancedString(self, s: str) -> int:
        res = n = len(s)
        count = Counter(s)
        flag = 0
        for k, v in count.items():
            if v != n/4: flag = 1
        if flag == 0: return 0
        start = 0
        for end, c in enumerate(s):
            count[c] -= 1
            while start <n and all(count[_c] <= n/4 for _c in 'QWER'):
                res = min(res, end-start+1)
                count[s[start]] += 1
                start += 1
        return res