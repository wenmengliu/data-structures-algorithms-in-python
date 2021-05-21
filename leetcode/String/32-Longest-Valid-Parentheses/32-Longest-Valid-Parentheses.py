class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, res = [0], 0
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    res = max(res, stack[-1])
                else:
                    # reset to 0
                    stack[-1] = 0
        return res