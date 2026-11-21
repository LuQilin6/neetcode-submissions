class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix[0])
        colLen = len(matrix)
        right= rowLen*colLen-1
        left = 0
        while left <= right:
            mid = left+int((right-left)/2)
            rowInd = mid//rowLen
            colInd = mid%rowLen
            midVal = matrix[rowInd][colInd]
            if midVal < target:
                left = mid + 1 
            elif midVal >target:
                right = mid - 1
            else:
                return True
        
        return False

        