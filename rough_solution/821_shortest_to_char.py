class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c_index_list = []
        for i in range(0, len(S)):
            if C == S[i]:
                c_index_list.append(i)

        result = []
        j = 0
        for i in range(0, len(S)):
            if i < c_index_list[j]:
                if j == 0:
                    result.append(abs(i - c_index_list[j]))
                else:
                    result.append(min(abs(i - c_index_list[j]), abs(i - c_index_list[j-1])))
            elif i > c_index_list[j]:
                if j == len(c_index_list) - 1:
                    result.append(abs(i - c_index_list[j]))
                else:
                    result.append(min(abs(i - c_index_list[i]), abs(i - c_index_list[i+1])))
            else:
                result.append(0)
                if j < len(c_index_list) - 1:
                    j += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    S = "loveleetcode"
    C = 'e'
    print(solution.shortestToChar(S, C))
