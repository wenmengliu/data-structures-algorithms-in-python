class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        r, c = len(maze), len(maze[0])
        q = collections.deque([start])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        
        # mark starting point as visited
        maze[start[0]][start[1]] = 2
        # bfs
        while q:
            x, y = q.popleft()
            if x == destination[0] and y == destination[1]:
                return True
            for dx, dy in dirs:
                row = x + dx
                col = y + dy 
                # stop conidtion
                while 0 <= row < r and 0 <= col < c and maze[row][col] != 1:
                    row += dx
                    col += dy
                # go back
                row -= dx
                col -= dy
                if maze[row][col] == 0:
                    q.append([row, col])
                    # mark as visited
                    maze[row][col] = 2
        return False
            