class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        upRow = 0
        downRow = len(matrix)-1
        while upRow <= downRow:
            midRow = upRow +(downRow-upRow)//2
            if matrix[midRow][0]<target:
                upRow = midRow+1
            elif matrix[midRow][0]>target:
                downRow = midRow-1
            else:
                return True
        
        upCol = 0
        downCol = len(matrix[0])-1
        while upCol <= downCol:
            midCol = upCol +(downCol-upCol)//2
            if matrix[downRow][midCol]<target:
                upCol = midCol+1
            elif matrix[downRow][midCol]>target:
                downCol = midCol-1
            else:
                return True

        return False
