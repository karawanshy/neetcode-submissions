class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        sqs = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                val = int(board[i][j]) - 1
                mask = 1 << val
                sq = (i // 3) * 3 + (j // 3)

                if mask & rows[i]:
                    return False
                if mask & cols[j]:
                    return False
                if mask & sqs[sq]:
                    return False
                
                rows[i] |= mask
                cols[j] |= mask
                sqs[sq] |= mask

        return True