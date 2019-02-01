class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        i, j = 0, 0
        # num_set = set([each for each in board[i] if each != '.'])
        self.dfs(i, j, board)

    def dfs(self, i, j, board):
        if j == 9:
            i += 1
            j = 0
        if i == 9:
            return True
        if board[i][j] == '.':
            for m in range(1, 10):
                board[i][j] = str(m)
                if not self.isValidSudoku(board) or not self.dfs(i, j + 1, board):
                    board[i][j] = '.'
                    continue
                else:
                    return True
            if board[i][j] == '.':
                return False
            else:
                return True
        else:

            return self.dfs(i, j + 1, board)

    def print_board(self, board):
        # f.write('-----------\n')
        print('----------')
        for i in range(0, len(board)):
            # f.write(str(board[i]) + '\n')
            print(board[i])

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
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solution.solveSudoku(board)
    solution.print_board(board)
