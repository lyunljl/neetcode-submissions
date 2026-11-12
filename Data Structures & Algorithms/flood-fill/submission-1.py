class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #eduardo
        # DFS needed for this graph problem
        #how many lists, length of any list
        # in a recursive function basecase is first
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]

        if original_color == color:
            return image
        
        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols or image[row][col] != original_color:
                return 
            else:
                image[row][col] = color
                dfs(row-1,col)
                dfs(row+1,col)
                dfs(row,col-1)
                dfs(row,col+1)
            return 

        dfs(sr,sc)
        return image