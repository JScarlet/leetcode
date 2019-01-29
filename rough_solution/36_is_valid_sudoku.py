class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0, len(board)):
            temp = set()
            for j in range(0, len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] not in temp:
                        temp.add(board[i][j])
                    else:
                        return False
        # print('111')
        for i in range(0, len(board[0])):
            temp = set()
            for j in range(0, len(board)):
                if board[j][i] != '.':
                    if board[j][i] not in temp:
                        temp.add(board[j][i])
                    else:
                        return False
        # print('222')
        for i in range(0, 3):
            for j in range(0, 3):
                temp = set()
                for m in range(3 * i, 3 * (i + 1)):
                    for n in range(3 * j, 3 * (j + 1)):
                        if board[m][n] != '.':
                            if board[m][n] not in temp:
                                temp.add(board[m][n])
                            else:
                                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    print(solution.isValidSudoku(board))