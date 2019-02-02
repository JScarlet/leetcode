class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        chess_list = [['.' for i in range(n)] for i in range(n)]
        result = []
        for i in range(0, n):
            chess_list[0][i] = 'Q'
            if not self.dfs(chess_list, 1, result):
                chess_list[0][i] = '.'
            else:
                chess_list = [['.' for j in range(n)] for j in range(n)]
        final = []
        for each in result:
            each_result = []
            for i in range(len(each)):
                temp = ''
                for j in range(len(each[i])):
                    temp += each[i][j]
                each_result.append(temp)
            final.append(each_result)
        return final

    def dfs(self, chess_list, column, result):
        if column == len(chess_list):
            single_result = []
            for m in range(len(chess_list)):
                column = []
                for n in range(len(chess_list[m])):
                    column.append(chess_list[m][n])
                single_result.append(column)
            result.append(single_result)
            return True
        for i in range(0, len(chess_list[0])):
            chess_list[column][i] = 'Q'
            if self.is_satisfied(chess_list, column, i):
                if not self.dfs(chess_list, column + 1, result):
                    chess_list[column][i] = '.'
                else:
                    if i == len(chess_list[column]) - 1:
                        chess_list[column][i] = '.'
                        return True
                    else:
                        chess_list[column][i] = '.'
            else:
                chess_list[column][i] = '.'
        if chess_list[column].count('Q') == 0:
            return False
        return True

    def is_satisfied(self, chess_list, i, j):
        if chess_list[i].count('Q') > 1:
            return False
        temp = []
        for m in range(0, len(chess_list)):
            temp.append(chess_list[m][j])
        if temp.count('Q') > 1:
            return False
        temp_2 = []
        left_x, y1 = j, i
        while 0 <= left_x and y1 >= 0:
            temp_2.append(chess_list[y1][left_x])
            left_x -= 1
            y1 -= 1
        if temp_2.count('Q') > 1:
            return False

        temp_3 = []
        right_x, y2 = j, i
        while right_x < len(chess_list[0]) and y2 >= 0:
            temp_3.append(chess_list[y2][right_x])
            right_x += 1
            y2 -= 1
        if temp_3.count('Q') > 1:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    result = solution.solveNQueens(8)
    print(len(result))
    for each in result:
        print('-----------')
        for i in range(0, len(each)):
            print(each[i])

# [["Q......","..Q....","....Q..","......Q",".Q.....","...Q...",".....Q."],["Q......","...Q...","......Q","..Q....",".....Q.",".Q.....","....Q.."],["Q......","....Q..",".Q.....",".....Q.","..Q....","......Q","...Q..."],["Q......",".....Q.","...Q...",".Q.....","......Q","....Q..","..Q...."],[".Q.....","...Q...","Q......","......Q","....Q..","..Q....",".....Q."],[".Q.....","....Q..","Q......","...Q...","......Q","..Q....",".....Q."],[".Q.....",".....Q.","..Q....","......Q","...Q...","Q......","....Q.."],[".Q.....","......Q","....Q..","..Q....","Q......",".....Q.","...Q..."],["..Q....","Q......",".....Q.",".Q.....","....Q..","......Q","...Q..."],["..Q....","....Q..","......Q",".Q.....","...Q...",".....Q.","Q......"],["..Q....",".....Q.",".Q.....","....Q..","Q......","...Q...","......Q"],["..Q....","......Q",".Q.....","...Q...",".....Q.","Q......","....Q.."],["...Q...","Q......","..Q....",".....Q.",".Q.....","......Q","....Q.."],["...Q...",".Q.....","......Q","....Q..","..Q....","Q......","....
#
# [["Q......","..Q....","....Q..","......Q",".Q.....","...Q...",".....Q."],["Q......","...Q...","......Q","..Q....",".....Q.",".Q.....","....Q.."],["Q......","....Q..",".Q.....",".....Q.","..Q....","......Q","...Q..."],["Q......",".....Q.","...Q...",".Q.....","......Q","....Q..","..Q...."],[".Q.....","...Q...","Q......","......Q","....Q..","..Q....",".....Q."],[".Q.....","...Q...",".....Q.","Q......","..Q....","....Q..","......Q"],[".Q.....","....Q..","Q......","...Q...","......Q","..Q....",".....Q."],[".Q.....","....Q..","..Q....","Q......","......Q","...Q...",".....Q."],[".Q.....","....Q..","......Q","...Q...","Q......","..Q....",".....Q."],[".Q.....",".....Q.","..Q....","......Q","...Q...","Q......","....Q.."],[".Q.....","......Q","....Q..","..Q....","Q......",".....Q.","...Q..."],["..Q....","Q......",".....Q.",".Q.....","....Q..","......Q","...Q..."],["..Q....","Q......",".....Q.","...Q...",".Q.....","......Q","....Q.."],["..Q....","....Q..","......Q",".Q.....","...Q...",".....Q.","Q...

