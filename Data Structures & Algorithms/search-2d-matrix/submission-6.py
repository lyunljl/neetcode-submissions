class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # naive solution for funzies
        for row in matrix:
            for value in row:
                if value == target:
                    return True
        return False