class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        for i in range(0, len(A)):
            result.append(A[i] ** 2)
        result.sort()
        return result


if __name__ == '__main__':
    solution = Solution()
    A = [-7,-3,2,3,11]
    print(solution.sortedSquares(A))
