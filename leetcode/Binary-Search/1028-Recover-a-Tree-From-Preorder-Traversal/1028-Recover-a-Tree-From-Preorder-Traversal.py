# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def recoverFromPreorder(self, S: str) -> TreeNode:
        stack, i, n = [], 0, len(S)
        while i < n:
            d, val = 0, 0
            # get the depth
            while i < n and S[i]=='-':
                d += 1
                i += 1
            # get the value
            while i < n and S[i].isdigit():
                val = val * 10 + int(S[i])
                i += 1
            # make the number of stack is the same as the depth
            while len(stack) > d:
                stack.pop()
            node = TreeNode(val)
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            stack.append(node)
        return stack[0]

# TC: O(N)
# SC: O(N)
    