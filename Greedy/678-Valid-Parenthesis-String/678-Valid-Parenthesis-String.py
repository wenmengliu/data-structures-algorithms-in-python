class Solution:
    def checkValidString(self, s: str) -> bool:
        # cmin: the minimum count of open parenthesis
        # cmax: the maximum count of open parenthesis
        cmin = cmax = 0
        for _s in s:
            cmax = cmax - 1 if _s == ')' else cmax + 1 
            cmin = cmin + 1 if _s == '(' else max(cmin - 1, 0)
            if cmax < 0: return False
        return cmin == 0