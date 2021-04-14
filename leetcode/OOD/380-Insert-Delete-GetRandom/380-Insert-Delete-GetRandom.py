class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict: 
            return False
        # add value and its index into a dict. average O(1) time
        self.dict[val] = len(self.list)
        # append value to array list. average O(1) time
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict:
            return False
        # move the last element to the place idx of the element to delete
        last_element, idx = self.list[-1], self.dict[val]
        # swap them
        self.list[idx], self.dict[last_element] = last_element, idx
        # delete the val in a dict and arr
        # pop the last element out. O(1)
        self.list.pop()
        # delete in O(1)
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        # random.choice get O(1) time 
        return choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()