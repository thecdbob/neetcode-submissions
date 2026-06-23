class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        lower, upper = 0, rows-1
        while lower <= upper:
            m = lower+((upper-lower)>>1)
            if matrix[m][0] > target:
                upper = m - 1
            elif matrix[m][columns-1] < target:
                lower = m + 1
            else:
                break
        if lower > upper:
            return False
        row = lower+((upper-lower)>>1)
        l, r = 0, columns - 1
        while l <= r:
            m = l+((r-l)>>1)
            if matrix[row][m] > target:
                r = m-1
            elif matrix[row][m] < target:
                l = m+1
            else:
                return True
        return False