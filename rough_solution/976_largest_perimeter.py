class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A, reverse=True)
        print(A)
        for i in range(0, len(A) - 2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0


if __name__ == '__main__':
    solution = Solution()
    A = [1,2,1]
    print(solution.largestPerimeter(A))
