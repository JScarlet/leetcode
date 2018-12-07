class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if A is None:
            return None
        if len(A) == 0:
            return A
        for i in range(0, len(A)):
            A[i] = A[i][::-1]
            for j in range(0, len(A[i])):
                print(A[i][j])
                A[i][j] = A[i][j] ^ 1
        return A


if __name__ == '__main__':
    solution = Solution()
    A = [[1,1,0],[1,0,1],[0,0,0]]
    print(solution.flipAndInvertImage(A))
