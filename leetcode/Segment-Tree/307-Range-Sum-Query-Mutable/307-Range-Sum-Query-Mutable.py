class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        # TC & SC: O(n)
        self.root = self.buildTree(0,len(nums)-1)
        
    def update(self, index: int, val: int) -> None:
        # TC: O(logK)
        # SC: O(1)
        return self.updateTree(self.root, index, val)
    
    def sumRange(self, left: int, right: int) -> int:
        # TC: O(logn + k)
        # SC: O(1)
        return self.rangeSum(self.root, left, right)
    
    def buildTree(self, start, end):
        # base case: for lead node
        if start == end:
            node = SegmentTreeNode(start, end)
            node.sum = self.nums[start]
            return node
        # build up tree like BST
        # TC: O(n) = n + n/2 + n/4 +... + 1 ~ 2n
        # SC: O(n) we used 2n extra space to store the segment tree
        mid = (start + end) // 2
        # build up left and right tree 
        root = SegmentTreeNode(start, end)
        
        root.left = self.buildTree(start, mid)
        root.right = self.buildTree(mid+1, end)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def updateTree(self, root, index,val):
        # binary search O(logn)
        if root.start == root.end == index:
            root.sum = val
            return root.sum
        mid = (root.start + root.end)//2
        if index <= mid:
            self.updateTree(root.left, index, val)
        else:
            self.updateTree(root.right, index, val)
        # update root value!
        root.sum = root.left.sum + root.right.sum
        return root.sum
    
    def rangeSum(self, root, i, j):
        # base case
        if i == root.start and j == root.end:
            return root.sum
        
        mid = (root.start + root.end)//2
        if j <= mid:
            return self.rangeSum(root.left, i, j)
        elif i >= mid+1:
            return self.rangeSum(root.right, i, j)
        else:
            return self.rangeSum(root.left, i, mid) + self.rangeSum(root.right, mid+1, j)
        
        
class SegmentTreeNode:
    def __init__(self,start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)