# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        """
        :type root: TreeNode
        :rtype res: List[int]
        """
        self.pos = 0
        self.flips = []
        def solve(root):
            if not root: return      
            if root.val != voyage[self.pos]:
                self.flips = [-1]
                return
            if root.left and root.left.val != voyage[self.pos + 1]:
                root.left, root.right = root.right, root.left
                self.flips.append(root.val)
            self.pos += 1
            solve(root.left)
            solve(root.right)    
        solve(root)
        return [-1] if -1 in self.flips else self.flips

# TC: O(N)
# SC: O(N)   