class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0, 0, float('inf'), float('-inf')
            N1, n1, min1, max1 = dfs(root.left)
            N2, n2, min2, max2 = dfs(root.right)
            n = n1 + n2 + 1 if max1 < root.val < min2 else float('-inf')
            return max(N1,N2,n), n, min(root.val, min1), max(root.val, max2)
        return dfs(root)[0]