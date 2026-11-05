class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(row, col):
            area = 0
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1 or (row, col) in visited:
                return 0
            else:
                # now we've encounted an island
                visited.add((row, col))
                area = 1
                area += dfs(row - 1, col)
                area += dfs(row + 1, col)
                area += dfs(row, col + 1)
                area += dfs(row, col - 1)
            return area
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area


