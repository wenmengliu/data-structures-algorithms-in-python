class Node:
    
    def __init__ (self, val = -1, right = None, down = None):
        # add a dummy head -1 
        self.val = val
        self.right = right
        self.down = down
        
class Skiplist:

    def __init__(self):
        self.head = Node() # dummy head 
        
    def search(self, target: int) -> bool:
        node = self.head
        while node:
            # scan the current level
            while node.right and node.right.val < target:
                node = node.right
            # find the target value
            if node.right and node.right.val == target:
                return True
            # otherwise go to the next level (down)
            node = node.down
        return False
    
    def add(self, num: int) -> None:
        nodes = []
        node = self.head
        # get the largest node at each level that less than num
        while node:
            while node.right and node.right.val < num:
                node = node.right
            # save the largetest node at current level that its value is smaller than num
            nodes.append(node)
            node = node.down
        
        insert = True
        down = None
        # insert from the bottom to the top, insert p = 1, 0.5, 0.25 ,...
        while insert and nodes:
            node = nodes.pop()
            node.right = Node(num, node.right, down)
            down = node.right
            insert = (random.getrandbits(1) == 0)
        
        # if dataset is too large and then create a dummy head, right = none
        if insert:
            self.head = Node(-1 ,None, self.head)
            
    def erase(self, num: int) -> bool:
        ans = False
        node = self.head
        while node:
            # move to the right in the current level
            while node.right and node.right.val < num:
                node = node.right
            # find the target node
            if node.right and node.right.val == num:
                ans = True
                # delete by skipping 
                node.right = node.right.right
            # move to the next level
            node = node.down 
        return ans



# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)