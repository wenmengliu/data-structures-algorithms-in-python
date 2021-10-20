class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        
        for i, _s in enumerate(s):
            # for open parentheses, adding the index
            if _s == '(':
                stack.append(i)
            elif _s == ')':
                if stack:
                    stack.pop()
                else:
                    # if close parentheses couldn't find a open parentheses
                    s[i] = ""
        
        while stack:
            s[stack.pop()] = ""
        
        return ''.join(s)