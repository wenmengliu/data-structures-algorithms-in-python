class DLL:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.dh = DLL(0,0)
        self.dt = DLL(-1, -1)
        self.dh.next = self.dt
        self.dt.prev = self.dh 
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # update the value similiar to get()
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeFromList(node)
            self.insertIntoHead(node)
        else:
            if len(self.cache) >= self.cap:
                self.removeFromTail()
            node = DLL(key, value)
            self.cache[key] = node
            self.insertIntoHead(node)
    
    def insertIntoHead(self, node):
        head_next = self.dh.next 
        self.dh.next = node
        node.prev = self.dh
        node.next = head_next
        head_next.prev = node 
    
    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def removeFromTail(self):
        if len(self.cache) == 0:
            return
        tail_node = self.dt.prev 
        del self.cache[tail_node.key]
        self.removeFromList(tail_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)