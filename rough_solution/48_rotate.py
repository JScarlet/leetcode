class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(0, length // 2):
            for j in range(i, length - i - 1):
                origin_i = i
                origin_j = j
                count = 0
                temp = matrix[origin_i][origin_j]
                while count < 4:
                    dis_i = (length - 1) / 2 - origin_i
                    dis_j = (length - 1) / 2 - origin_j
                    print(dis_i, dis_j)
                    print(int((length - 1) / 2 - dis_j), int((length - 1) / 2 + dis_i))
                    matrix[int((length - 1) / 2 - dis_j)][int((length - 1) / 2 + dis_i)], temp = temp, matrix[int((length - 1) / 2 - dis_j)][int((length - 1) / 2 + dis_i)]
                    count += 1
                    # print(length // 2 - dis_j, length // 2 + dis_i, matrix[length // 2 - dis_j][length // 2 + dis_i])
                    origin_i = int((length - 1) / 2 - dis_j)
                    origin_j = int((length - 1) / 2 + dis_i)

        # print(matrix)
        for i in range(len(matrix)):
            print(matrix[i])


        # best solution
        # matrix[:] = map(list, zip(*matrix[::-1]))


if __name__ == '__main__':
    solution = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate(matrix)
