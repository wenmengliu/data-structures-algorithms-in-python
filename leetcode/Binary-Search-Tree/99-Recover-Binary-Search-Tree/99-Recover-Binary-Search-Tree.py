# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lastSeen = TreeNode(float('-inf'))
        self.first = TreeNode(None)
        self.second = TreeNode(None)
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(current_node):
            if not current_node:
                return
            
            dfs(current_node.left)   
            if current_node.val >= self.lastSeen.val:
                self.lastSeen = current_node
            else:
                if not self.first.val:
                    self.first = self.lastSeen
                    self.second = current_node
                    self.lastSeen = current_node
                else:
                    self.second = current_node
                    return
            dfs(current_node.right)
            
        dfs(root)
        tmp = self.first.val
        self.first.val = self.second.val
        self.second.val = tmp