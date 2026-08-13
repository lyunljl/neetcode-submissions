class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
                """
                conditions to claim a perimeter...
                detects if i/j are at their borders
                detects if i/j are at their other borders
                detects if current square is water

                all of these allow us to basicaly claim a perimeter
                """
                return 1

            if (i,j) in visited:
                return 0
            
            visited.add((i,j))

            perimeter = dfs(i, j+1) #dfs on the cell to the right
            perimeter += dfs(i + 1, j) #dfs on the below cell
            perimeter += dfs(i, j-1) #dfs on the cell to the left
            perimeter += dfs(i - 1, j) #dfs on the cell to the top

            return perimeter
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)