class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 1:
            return 0
        A = sorted(A)
        if A[0] + abs(K) < A[-1] - abs(K):
            return A[-1] - A[0] - 2 * abs(K)
        else:
            return 0


if __name__ == '__main__':
    solution = Solution()
    A = [1,3,6]
    K = 3
    print(solution.smallestRangeI(A, K))