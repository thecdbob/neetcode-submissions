class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        hashRows = [set() for _ in range(9)]
        hashColumns = [set() for _ in range(9)]
        hashGrids = dict()
        for i in range(3):
            for j in range(3):
                hashGrids[(i, j)] = set()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] in hashRows[i]:
                    return False
                elif board[i][j] in hashColumns[j]:
                    return False
                else:
                    if board[i][j] != ".":
                        if board[i][j] in hashGrids[(i//3, j//3)]:
                            return False
                        else: 
                            hashGrids[(i//3, j//3)].add(board[i][j])
                            hashRows[i].add(board[i][j])
                            hashColumns[j].add(board[i][j])
        return True
