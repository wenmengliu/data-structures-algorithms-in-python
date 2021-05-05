class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        """ BFS
        TC: O(N)
        SC: O(N)
        """
        q, n = [start], len(arr)
        
        while q:
            idx = q.pop()
            # it has reached zero
            if arr[idx] == 0:
                return True
            # node has visited
            if arr[idx] < 0:
                continue
            for i in [idx+arr[idx], idx-arr[idx]]:
                if 0 <= i < n and arr[idx] != -1:
                    q.append(i)
            # mark node as visited w/ negative value
            arr[idx] = -1
        return False