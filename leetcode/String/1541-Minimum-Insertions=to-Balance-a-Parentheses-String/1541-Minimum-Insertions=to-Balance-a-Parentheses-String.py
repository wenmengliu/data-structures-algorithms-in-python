class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace('))','*')
        res = l = 0
        for c in s:
            if c == '(':
                l += 1
            else:
                if c == ')':
                    # it needs to add one right )
                    res += 1      
                if l:
                    # to match ) or ))
                    l -= 1
                else:
                    # add one left ( to match ) or ))
                    res += 1
        
        return res + l * 2