class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        build a visited set to store all the visited postions
        setup an island counter
        loop through all indicies
            if an unvisited position is encountered and its not water
                run dfs ... but how do we tell when the island ends?
            else: aka already visited before
                just move on
        
        """
        islands = 0
        visited = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0" or (i,j) in visited:
                return
        
            visited.add((i,j))

            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i+1, j)
            dfs(i-1, j)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    islands += 1
                    dfs(i,j)
                else:
                    continue
        return islands


        
