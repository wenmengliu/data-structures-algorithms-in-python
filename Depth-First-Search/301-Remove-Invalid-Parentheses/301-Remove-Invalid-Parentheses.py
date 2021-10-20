class Solution:
    def __init__(self):
        self.ans = []
        
    def removeInvalidParentheses(self, s: str) -> List[str]:
        l = r = 0
        # to calculate how many unbalanced '(' and ')' that need to be removed
        for c in s:
            if c == '(': 
                l += 1        
            if l == 0:
                r += 1 if c == ')' else 0
            else:
                l -= 1 if c ==')' else 0
        self.dfs(s, 0, l, r)
        return self.ans
    
    def isValid(self, s):
        count = 0
        for c in s:
            if c == '(': count += 1
            elif c == ')': count -= 1
            if count < 0: return False
        return count == 0
    
    def dfs(self, s, start, l, r):
        # when l == 0 and r == 0 and s is valid adding to ans
        # nothing to remove  
        if l == 0 and r == 0:
            if self.isValid(s):
                self.ans.append(s)
            return
        
        for i in range(start, len(s)):
            # only remove the first parentheses if they are consecutive ones to avoid duplicates
            if i != start and s[i] == s[i-1]: continue
            if s[i] == '(' or s[i] == ')':
                # to remove the parentheses
                # to firstly remove ')' right parenthese to make prefix valid
                if r > 0 and s[i] == ')':
                    curr = s[:i] + s[i+1:]
                    self.dfs(curr, i, l, r-1)
                elif l > 0 and s[i] == '(':
                    curr = s[:i] + s[i+1:]
                    self.dfs(curr, i, l-1, r)