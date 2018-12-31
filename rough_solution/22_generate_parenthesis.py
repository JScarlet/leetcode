class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        final = []
        if n <= 0:
            return final
        # initial = '(' * n + ')' * n
        # result.append(initial)
        result = []
        for i in range(0, n):
            temp = []
            while len(result) > 0:
                index_list = result.pop()
                for j in range(i, i * 2 + 1):
                    if j > index_list[-1]:
                        temp_index_list = [each for each in index_list]
                        temp_index_list.append(j)
                        temp.append(temp_index_list)
            if len(temp) > 0:
                result.extend(temp)
            else:
                for j in range(i, i * 2 + 1):
                    index_list = [j]
                    result.append(index_list)
        for i in range(0, len(result)):
            temp = ''
            for j in range(0, n * 2):
                if j in result[i]:
                    temp += '('
                else:
                    temp += ')'
            final.append(temp)
        return final


if __name__ == '__main__':
    solution = Solution()
    n = 3
    print(solution.generateParenthesis(n))
