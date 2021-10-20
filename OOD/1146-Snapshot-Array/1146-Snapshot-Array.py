class SnapshotArray:
    
    def __init__(self, length: int):
        self.arr = {}
        self.snap_d = {}
        self.snap_id = -1
    
    def set(self, index: int, val: int) -> None:
        self.arr[index] = val

    def snap(self) -> int:
        self.snap_id += 1
        self.snap_d[self.snap_id] = self.arr.copy()
        return self.snap_id
        
    def get(self, index: int, snap_id: int) -> int:
        if snap_id in self.snap_d:
            arr = self.snap_d[snap_id]
            if index in arr:
                return arr[index]
        return 0

# Use Hashmap
# insert : O(1), get : O(1)
# SC: O(N*S)

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)