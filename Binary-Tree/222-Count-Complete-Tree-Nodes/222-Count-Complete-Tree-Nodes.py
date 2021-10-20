# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        h = 0
        dummy = root
        # get the height of the root
        while dummy:
            dummy = dummy.left
            h += 1
        # get the min and max nums of nodes at the last level
        low = pow(2, h-1)
        hi = pow(2, h) -1
        # binary search
        while low < hi:
            mid = low + (hi-low+1)//2
            if self.hasK(mid, root):
                low = mid
            else:
                hi = mid - 1
        return low
    
    def hasK(self, K, root) -> int:
        """ To check whether root has K node
        Args:
            K: int 
        Return:
            boolean: true if exists else false
        """
        path = []
        while K > 0:
            path.append(K)
            K = K//2
        for i in range(len(path)-1, -1, -1):
            if root is None: 
                return False
            if i == 0: 
                return True
            if path[i-1] == 2 * path[i]:
                root = root.left
            else:
                root = root.right 
        return False

# TC: O(d**2) d is the depth of the tree
# SC: O(d)
                