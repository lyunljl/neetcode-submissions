class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        I intend on using binary search...
        lets call the matrix n by m
        since the matrix is SORTED we know that we can first check if target is in betweeen 
        the values represented by a left and right pointer then whichever row/column that is.
        we will then go through that row/column using a normal binary search

                m                              [1,2,3,4,5]
            [1,2,3,4]                          [6,7,8,9,10]
        n   [5,6,7,8]
            [9,10,11,12]
        '''

        for m in range(len(matrix)): #iterate through the rows
            for n in range(len(matrix[m])): #iterate through the values
                left = 0
                right = len(matrix[m]) - 1
                while left <= right:
                    mid = (left+right) // 2
                    if matrix[m][mid] == target:
                        return True
                    elif matrix[m][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False







        return false