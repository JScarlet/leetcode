class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(M) == len(M[0]) == 1:
            return M

        result = [[0 for j in range(len(M[0]))] for i in range(0, len(M))]
        for i in range(0, len(M)):
            for j in range(0, len(M[i])):
                point_index_list = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
                temp = 0
                count = 0
                for point_index in point_index_list:
                    # print(point_index)
                    if 0 <= point_index[0] < len(M) and 0 <= point_index[1] < len(M[i]):
                        # print(M)
                        # print(M[point_index[0]][point_index[1]])
                        temp += M[point_index[0]][point_index[1]]
                        count += 1
                # print(temp, count)
                # print(temp//count)
                result[i][j] = temp // count
        return result


if __name__ == '__main__':
    solution = Solution()
    M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
    print(solution.imageSmoother(M))


# 解题思路：
# 每个点都计算找出周围点，再根据题意计算每个点的数值
