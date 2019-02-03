class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # if len(board) == 1 and len(board[0]) == 1:
        #     if board[0][0] == word:
        #         return True
        #     return False
        reach_set = set()
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if board[i][j] == word[0]:
                    if self.dfs(board, word, reach_set, i, j):
                        return True
        return False


    def dfs(self, board, word, reach_set, center_i, center_j):
        if word == '':
            return True
        if board[center_i][center_j] != word[0]:
            return False
        # reach_set.add()
        direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        candidate_list = []
        for i in range(len(direction)):
            temp_i = center_i + direction[i][0]
            temp_j = center_j + direction[i][1]
            if 0 <= temp_i < len(board) and 0 <= temp_j < len(board[temp_i]) and (temp_i, temp_j) not in reach_set:
                candidate_list.append([temp_i, temp_j])
        if len(candidate_list) == 0:
            if board[center_i][center_j] == word:
                return True
            return False
        for i in range(0, len(candidate_list)):
            if self.dfs(board, word[1:], reach_set | {(center_i, center_j)}, candidate_list[i][0], candidate_list[i][1]):
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCCE'
    # board = [['a']]
    # word = 'a'
    print(solution.exist(board, word))