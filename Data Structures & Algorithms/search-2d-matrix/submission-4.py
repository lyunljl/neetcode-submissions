class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        since the entire matrix is sorted just flatten the list and run a normal binary search
        '''
        array = []
        for m in matrix:
            for value in m:
                array.append(value)
        
        left = 0
        right = len(array) - 1

        while left <= right:
            mid = (left+right) // 2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False