class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        # Get the indexes of elements when the array is sorted by increasing value 
        idxs_sorted_by_values = sorted(range(n), key = lambda i: arr[i])
        odd_next_hops = self.getNextHops(idxs_sorted_by_values)
        # Get the indexes of elements when the array is sorted by decreasing value
        idxs_sorted_by_values.sort(key = lambda i: -arr[i])
        even_next_hops = self.getNextHops(idxs_sorted_by_values)
        even, odd = [False] * n, [False] * n
        even[-1], odd[-1] = True, True
        
        for i in reversed(range(n-1)):
            odd_next_hop, even_next_hop = odd_next_hops[i], even_next_hops[i]
            if odd_next_hop: odd[i] = even[odd_next_hop]
            if even_next_hop: even[i] = odd[even_next_hop]
        return sum(odd)
    
    def getNextHops(self, arr):
        next_hops = [None] * len(arr)
        stack = []
        for idx in arr:
            # generate a mono decreasing stack
            while stack and stack[-1] < idx:
                next_hops[stack.pop()] = idx
            stack.append(idx)
        return next_hops