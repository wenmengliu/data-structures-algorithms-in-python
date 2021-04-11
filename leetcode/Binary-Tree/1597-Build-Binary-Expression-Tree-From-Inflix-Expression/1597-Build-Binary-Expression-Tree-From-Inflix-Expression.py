# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        ops, nums = [], []
        def compute():
            op = ops.pop()
            r = nums.pop()
            l = nums.pop()
            nums.append(Node(val = op, left = l, right = r))
        for ch in s:
            if ch.isdigit():
                nums.append(Node(val=ch))
            elif ch in ['+','-']:
                # merge the top two nodes
                while ops and ops[-1] in ['+','-','*','/']:
                    compute()
                ops.append(ch)
            elif ch in ['*','/']:
                while ops and ops[-1] in ['*','/']:
                    compute()
                ops.append(ch)
            elif ch == '(':
                ops.append('(')
            elif ch == ')':
                while ops[-1] != '(':
                    compute()
                ops.pop()
        while ops:
            compute()
        return nums[0]

# TC: O(N)
# SC: O(N)
# two stack solution