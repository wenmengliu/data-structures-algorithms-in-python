# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def dfs(current_node):
            if current_node in nodes or not current_node:
                return current_node
            left, right = dfs(current_node.left), dfs(current_node.right)
            return current_node if left and right else left or right
        
        return dfs(root)