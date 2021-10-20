# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = collections.deque(preorder)
        def helper(preorder,inorder):
            if inorder:
                ind = inorder.index(preorder.popleft())
                root = TreeNode(inorder[ind])
                root.left = helper(preorder, inorder[:ind])
                root.right = helper(preorder, inorder[ind+1:])
                return root
        return helper(preorder, inorder)

# TC: O(N)
# SC: O(N)