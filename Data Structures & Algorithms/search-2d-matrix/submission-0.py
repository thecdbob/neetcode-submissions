class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        cm = 0
        while left<=right:
            cm = left+((right-left)>>1)
            if matrix[cm][len(matrix[cm])-1] < target:
                left = cm+1
            elif matrix[cm][0] > target:
                right = cm-1
            else:
                break
        rleft = 0
        rright = len(matrix[cm]) - 1
        rm = 0
        while rleft <= rright:
            rm = rleft+((rright-rleft)>>1)
            if matrix[cm][rm] < target:
                rleft = rm + 1
            elif matrix[cm][rm] > target:
                rright = rm - 1
            else:
                return True
        return False

            