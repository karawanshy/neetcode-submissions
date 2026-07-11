class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap, colMap, sqMap = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue

                sq = 3 * (i // 3) + (j // 3)

                if board[i][j] in rowMap[i] or board[i][j] in colMap[j] or board[i][j] in sqMap[sq]:
                    return False

                rowMap[i].add(board[i][j])
                colMap[j].add(board[i][j])
                sqMap[sq].add(board[i][j])

        return True
