class Solution:
    def scoreOfParentheses(self, s: str) -> int:
    	""" use Stack DS
    	
    	TC: O(n)
    	SC: O(1)
    	
    	Arguments:
    		s {str} -- [description]
    	
    	Returns:
    		int -- [description]
    	"""
        res = l = 0
        for a, b in zip(s, s[1:]):
            if a + b == '()': res += 1 << l
            l += 1 if a == '(' else -1
            
        return res