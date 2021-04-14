class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict ={}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val in self.dict:
            self.dict[val] = self.dict[val] + [len(self.list)]
            self.list.append(val)
            return False
        
        self.dict[val] = [len(self.list)]
        self.list.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.dict:
            last_element, idx = self.list[-1], self.dict[val][-1]
            self.list[-1], self.list[idx] = self.list[idx], last_element
            self.list.pop()
            self.dict[last_element][-1] = idx
            self.dict[last_element].sort()
            self.dict[val].pop()
            if not self.dict[val]:
                del self.dict[val]
            return True
        
        return False
            
    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.list)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()