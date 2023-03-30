class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set() # set of (r,c) 
        
        def bfs(r, c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            
            # move          left   right    up      down
            shifts = [(-1, 0), (+1, 0), (0, 1), (0, -1)]
            while q:
                row, col = q.popleft()
                for shift_x, shift_y in shifts:
                    r, c = row + shift_x, col + shift_y
                    if (  0 <= r < rows and 0 <= c < cols and
                            (r,c) not in visited and grid[r][c] == '1'):
                        q.append((r,c))
                        visited.add((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited: # island 
                    islands +=1
                    bfs(r,c)
                    
        return islands