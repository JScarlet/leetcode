class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(0, len(A[0])):
            temp = []
            for j in range(0, len(A)):
                temp.append(A[j][i])
            result.append(temp)
        return result


if __name__ == '__main__':
    solution = Solution()
    A = [[1,2,3],[4,5,6]]
    print(solution.transpose(A))
