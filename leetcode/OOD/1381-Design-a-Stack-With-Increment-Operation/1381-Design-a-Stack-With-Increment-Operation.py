class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        
    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return
        self.stack.append(x)
            
    def pop(self) -> int:
        if not self.stack:
            return -1
        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) <= k:
            self.stack = [x+val for x in self.stack]
        else:
            sub_stack = self.stack[:k]
            sub_stack = [x+val for x in sub_stack]
            self.stack = sub_stack + self.stack[k:]
        return self.stack

# init: O(1), push: O(1), pop: O(1), inc: O(k)
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)