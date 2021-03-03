# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.output = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def reverse(current_node):
            if not current_node:
                return False
            
            left = reverse(current_node.left)
            right = reverse(current_node.right)
            
            mid = current_node == p or current_node == q
            
            if mid + left + right > 1:
                self.output = current_node
            
            return mid or left or right
        
        reverse(root)
        
        return self.output
## TC: O(N) where N is the number of nodes in BT. The worst case is that we need to visit all the nodes of the BT.
## SC: O(N) this is bc/ the maximum amount of space utilized by the recursion stack would be N since the height of a skewed binarny tree could be N