# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        def dfs(current_node):
            if not current_node or current_node.val == p or current_node.val == q:     
                return current_node
            left, right = dfs(current_node.left), dfs(current_node.right)
            return current_node if left and right else left or right
        
        def dist(node, target):
            if not node:
                return float('inf')
            if node.val == target:
                return 0

            return 1 + min(dist(node.left, target), dist(node.right, target))
        
        lca = dfs(root)
        return dist(lca,p) + dist(lca,q)