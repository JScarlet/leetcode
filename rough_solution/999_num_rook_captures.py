class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == 'R':
                    direction_list = [[-1, 0], [0, -1], [1, 0], [0, 1]]
                    for direction in direction_list:
                        new_i = i + direction[0]
                        new_j = j + direction[1]
                        while 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                            if board[new_i][new_j] == 'p':
                                count += 1
                                break
                            elif board[new_i][new_j] == 'B':
                                break
                            else:
                                new_i += direction[0]
                                new_j += direction[1]
                    return count


if __name__ == '__main__':
    solution = Solution()
    board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    print(solution.numRookCaptures(board))
