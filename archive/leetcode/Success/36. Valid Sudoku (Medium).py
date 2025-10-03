class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not self.check(board, board[i][j], i, j):
                        return False
        return True
    
    def check(self, board, to_check, check_i, check_j):
        for i in range(9):
            if check_i != i and to_check == board[i][check_j]:
                return False
        for j in range(9):
            if check_j != j and to_check == board[check_i][j]:
                return False
        if check_i < 3:
            i_low, i_high = 0, 3
        elif check_i < 6:
            i_low, i_high = 3, 6
        elif check_i < 9:
            i_low, i_high = 6, 9
        if check_j < 3:
            j_low, j_high = 0, 3
        elif check_j < 6:
            j_low, j_high = 3, 6
        elif check_j < 9:
            j_low, j_high = 6, 9
        for i in range(i_low, i_high):
            for j in range(j_low, j_high):
                if i != check_i and j != check_j:
                    if board[i][j] == to_check:
                        return False
        return True
