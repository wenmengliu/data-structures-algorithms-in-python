class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DLinkedNode(0,0)
        self.tail = DLinkedNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            # remove an node from the existing Linked list
            self._remove(node)
            # move an evicted node after head
            self._add(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])
        node = DLinkedNode(key, value)
        self._add(node)
        self.dict[key] = node
        if len(self.dict) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dict[n.key]
    
    
    def _remove(self, node):
        p = node.prev 
        n = node.next 
        p.next = n
        n.prev = p
    
    
    def _add(self, node):
        p = self.tail.prev 
        p.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = p

class DLinkedNode():
    
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

# HashTable + DoubleLinkedList to achieve put and get in O(1) time
# Access to a random key in O(1) -> hashtable
# remove the first entry in LRU cache in O(1) -> list
# add/move an entry to the end of LRU cache in O(1) -> list


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)