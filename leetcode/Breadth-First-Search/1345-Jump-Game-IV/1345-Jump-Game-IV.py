class Solution:
    """BFS
    TC: O(n)
    SC: O(n)
    """
    def minJumps(self, arr: List[int]) -> int:
        graph = defaultdict(list)
        # to save all elems in the graph
        for i, n in enumerate(arr):
            graph[n].append(i)
        visited, queue = set(), deque()
        node, dest = 0, len(arr)-1
        queue.append((node,0))
        visited.add(node)
        
        while queue:
            node, dist = queue.popleft()
            if node == dest:
                return dist
            for child in [node+1, node-1] + graph[arr[node]][::-1]:
                if 0 <= child < len(arr) and child != node and child not in visited:
                    if child == dest:
                        return dist + 1
                    queue.append((child, dist+1))
                    visited.add(child)
             # clear the list to prevent redundant search
            graph[arr[node]].clear()
        return -1
